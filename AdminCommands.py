#AdminComamnds.py
import sys
import datetime, time

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def consolelog(name, content):
	print("User: " + name + " ran command: " + content + " at: " + st)

def exitbot(client, message):
	client.send_message(message.channel, 'Discord Bot Stopping')
	consolelog(message.author.name, str(message.content))
	sys.exit(0)

def addword(client, message):  #deprecated
	import sqlite3 as sql
	con = sql.connect('discwords')
	cur = con.cursor()
	keyword = str(message.content).split(" ")
	try:
		print("Attempting to add: " + keyword[1] + " To URL: " +keyword[2])
		cur.execute('''INSERT INTO links (word,url) VALUES (?,?)''', (keyword[1], keyword[2]))
		con.commit()
		con.close()
		client.send_message(message.channel, "Adding Keyword: " + keyword[1] + " with URL: " + keyword[2])
		print("User: " + message.author.name + "Added keyword: " + keyword[1] + " That has URL: " + keyword[2] + " At: " + str(st))
	except:
		client.send_message(message.channel, 'Unable to add keyword: %s' % keyword[1])
	
def delword(client, message):   #deprecated
	import sqlite3 as sql
	con = sql.connect('discwords')
	cur = con.cursor()
	keyword = str(message.content).split(" ")
	cur.execute("DELETE FROM links WHERE word=%s" % keyword[1])
	con.commit()
	con.close()

def word(client, message):
	import sqlite3 as sql
	con = sql.connect('discwords')
	cur = con.cursor()
	commandline = str(message.content).split(" ")
	print commandline[1]
	if commandline[1] == "list":
		print "in list"
		cur.execute("SELECT * FROM links")
		rows = cur.fetchall()
		keywords = []
		for i in rows:
			keywords.append(str(i[0]))
		con.close()
		keywords = str(', '.join(keywords))
		client.send_message(message.channel, keywords )
		return()
	print "after list"
	if commandline[1] == "add":
		print add
		try:
			print("Attempting to add: " + keyword[2] + " To URL: " +keyword[3])
			cur.execute('''INSERT INTO links (word,url) VALUES (?,?)''', (keyword[2], keyword[3]))
			con.commit()
			con.close()
			client.send_message(message.channel, "Adding Keyword: " + keyword[2] + " with URL: " + keyword[3])
			print("User: " + message.author.name + "Added keyword: " + keyword[2] + " That has URL: " + keyword[3] + " At: " + str(st))
		except:
			client.send_message(message.channel, 'Unable to add keyword: %s' % keyword[1])
	if commandline[1] == "remove":
		print remove
		client.send_message(message.channel, "Command: " + commandline[0] + " " + commandline[1] + "Not yet implimented")
	else:
		client.send_message(message.channel, "Sorry " + message.author.name + " Comamnd !word does not have subcommand of " + commandline[1])
	
adminStrings = {'!exit': exitbot, '!word': word}
