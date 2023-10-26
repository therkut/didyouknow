import requests
import os
import time
import datetime
from requests_oauthlib import OAuth1Session
from bs4 import BeautifulSoup
from html import unescape

consumer_key = "L6H7isVGFUsSakFU73aeqjrTc"
consumer_secret = "mPlGmndoJZ9Kn8ESuBAwktARByuqC4XNz7Q2xryAcLGQt7O9bK"
access_token = "1717148000491835392-Exl11W9MQUIHJmbfIwasjcacAB78QP"
access_token_secret = "ihVSNeocauOway7s2xV26GLYckheYi6uEyeDYOMp6L9Or"
bearer_token = "AAAAAAAAAAAAAAAAAAAAANnRqgEAAAAA8QUUvKmEE%2FfEFAqhFf2MTdcoNl8%3DniwcwC5B0idiIxvYfR1qBtxU5vUDsSBhVmE2k5HhU8HvMgs8j2"

bugun = datetime.date.today()
aylar = ["", "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
bu_ay = aylar[bugun.month]
bu_gun = bugun.day
hashtag = f"{{{bu_gun} {bu_ay}}} > #Bugün #Tarih #Spor #Sanat"

def strip_tags(html):
    return unescape(BeautifulSoup(html, 'html.parser').text)

def tweekibot():
    try:
        wiki = requests.get('https://tr.wikipedia.org/wiki/Anasayfa')
        wiki_page = wiki.text
        soup = BeautifulSoup(wiki_page, 'html.parser')

        # td etiketi içeriğini bul
        td_tag = soup.find('td', {'id': 'mp-bm'})

        # td etiketi içindeki ul etiketini bul
        ul_tag = td_tag.find('ul')

        # ul etiketi içindeki tüm li etiketlerini bul
        li_tags = ul_tag.find_all('li')

        # Liste öğelerini tersine çevir
        li_tags.reverse()

        tweet_list = []

        for counter, li in enumerate(li_tags):
            if counter == 5:
                break
            tweet = strip_tags(li.get_text())
            tweet_list.append(tweet)

        return tweet_list

    except Exception as e:
        print("Wikipedia'dan veri çekerken hata oluştu:", e)
        return []

oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

tweet_list = tweekibot()
tweet = "\n".join(tweet_list)  # Tweet listesini tek bir dizede birleştir

for tweet in tweet_list:
    payload = {"text": f"{tweet}\n\n{hashtag}"}

    print("Payload: %s" % payload)

    response = oauth.post("https://api.twitter.com/2/tweets", json=payload)
    
    if response.status_code != 200:
        print("İstek hata döndürdü: {} {}".format(response.status_code, response.text))
    else:
        print("Tweet başarıyla gönderildi")

    time.sleep(20)  # 20 saniyelik aralık
