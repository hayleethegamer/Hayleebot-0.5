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
import socket
import string
from Settings import HOST, PORT, PASS, IDENT, CHANNEL
from Read import getUser, getMessage, getTime

usedChannel = ""
def openSocket():
	s = socket.socket()
	s.connect((HOST, PORT))
	sendPass = "PASS " + PASS + "\r\n"
	s.send(sendPass.encode('utf-8'))
	sendNick = "NICK " + IDENT + "\r\n"
	s.send(sendNick.encode('utf-8'))
	sendJoin = "JOIN #" + CHANNEL + "\r\n"
	s.send(sendJoin.encode('utf-8'))
	return s
	
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	messageSend = messageTemp + "\r\n"
	s.send(messageSend.encode('utf-8'))
	print(getTime() + " Hayleethebot: " + messageTemp)
