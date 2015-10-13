# HammerControl.py

import discord
import sqlite3 as sql
import sys
import json
import UserCommands

with open("config.json") as json_file:
    json_data = json.load(json_file)
    
client = discord.Client()
client.login(json_data['DiscBot']['discord']['email'], json_data['DiscBot']['discord']['password']) 

gAdmins = json_data['DiscBot']['admins']  #list
gDebug = '1'  #set to blank for no debug. This will be moved to a commandline switch at some point. FUTURE TODD, DO THIS!
con = None

try: 
	con = sql.connect('discwords')
	cur = con.cursor()
	cur.execute("SELECT * FROM links")
	rows = cur.fetchall()
except sql.Error, e:
	print "Error %s:" % e.args[0]
	sys.exit(1)

def fire_all(func_list):
    for f in func_list:
        f()

@client.event
def on_message(message):
	userCommands = {'!hello': UserCommands.hello, '!bye': UserCommands.bye}
	adminCommands = {}
#	if message.author.name == json_data['DiscBot']['discord']['username']:
#		return()
#	userCommands['!hello']()
	print "in message event"
	for key in userCommands:  #seems like there is a lot of looping here
		print key, 'corresponds to', userCommands[key]
		if message.content.startswith(key):
			print "inside if"
			userCommands[key](message)
@client.event
def on_ready():
	print("Logged in as: " + client.user.name)
	print('------')
	print('Discord Admins:')
	for i in gAdmins:
		print("     " + i)
	print('------')
	channel = client.get_channel(json_data['DiscBot']['admin_channel_ID'])
#	try:
#		client.send_message(channel, "Bot Control ONLINE!")
#	except:
#		print "Unable to send message"
client.run()