
import Channel


class Message:

    def __init__(self, id, agent):
        self.id = id
        self.agent = agent
        self.content = ''
        self.author = None
        self.channel = None