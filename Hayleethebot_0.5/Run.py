'''Copyright (C) 2016 Hayleethegamer 

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.'''
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
