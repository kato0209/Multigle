import json
import datetime
import time
import math
from requests_oauthlib import OAuth1Session


SEARCH_TWEETS_URL = 'https://api.twitter.com/1.1/search/tweets.json'
EMBED_TWEETS_URL = 'https://publish.twitter.com/oembed'
SEARCH_LIMIT_COUNT = 10

class TwitterApi:
    def __init__(self, oauth_session_params):
        
        CONSUMER_KEY    = oauth_session_params['consumer_key']
        CONSUMER_SECRET = oauth_session_params['consumer_secret']
        ACCESS_TOKEN    = oauth_session_params['access_token']
        ACCESS_TOKEN_SECRET   = oauth_session_params['access_token_secret']

        self.twitter    = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.url_search = SEARCH_TWEETS_URL
        self.url_embed  = EMBED_TWEETS_URL
        self.count = SEARCH_LIMIT_COUNT

    def search_tweets(self, keyword):
        params = {'q': keyword, 'count': self.count }
        request = self.twitter.get(self.url_search, params = params)
        if request.status_code == 200:
            search_tweets = json.loads(request.text)
            return search_tweets
        else:
            return None
    
    def get_embed_params(self, search_tweets):
        embed_params_dicts = []
        for tweet in search_tweets['statuses']:
            embed_params_dict = {}
            embed_params_dict['tweet_id'] = str(tweet['id'])
            embed_params_dict['screen_name'] = tweet['user']['screen_name']
            embed_params_dicts.append(embed_params_dict)
        return embed_params_dicts

    
    def get_embed_datas(self, embed_params_dicts):
        embed_datas = []
        for e in embed_params_dicts:
            url = 'https://twitter.com/'+e['screen_name']+'/'+'status/'+e['tweet_id']
            params = {'url': url, 'hide_media': False, 'align': 'center'}
            request = self.twitter.get(self.url_embed, params = params)
            embed_data = json.loads(request.text)
            embed_datas.append(embed_data['html'])
        return embed_datas

    def get_tweets(self, keyword):
        search_tweets = self.search_tweets(keyword)
        embed_params_dicts = self.get_embed_params(search_tweets)
        embed_datas        = self.get_embed_datas(embed_params_dicts)
        
        return embed_datas