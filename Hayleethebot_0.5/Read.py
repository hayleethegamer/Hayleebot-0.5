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
import datetime

def getUser(line):
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user
def getMessage(line):
	separate = line.split(":", 2)
	message = separate[2]
	return message
def getTags(line):
	split = line.split(" :",2)
	tags = split[0]
	tags = tags.split(";")
	return tags
def getTime():
	now = datetime.datetime.now()
	hour = str(now.hour)
	minute = str(now.minute)
	second = str(now.second)
	year = str(now.year)
	month = str(now.month)
	day = str(now.day)
	result = (month + " " + day + " " + year + ", " + hour + ":" + minute + ":" + second)
	return result
