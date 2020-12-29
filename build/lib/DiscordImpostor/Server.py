
import DiscordImpostor.Channel


class Server:

    def __init__(self, agent, id):
        self.agent = agent
        self.id = id
        self.name = ''
        self.emoji = []
        self.channels = []

    def load(self):
        data = self.agent.authorized_get('https://discord.com/api/v8/guilds/' + self.id).json()

        self.name = data['name']
        self.emoji = data['emojis']

    def load_channels(self):
        channels_json = self.agent.authorized_get('https://discord.com/api/v8/guilds/' + self.id + '/channels').json()

        for channel_json in channels_json:
            channel = DiscordImpostor.Channel.Channel(channel_json['id'], self.agent)
            channel.name = channel_json['name']
            channel.guild = self
            self.channels.append(channel)
