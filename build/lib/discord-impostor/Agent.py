import requests
import Server


class Agent:

    def __init__(self):
        self.token = ''
        self.servers = []

    def login(self, login, password):

        login_url = 'https://discord.com/api/v8/auth/login'
        login_data = {
            'login': login,
            'password': password
        }
        headers = {
            'Content-Type': 'application/json'
        }

        token_responce = requests.post(login_url, json=login_data, headers=headers)

        self.token = token_responce.json()['token']

    def load_servers(self):
        request_url = 'https://discord.com/api/v8/users/@me/affinities/guilds'
        responce_json = self.authorized_get(request_url).json()
        for guild in responce_json['guild_affinities']:
            id = guild['guild_id']
            server = Server.Server(self, id)
            server.load()
            self.servers.append(server)

    def authorized_get(self, url, json=None):
        headers = {
            'authorization': self.token
        }
        return requests.get(url, headers=headers, json=json)

    def authorized_post(self, url, json):
        headers = {
            'authorization': self.token
        }
        return requests.post(url, headers=headers, json=json)
