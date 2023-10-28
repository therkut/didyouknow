# Twitter Bot

This Python code is used to create a Twitter bot that automatically tweets through a specific account on Twitter. The bot generates tweets using the latest updates from the Turkish Wikipedia's main page and shares these tweets at specified time intervals.

## Objective

This Python code implements an automatic tweet bot that fetches current information from the specified Wikipedia page and posts this information as a series of tweets on Twitter. The tweets are shared with specific hashtags (#Today #Date #Sports #Art) concatenated to them.

## Requirements

To run the code correctly, you need the following Python libraries to be installed:
- requests
- time
- requests_oauthlib
- BeautifulSoup
- html

Additionally, you'll need access to Twitter API keys (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET) to interact with the Twitter API. These keys should be stored as environmental variables.

## Steps

The code follows the following steps:

1. Fetching Wikipedia Data:
   - An HTTP request is made to Wikipedia's Turkish main page (https://tr.wikipedia.org/wiki/Anasayfa), and the page data is retrieved.
   - The page data is processed using the BeautifulSoup library.
   - Content with the 'td' tag and 'mp-bm' attribute is found.
   - The 'ul' tag inside the 'td' tag is found.
   - All 'li' tags inside the 'ul' tag are found and reversed in order.
   - The first 5 'li' elements are taken, and a list called tweet_list is created.

2. Tweet Creation:
   - HTML tags are stripped from each 'li' element using the strip_tags function and added to the tweet_list.
   - The tweet_list elements are concatenated to create a single tweet text.

3. Posting Tweets to Twitter:
   - Access to the Twitter API is provided using OAuth1Session.
   - JSON data to be sent to the Twitter API is created for each tweet.
   - A 30-second waiting period is added after each tweet is posted.

4. Error Handling:
   - In case of any error, an error message is printed, and the process continues.

## Usage

This code is designed to send tweets through a specific Twitter account. The user should assign Twitter API keys to environmental variables. Additionally, this bot needs to be run at regular intervals.

## Notes

- This code can be customized to fetch data from a specific Wikipedia page and post tweets on Twitter. You can change the relevant Wikipedia page and tweet content.

- Refer to the [Twitter API documentation](https://developer.twitter.com/en/docs) for using the Twitter API.

- This code provides a basic framework for any customization or further development.

We hope this README helps you better understand the operation of the Python code that serves a specific purpose.
