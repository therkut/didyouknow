import requests
import time
from requests_oauthlib import OAuth1Session
from bs4 import BeautifulSoup
from html import unescape

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

def strip_tags(html):
    return unescape(BeautifulSoup(html, 'html.parser').text)

def tweetBot():
    try:
        wiki = requests.get('https://tr.wikipedia.org/wiki/Anasayfa')
        wiki_page = wiki.text
        soup = BeautifulSoup(wiki_page, 'html.parser')

        # Find the content of the 'td' tag
        td_tag = soup.find('td', {'id': 'mp-bm'})

        # Find the 'ul' tag inside the 'td' tag
        ul_tag = td_tag.find('ul')

        # Find all 'li' tags within the 'ul' tag
        li_tags = ul_tag.find_all('li')

        # Reverse the list elements
        li_tags.reverse()

        tweet_list = []

        for counter, li in enumerate(li_tags):
            if counter == 5:
                break
            tweet = strip_tags(li.get_text())
            tweet_list.append(tweet)

        return tweet_list

    except Exception as e:
        print("An error occurred while fetching data from Wikipedia:", e)
        return []

oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

tweet_list = tweetBot()
tweet = "\n".join(tweet_list)  # Join the tweet list into a single string

for tweet in tweet_list:
    payload = {"text": f"{tweet}\n\n #Bugün #Tarih #Spor #Sanat"}

    print("Payload: %s" % payload)

    response = oauth.post("https://api.twitter.com/2/tweets", json=payload)
    
    if response.status_code != 200:
        print("Request returned an error: {} {}".format(response.status_code, response.text))
    else:
        print("Tweet successfully sent")

    time.sleep(30)  # 30-second interval
