
import DiscordImpostor.Server
import DiscordImpostor.Message
import DiscordImpostor.User


class Channel:

    def __init__(self, id, agent):
        self.id = id
        self.agent = agent
        self.name = ''
        self.guild = None

    def load(self):
        channel_json = self.agent.authorized_get('https://discord.com/api/v8/channels/' + self.id).json()
        self.name = channel_json['name']
        self.guild = DiscordImpostor.Server.Server(self.agent, channel_json['guild_id'])

    def send_msg(self, content):
        url = 'https://discord.com/api/v8/channels/' + self.id + '/messages'
        data = {
            'content': content
        }
        self.agent.authorized_post(url, data)

    def get_newest_msg(self):
        msg_data = self.agent.authorized_get('https://discord.com/api/v8/channels/' + self.id + '/messages').json()[0]
        return self.get_msg_from_json(msg_data)

    def get_msgs(self, amount=10):
        msgs_left = amount
        msgs = []
        curr_id = ''
        page = 1
        while msgs_left > 0:
            get_amount = min(msgs_left, 100)
            if amount >= 1000:
                print('Reading messages (' + str(page) + '/' + str(amount / 100) + ')')
            id_text = ''
            if curr_id != '':
                id_text = '&before=' + curr_id
            msgs_data = self.agent.authorized_get('https://discord.com/api/v8/channels/' + self.id + '/messages?limit=' + str(get_amount) + id_text).json()
            for msg_json in msgs_data:
                msgs.append(self.get_msg_from_json(msg_json))
            msgs_left -= get_amount
            curr_id = msgs[len(msgs) - 1].id
            page += 1
        return msgs

    def get_msg_from_json(self, msg_data):
        msg = DiscordImpostor.Message.Message(msg_data['id'], self.agent)
        msg.content = msg_data['content']
        msg.channel = self
        msg.author = DiscordImpostor.User.User(msg_data['author']['id'], self.agent)
        msg.author.username = msg_data['author']['username']

        return msg