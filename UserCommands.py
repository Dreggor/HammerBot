#UserComamnds.py
import json

with open("config.json") as json_file:
    json_data = json.load(json_file)


def hello(client, message):
	client.send_message(message.channel, 'Hello %s , I am HammerBot' % message.author.name)
	
def bye(client, message):
	client.send_message(message.channel, "Sorry %s, I am not going anywhere, why don't you leave." % message.author.name)

def admins(client, message):	
	admins = str(', '.join(json_data['DiscBot']['admins']))
	name = str(json_data['DiscBot']['botname'])
	client.send_message(message.channel, "" + name + " admins are: " + admins)
	
userCommands = {'!hello': hello, '!bye': bye, '!admins': admins}