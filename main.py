import os
import time
import requests
from bs4 import BeautifulSoup
from html import unescape
from requests_oauthlib import OAuth1Session

# Constants
WIKIPEDIA_URL = 'https://tr.wikipedia.org/wiki/Anasayfa' 
TWITTER_API_URL = 'https://api.twitter.com/2/tweets'
WAIT_INTERVAL = 40  # 40-second interval
TD_ELEMENT_ID = 'mp-bm'  # ID of the td element

# Authenticate with Twitter API
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


oauth = OAuth1Session(consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)

# Hastag
hashtag = f"#Bugün #Tarih #Güncel #Bilgi #TarihteBugün"

# Function to strip HTML tags from text
def strip_tags(html):
    return unescape(BeautifulSoup(html, 'html.parser').text)

# Function to fetch Wikipedia data
def get_wikipedia_data():
    try:
        response = requests.get(WIKIPEDIA_URL)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        td_tag = soup.find('td', {'id': TD_ELEMENT_ID})
        li_tags = td_tag.find_all('li')
        tweet_list = [strip_tags(li.get_text()) for li in li_tags[:5]]
        return tweet_list
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching data from Wikipedia: %s", str(e))
        return []

# Function to post a tweet
def post_tweet(tweet_text, oauth):
    try:
        payload = {"text": tweet_text}
        response = oauth.post(TWITTER_API_URL, json=payload)
        response.raise_for_status()
        print("Tweet sent successfully: %s", tweet_text)
    except Exception as e:
        print("Request returned an error: {} {}".format(response.status_code, response.text))

# Main function
def main():
    # Get Wikipedia data and post tweets
    tweet_list = get_wikipedia_data()
    for tweet in tweet_list:
        tweet_text = f"{tweet}\n\n{hashtag}"
        post_tweet(tweet_text, oauth)
        time.sleep(WAIT_INTERVAL)

if __name__ == '__main__':
    main()
