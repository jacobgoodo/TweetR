from time import sleep as s #importing sleep from the time module as s
print('Hey there!')#Print statement to display text
s(1) # Pausing for 1 second
print('We need to create a file called \'auth.py\' that will contain all of your Twitter credentials (and a bit extra)') #More print statements, this time using a \ before a ' so that it won't end the string
C_KEY = input('Please enter your Comsumer Key (API Key):\n') #Defining Comsumer Key
C_SECRET = input('Please enter your Consumer Secret (API Secret):\n') #Defining Comsumer Secret
A_TOKEN = input ('Please enter your Access Token:\n') #Defining Defining Access Token
A_SECRET = input('Please enter your Access Token Secret:\n')#Defining Access Secret Key
#My code is a bit messy I know
with open('auth.py', 'w') as f: #Opening the auth.py file (which does not exist until the line) as 'f'
	f.write('import tweepy') #Writing to the file, continues for the next couple of lines.
	f.write('\ndef login():') #The '\n' enters a new line
	f.write('\n    CONSUMER_KEY = ' + "'" + C_KEY + "'")
	f.write('\n    CONSUMER_SECRET = ' + "'" + C_SECRET + "'")
	f.write('\n    ACCESS_KEY = ' + "'" + A_TOKEN + "'")
	f.write('\n    ACCESS_SECRET = ' + "'" + A_SECRET + "'")
	f.write('\n    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)')
	f.write('\n    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)')
	f.write('\n    api = tweepy.API(auth)')
	f.write('\n    return api') #A very important line, this means that when this function is called (which it is from the bot.py file with t = auth.login()) it returns 'api', the api function is used to post tweets, but we define it as t, so instead of api.update_status(), we can use t.update_status(), it also makes it easier to login without having to specify your credentials every time
s(2) #Pausing for 2 seconds
print('Should be all setup now, please try running the bot.py file!') #Informing you that is it all done
s(5) #Pausing for 5 seconds