import tweepy
import re
import random
import time

"""Administrator access keys"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def get_all_tweets(screen_name):
    """Retrieves tweets from twitter timeline"""

    all_tweets = []
    new_tweets =[]
    
    auth= tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
    client = tweepy.API(auth)
    new_tweets = client.user_timeline(screen_name=screen_name, count=200)
    
    while len(new_tweets) >0:
        for tweet in new_tweets:
            all_tweets.append(str(tweet.text.encode("utf-8")))
        print("%s tweets recieved" %(len(all_tweets)))
        max_id = new_tweets[-1].id-1
        new_tweets = client.user_timeline(screen_name=screen_name,count=200,max_id=max_id)
    return all_tweets

def clean_tweets(tweet):
    """Cleans unwanted code in tweets"""
    tweet = re.sub("http\S+","",tweet) #link
    #tweet = re.sub("#\S+","",tweet)    #hashtags
    #tweet = re.sub("\.?@","",tweet)    #at mentions
    tweet = re.sub("RT.+","",tweet)    #retweets
    tweet = re.sub("Video\:","",tweet) #Videos
    tweet = re.sub("\n","",tweet)      #new lines
    tweet = re.sub("^\.\s.","",tweet)  #leading whitespace
    tweet = re.sub("\s+"," ",tweet)    #extra whitespace
    tweet = re.sub("&amp;","&",tweet)  #encoded ampersands
    tweet = re.sub("b'","",tweet)     
    tweet = re.sub('b"' , '',tweet)
    tweet = re.sub('\xF0\S+'," ",tweet)


    tweet = (tweet.

    		replace('\\xe2\\x80\\x99', "'").

            replace('\\xc3\\xa9', 'e').

            replace('\\xe2\\x80\\x90', '-').

            replace('\\xe2\\x80\\x91', '-').

            replace('\\xe2\\x80\\x92', '-').

            replace('\\xe2\\x80\\x93', '-').

            replace('\\xe2\\x80\\x94', '-').

            replace('\\xe2\\x80\\x94', '-').

            replace('\\xe2\\x80\\x98', "'").

            replace('\\xe2\\x80\\x9b', "'").

            replace('\\xe2\\x80\\x9c', '"').

            replace('\\xe2\\x80\\x9c', '"').

            replace('\\xe2\\x80\\x9d', '"').

            replace('\\xe2\\x80\\x9e', '"').

            replace('\\xe2\\x80\\x9f', '"').

            replace('\\xe2\\x80\\xa6', '...').

            replace('\\xe2\\x80\\xb2', "'").

            replace('\\xe2\\x80\\xb3', "'").

            replace('\\xe2\\x80\\xb4', "'").

            replace('\\xe2\\x80\\xb5', "'").

            replace('\\xe2\\x80\\xb6', "'").

            replace('\\xe2\\x80\\xb7', "'").

            replace('\\xe2\\x81\\xba', "+").

            replace('\\xe2\\x81\\xbb', "-").

            replace('\\xe2\\x81\\xbc', "=").

            replace('\\xe2\\x81\\xbd', "(").

            replace('\\xe2\\x81\\xbe', ")")


                 )
    return tweet


finished_tweets1 = []
finished_tweets2 = []
finished_tweets3 = []

for tweet in get_all_tweets("""user"""):
    """Cleans tweet text and appends it to finished_tweets1 list"""
    tweets = clean_tweets(tweet)
    finished_tweets1.append(tweets)


# for tweet in get_all_tweets("""user"""):
#     """Cleans tweet text and appends it to finished_tweets1 list"""
#     tweets = clean_tweets(tweet)
#     finished_tweets1.append(tweets)
                           
# for tweet in get_all_tweets("""user"""):
#     """Cleans tweet text and appends it to finished_tweets1 list"""
#     tweets = clean_tweets(tweet)
#     finished_tweets1.append(tweets)



for tweet in get_all_tweets("""News outlet"""):
    """Cleans tweet text and appends it to finished_tweets2 list"""
    tweets2 = clean_tweets(tweet)
    finished_tweets2.append(tweets2)

for tweet in finished_tweets2:
    """If quotation mark in finished_tweets2 tweet: removes all char after quote"""
    if '"' in tweet:
        finished_tweets3.append(tweet)


random_tweet1 = clean_tweets(random.choice(finished_tweets1))
random_tweet2 = clean_tweets(random.choice(finished_tweets3))

random_tweet2 = random_tweet2.split('"',1)[0]

finalized_tweet = random_tweet2 + '"' + random_tweet1 + '"'


def countdown(t):
    """Calls status update at random time given by the countdown call"""
    while t>0:
        time.sleep(1)
        t -=1
    api.update_status()

        
while True:
    countdown(random.randint("""How often bot tweets (keep in mind Twitters bot guidelines"""))