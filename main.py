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

# OAuth authentication with Twitter
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

oauth = OAuth1Session(consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)

# Hashtag
HASHTAG = "#Bugün #Tarih #Güncel #Bilgi #TarihteBugün"

# Function to strip HTML tags from text
def strip_tags(html):
    return unescape(BeautifulSoup(html, 'html.parser').text)

# Function to fetch Wikipedia data
def fetch_wikipedia_data():
    try:
        response = requests.get(WIKIPEDIA_URL)
        response.raise_for_status()
        print("Wikipedia page fetched successfully.")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data from Wikipedia: {e}")
        return None

# Function to process Wikipedia data and extract tweets
def process_wikipedia_data(data):
    if data:
        try:
            soup = BeautifulSoup(data, 'html.parser')
            td_tag = soup.find('td', {'id': TD_ELEMENT_ID})
            li_tags = td_tag.find_all('li')[:5]
            tweet_list = [strip_tags(li.get_text()) for li in li_tags]
            print("Wikipedia data processed successfully.")
            return tweet_list
        except Exception as e:
            print(f"An error occurred while processing Wikipedia data: {e}")
    return []

# Function to post a tweet
def post_tweet(tweet_text, oauth):
    try:
        payload = {"text": f"{tweet_text}\n\n{HASHTAG}"}
        response = oauth.post(TWITTER_API_URL, json=payload)
        response.raise_for_status()
        print(f"Tweet sent successfully: {tweet_text}")
    except Exception as e:
        print(f"Request returned an error: {e}")

# Main function
def main():
    wikipedia_data = fetch_wikipedia_data()
    if wikipedia_data:
        tweet_list = process_wikipedia_data(wikipedia_data)
        for tweet in tweet_list:
            post_tweet(tweet, oauth)  # 'oauth' is defined in the global scope
            time.sleep(WAIT_INTERVAL)

if __name__ == '__main__':
    main()
