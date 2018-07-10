
# coding: utf-8

# In[27]:


import tweepy
import json

consumer_key="eN1MwDQ3IS9aHS2nl5eN9FhlQ"
consumer_secret="5TtkJHVmZthp7mu5kVrtKJNwd9UrN0YQ8rpAl18rXj7S2eSmiF"
access_token="4535201292-76uCkz5CzRtmccCsRYLb6JD9ODOMLlMzCDa9hsr"
access_token_secret="E57aEOipKVgmw0pPdT1yZ94o1TnckOK61k41RoX4Vb0zH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

rest = tweepy.API(auth) # instance of rest api

    
class StdOutListener(tweepy.streaming.StreamListener):
    # A listener handles tweets that are received from the stream.
    #This listener collects N tweets, storing them in memory, and then stops.
    def __init__(self,N):
        super(StdOutListener,self).__init__(self)
        self.data = []
        self.N = N
    def on_data(self, data):
        self.data.append(json.loads(data))
        if len(self.data) >= self.N:
            return False
        else:
            return True

    def on_error(self, status):
        print(status)
        
def getNtweets(N, auth, track = [], locations = []):
    listener = StdOutListener(N)
    stream = tweepy.Stream(auth, listener)
    if len(track) and len(locations):
        stream.filter(track=track, locations = locations)
    elif len(track):
        stream.filter(track = track)
    elif len(locations):
        stream.filter(locations = locations)

    return listener.data
dataScienceTweets = getNtweets(10, auth, track=['data', 'science'])
#for tweet in dataScienceTweets:
    #print(tweet['text'])
    
bbox = [-180.00, -90, 180.00, 90]
globalTweets = getNtweets(100, auth, locations=bbox)

globalTweets[0].keys()

for tweet in globalTweets:
    print(tweet['place']['full_name'])
    print(tweet['text'])
    print("")

