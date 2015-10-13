#UserComamnds.py

def hello(client, message):
		client.send_message(message.channel, 'Hello %s , I am HammerBot' % message.author.name)
	
def bye():
	print "I am not going away, so why don't you leave!"
	return()