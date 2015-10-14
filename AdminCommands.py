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

def addword(client, message):
	import sqlite3 as sql
	con = sql.connect('discwords')
	cur = con.cursor()
	keyword = str(message.content).split(" ")
	try:
		cur.execute('''INSERT INTO links (word,url) VALUES (?,?)''', (keyword[1], keyword[2]))
		cur.commit()
		client.send_message(message.channel, "Adding Keyword: " + keyword[1] + " with URL: " + keyword[2])
	except:
		client.send_message(message.channel, 'Unable to add keyword: %s' % keyword[1])
	
	
	
	
adminStrings = {'!exit': exitbot, '!addkeyword': addword}
