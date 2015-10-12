import discord
import sqlite3 as sql
import sys

client = discord.Client()
client.login(sys.argv[1], sys.argv[2]) #run commandline with <username> <password>

gBotName = 'HammerBot'
gAdmins = ['Dreggor', 'Dazik']
gDebug = '1'  #set to blank for no debug. This will be moved to a commandline switch at some point. FUTURE TODD, DO THIS!
gAdminChannel = 'bot-testing'
con = None

try: 
	con = sql.connect('hammerwords')
	cur = con.cursor()
	cur.execute("SELECT * FROM links")
	rows = cur.fetchall()
except sql.Error, e:
	print "Error %s:" % e.args[0]
	sys.exit(1)


@client.event
def on_message(message):
	if gDebug:
		print("" + message.author.name + ": " + message.content)
		print(message.channel.name)
		print(message.channel.id)
	if message.author.name == gBotName:
		return()
	elif message.content.startswith('!hello'):
		if message.author.name in gAdmins:
			client.send_message(message.channel, 'Hello %s , I am HammerBot' % message.author.name)
			if gDebug:
				client.send_message(message.channel, 'DEBUG-ACCEPT: Author ID: %s' % message.author.name)
				print('Message Author ID:', message.author.name)
				print('Originating Channel:', message.channel.name)
			return()
		else:
			if gDebug:
				client.send_message(message.channel, 'DEBUG-REJECT: Author ID: %s' % message.author.name)
			client.send_message(message.channel, 'Sorry, I do not like you and will not listen to you. Politely fuck off')
		return()
	elif message.content.startswith('!admin'):
		client.send_message(message.channel, 'HammerBot Admins are:')
	elif message.content.startswith('!exit'):
		client.send_message(message.channel, 'HammerBot shuuuuttttiiinnngggg dooooowwwwnnnnnnnn......')
		sys.exit(0)
	for row in rows:
		word = row[0]
		#print("Inside for statement for word scanning: " + word)
		if word in message.content:
			if gDebug:
				print rows[1]
			link = row[1]
			client.send_message(message.channel, link)

	
@client.event
def on_ready():
	print("Logged in as: " + client.user.name)
	print('------')
	print('Discord Admins:')
	for i in gAdmins:
		print("     " + i)
	print('------')
	print "Keywords in DB:"
	for row in rows:
		print("     " + row[0])
	print "------"
	channel = client.get_channel("98838694521229312")
	print(channel)
	client.send_message(channel, 'HammerBot ONLINE!')  # this does not work due to some crazy channel object I don't understand yet.
client.run()


