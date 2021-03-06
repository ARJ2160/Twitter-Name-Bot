#Twitter Bot Program
#Section 1 : A function declaraing the authentication
#Section 2 : Code for changing Name of account
                         #Section 1
import tweepy 
import os
import time
def create_api():
  consumer_key = os.getenv('consumer_key')
  consumer_secret = os.getenv('consumer_secret')
  access_token = os.getenv('access_token')
  access_token_secret = os.getenv('access_token_secret')
  
  #Authorization of Keys
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print("API Created")
  return api
                            #Section 2
#Declare Number Emojis
#Split followers count  
#Followers will be displayed in emojis
def follower_count(user):
  emoji_numbers = {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                        4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"} 
  uf_split = [int(i) for i in str(user.followers_count)]
  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()])
  return emoji_followers

api = create_api()

while True:
   user = api.get_user('arjrocks2001')
   api.update_profile(name =f'ARJ|{follower_count(user)} Followers' )#Profile is Updating
   print(f'Updating Twitter Name : ARJ|{follower_count(user)} Followers') #For our Understanding
   print('Waiting for Refresh')
   time.sleep(60)
