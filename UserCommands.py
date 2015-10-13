#UserComamnds.py

def hello(client, message):
	client.send_message(message.channel, 'Hello %s , I am HammerBot' % message.author.name)
	
def bye(client, message):
	client.send_message(message.channel, "Sorry %s, I am not going anywhere, why don't you leave." % message.author.name)
