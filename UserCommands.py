#UserComamnds.py
import discord

def hello(message):
	print "inside hello"
	print message.channel
	print message.author.name
	try:
		client.send_message(message.channel, 'Hello %s , I am HammerBot' % message.author.name)
	except:
		print "could not send"
	
def bye():
	print "in the bye module"
	return()