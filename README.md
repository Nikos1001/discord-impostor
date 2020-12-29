# discord-impostor
A python package for creating Discord bots that pretend to be real users

### Installation

To install discord-impostor, simply run ```pip install discord-impostor```

### Basic Usage

To login into Discord with discord-imposter, you need to create and authorize an "Agent".

```

from DiscordImpostor.Agent import Agent

agent = Agent()
agent.login('<your-email-here>', '<your-password-here>')

```

An agent can do many of the actions a normal user can. For example, an agent can read / write messages in a channel

```

from DiscordImpostor.Channel import Channel

channel = Channel('<channel-id>', agent)
channel.load()

latest_msg = channel.get_newest_msg()
print(latest_msg.content)

channel.send_msg('Hello World!')

```

To see the full functionality, take a look at the source code.

### Pypi Page

https://pypi.org/project/discord-impostor/1.0.0/