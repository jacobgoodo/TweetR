#
# Copyright (2019) Jacob https://github.com/jacobgoodo/
# If you redistribute this code, please leave this notice at the top :3
#

import auth #for logging in to Twitter
import time #for sleep
from time import sleep # sleep

t = auth.login() #In order to log into Twitter.


tweet = input('What would you like to tweet? ')
t.update_status(tweet) #Posts the tweet, using t.	
print(f'Completed! Posted "{tweet}"')
