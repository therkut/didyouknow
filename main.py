import os
import time
import requests
from bs4 import BeautifulSoup
from html import unescape
from requests_oauthlib import OAuth1Session

# Constants
WIKI_URL = 'https://tr.wikipedia.org/wiki/Anasayfa'
TWEET_URL = 'https://api.twitter.com/2/tweets'
TWEET_INTERVAL = 30  # 30-second interval
TD_TAG_ID = 'mp-bm'  # ID for the desired 'td' tag

# OAuth configuration
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

oauth = OAuth1Session(consumer_key, client_secret=consumer_secret,
                      resource_owner_key=access_token, resource_owner_secret=access_token_secret)

def fetch_and_format_tweets():
    try:
        wiki = requests.get(WIKI_URL)
        wiki_page = wiki.text
        soup = BeautifulSoup(wiki_page, 'html.parser')
        td_tag = soup.find('td', {'id': TD_TAG_ID})
        ul_tag = td_tag.find('ul')
        li_tags = ul_tag.find_all('li')[:5]  # Only first 5 items
        tweet_list = [unescape(BeautifulSoup(li.get_text(), 'html.parser').text) for li in li_tags]
        return tweet_list
    except requests.RequestException as e:
        print(f"An error occurred while fetching data from Wikipedia: {e}")
        return []

def post_tweets(tweets):
    for tweet in tweets:
        payload = {"text": f"{tweet}\n\n #Bugün #Tarih #Spor #Sanat"}
        print("Payload: %s" % payload)
        response = oauth.post(TWEET_URL, json=payload)
        if response.status_code != 200:
            print(f"Request returned an error: {response.status_code} {response.text}")
        else:
            print("Tweet successfully sent")

if __name__ == "__main__":
    tweet_list = fetch_and_format_tweets()
    post_tweets(tweet_list)
    time.sleep(TWEET_INTERVAL)
