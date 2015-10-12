# HammerControl.py

import discord
import sqlite3 as sql
import sys
import json

with open("config.json") as json_file:
    json_data = json.load(json_file)
    
client = discord.Client()
client.login(json_data['HammerBot']['discord']['user'], json_data['HammerBot']['discord']['password']) 

gAdmins = json_data['HammerBot']['admins']  #list
gDebug = '1'  #set to blank for no debug. This will be moved to a commandline switch at some point. FUTURE TODD, DO THIS!
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
	elif message.author.name == ['HammerBot']['botname']:
		return()
	elif message.author.name in gAdmins:
			if message.content.startswith('!Controlexit'):
				client.send_message(message.channel, 'HammerBotControl Stopping')
				if gDebug:
					client.send_message(message.channel, 'DEBUG-ACCEPT: Author ID: %s' % message.author.name)
					print('Message Author ID:', message.author.name)
					print('Originating Channel:', message.channel.name)
				sys.exit(0)
	else:
		client.send_message(message.channel, 'in else statement')
		client.send_message(message.channel, "Sorry %s you do not have permission to run the command: " + message.content % message.author.name)
		return()
	
@client.event
def on_ready():
	print("Logged in as: " + client.user.name)
	print('------')
	print('Discord Admins:')
	for i in gAdmins:
		print("     " + i)
	print('------')
	channel = client.get_channel(json_data['HammerBot']['admin_channel_ID'])
	try:
		client.send_message(channel, "HammerBot Control ONLINE!")
	except:
		print "Unable to send message"
client.run()