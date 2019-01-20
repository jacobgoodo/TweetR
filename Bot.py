#
# Copyright (2019) Jacob Goodridge (Twitter: @jacob_1F308, Elsewhere: @jacobgoodo)
# If you redistribute this code, please leave this notice at the top :3
#

import auth #for logging in to Twitter
import time #for sleep
from time import sleep # sleep

t = auth.login() #In order to log into Twitter.
ok = True #Just for loop start


tweet = input('What would you like to tweet? ')
if ok == True: #making sure ok is true	

	t.update_status(tweet) #Posts the tweet, using t.	
	print(f'Completed! Posted "{tweet}")


  
except:
	pass #If fails, just ignore and keep going.
