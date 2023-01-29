import requests
import json
from newsapi import NewsApiClient
from datetime import datetime
from datetime import timezone

def get_search(params, keyword):
    newsapi = NewsApiClient(api_key=params['api_key'])
    news_res = newsapi.get_everything(
        q = keyword,
    )

    articles_params_list = []
    for article in news_res['articles']:
        article_params_dict = {}
        article_params_dict['title'] = article['title']
        article_params_dict['description'] = article['description']
        article_params_dict['url'] = article['url']
        article_params_dict['image_url'] = article['urlToImage']

        published_at = datetime.fromisoformat(article['publishedAt'][:-1]).astimezone(timezone.utc)
        published_at = published_at.strftime('%Y年%m月%d日 %H時%M分')
        article_params_dict['published_at'] = published_at
        
        articles_params_list.append(article_params_dict)

    return articles_params_list

    