# HammerControl.py

import discord
import sqlite3 as sql
import sys
import json
import UserCommands, AdminCommands

with open("config.json") as json_file:
    json_data = json.load(json_file)

try:
	client = discord.Client()
	client.login(json_data['DiscBot']['discord']['email'], json_data['DiscBot']['discord']['password']) 
except:
	print "Unable to login"

gAdmins = json_data['DiscBot']['admins']  #list
gDebug = '1'  #set to blank for no debug. This will be moved to a commandline switch at some point. FUTURE TODD, DO THIS!
con = None

try: 
	con = sql.connect('discwords')
	cur = con.cursor()
	
	
except sql.Error, e:
	print "Error %s:" % e.args[0]
	sys.exit(1)

@client.event
def on_message(message):
	cur.execute("SELECT * FROM links")
	rows = cur.fetchall()
	if message.author.name == json_data['DiscBot']['discord']['username']:
		return()
	if message.content.startswith("!"):
		for key in UserCommands.userCommands:  #seems like there is a lot of looping here
			if message.content.startswith(key):
				UserCommands.userCommands[key](client, message)
		for key in AdminCommands.adminStrings:  #seems like there is a lot of looping here
			for admin in gAdmins:
				if message.author.name == admin:
					if message.content.startswith(key):
						AdminCommands.adminStrings[key](client, message)
	for row in rows:
			word = row[0]
			#print("Inside for statement for word scanning: " + word)
			if word in message.content:
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
	channel = client.get_channel(json_data['DiscBot']['admin_channel_ID'])
	try:
		client.send_message(channel, "Bot Control ONLINE!")
	except:
		print "Unable to send message"
client.run()