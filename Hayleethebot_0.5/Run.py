import string
import time
from Read import getUser, getMessage, getTime
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Chat_Commands import chatCommands, fileRead
from sys import argv
import sys
#import Simple_Commands

s = openSocket()
joinRoom(s)
readbuffer = ""

greeted = []
mods = []
trusted = []
tempWhitelist = []
platform = "twitch"
stopped = 0
errors = 0


while True:

	readbuffer = readbuffer + s.recv(1024).decode()
	#temp = string.split(readbuffer, "\n")
	temp = readbuffer.split("\n")
	readbuffer = temp.pop()
	print("HELLOOOOOOOOOOOOOOOOO")
	for line in temp:
		#print("Debug: " + line)
		if "PING" in line:
			s.send(line.replace("PING", "PONG"))
			print(getTime() + " " + line)
			print(getTime() + " " + line.replace("PING", "PONG"))
			sendMessage(s, "Debug: Ping found and responded too")
			continue
		user = getUser(line)
		message = getMessage(line)
		#await Simple_Commands.simpleCommands(message,s,platform,user)
		chatCommands(readbuffer,s,message,temp,line,user,greeted,trusted,mods,tempWhitelist)