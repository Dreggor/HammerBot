#AdminComamnds.py
import sys
import datetime, time

def consolelog(name, content):
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	print("User: " + name + " ran command: " + content + " at: " + st)

def exitbot(client, message):
	client.send_message(message.channel, 'Discord Bot Stopping')
	consolelog(message.author.name, str(message.content))
	sys.exit(0)

adminStrings = {'!exit': exitbot}
