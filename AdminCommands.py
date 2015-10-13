#AdminComamnds.py
import sys

def exitbot(client, message):
	client.send_message(message.channel, 'Discord Bot Stopping')
	sys.exit(0)

	
