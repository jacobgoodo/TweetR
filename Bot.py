#
# **THE WEBSCRAPING PART OF CODE IS BY WILL BISHOP!**
#
# Copyright (2016) Will Bishop
# If you distribute this code, please leave this notice at the top, thanks :d
#

import random #random strings..
import auth #for logging in to Twitter
import time #for sleep
import requests #imports networking and parsing module
from bs4 import BeautifulSoup
from time import sleep # Again, for sleep

t = auth.login() #In order to log into Twitter.
ok = True #Just for loop start

while True: #Infinite loop
	try: #Try the following code, if fails goto except
		r = requests.get("http://chadsoft.co.uk/online-status/status.txt") #Found this is better than http://chadsoft.co.uk/online-status/ (same data)
		soup = BeautifulSoup(r.text, 'html.parser')



		status = soup.find('table', {'class': 'ctww-status'}) #main table
		final = {"status": soup.find('div', {'class': 'clear-before _1c1'}).find('h1').text} #Defines a dictionary and gives it a key of "status", final["status"] is equal to "CTWW STATUS: 7 players across 2 rooms."
		for i in status.findAll('tr'): #Finds each row in table
			content = []
			for x in i.findAll('td'): #each td row contains some data
				content.append(x.text)
 
			if len(content) > 0:
				final[content[0]] = {"room": content[0], "players": content[1], "hostvr": content[2], "uptime": content[3], "joinable": content[4], "participants": content[5]} #nice dictionary
#
# Begin Jacob's code
# 
		
			tweet = "%s (%d)" % (final["status"],random.randint(1,9999)) # prints status and random number to prevent twitter deletion
		if ok == True: #making sure ok is true		
			t.update_status(tweet) #Posts the tweet, using t.
		
		sleep(180) #Sleep for 3mins
		
	except:
		pass #If fails, just ignore and keep going.
	

#print(final) #displays everything
#To access any of the data, use
#print(final["Room 2"]["players"])
#This would return something like "5 players"