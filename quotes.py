import requests
import json 
import tweepy as tw
import time
consumer_key= 'yourkeyhere'
consumer_secret= 'yourkeyhere'
access_token= 'yourkeyhere'
access_token_secret= 'yourkeyhere'
while True:
    response = requests.get("https://api.quotable.io/random?tags=technology&maxLength=125").text
    value = json.loads(response)
    tweet_data = "Quote for You !\n"+str(value["content"]) +"\n- "+str(value["author"])+"\n#technology #quotes #motivation #inspiration #startup #entrepreneur #developer #techie #engineer\n Follow @Imsundar_b"    
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    api.update_status(tweet_data)
    time.sleep(60 * 60 * 24)
    print(tweet_data)