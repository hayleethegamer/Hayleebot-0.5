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
