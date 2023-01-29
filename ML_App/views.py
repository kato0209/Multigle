from django.shortcuts import render
from django.http import HttpResponse
import os
import environ
from dotenv import load_dotenv
import requests

from . import forms, twitter, qiita, youtube, instagram, hotpepper, rakuten_travel, rakuten_market, newsapi
from ML_Project import settings


""" 
import time                                
from selenium import webdriver              
import chromedriver_binary
"""

load_dotenv()

def top(request):
    return render(request, 'top.html')

def search_on_twitter(request):
    if request.method == 'GET':
        form = forms.SearchForm()
        return render(request, 'twitter.html', {'form' : form })
    elif request.method == 'POST':
        form = forms.SearchForm(request.POST)
        keyword = request.POST['keyword']

        oauth_session_params = {}
        oauth_session_params['consumer_key']    = os.environ['TWITTER_API_KEY']
        oauth_session_params['consumer_secret'] = os.environ['TWITTER_API_SECRET']
        oauth_session_params['access_token']    = os.environ['TWITTER_ACCESS_TOKEN']
        oauth_session_params['access_token_secret']   = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

        try:
            twitterApi = twitter.TwitterApi(oauth_session_params)
            tweets = twitterApi.get_tweets(keyword)

            context = {
                'tweets' : tweets, 
                'keyword' : keyword,
                'form' : form,
            }
            return render(request, 'twitter.html', context)
        except:
            error_message = 'リクエストにエラーが発生しました'
            context = {
                'error_message' : error_message,
                'keyword' : keyword,
                'form' : form,
            }
            return render(request, 'twitter.html', context)

def search_on_qiita(request):
    if request.method == 'GET':
        form = forms.SearchForm()
        return render(request, 'qiita.html', {'form' : form })
    elif request.method == 'POST':
        form = forms.SearchForm(request.POST)
        qiita_url = 'https://qiita.com'
        keyword = request.POST['keyword']
        qiita_access_token = os.environ['QIITA_ACCESS_TOKEN']

        try:
            posts_parameters_list = qiita.get_search(qiita_access_token, keyword)
            context = {
                'posts' : posts_parameters_list,
                'keyword' : keyword,
                'qiita_url' : qiita_url,
                'form' : form,
            }
            return render(request, 'qiita.html', context)
        except:
            error_message = 'リクエストにエラーが発生しました'
            context = {
                'error_message' : error_message,
                'keyword' : keyword,
                'form' : form,
            }
            return render(request, 'qiita.html', context)

def search_on_youtube(request):
    if request.method == 'GET':
        form = forms.SearchForm()
        return render(request, 'youtube.html', {'form' : form })
    elif request.method == 'POST':
        form = forms.SearchForm(request.POST)
        youtube_api_key = os.environ['YOUTUBE_API_KEY']
        youtube_url = 'https://youtube.com'
        keyword = request.POST['keyword']

        try:
            videos_parameters_list = youtube.get_search(youtube_api_key, keyword)
            context = {
                'videos' : videos_parameters_list,
                'keyword' : keyword,
                'youtube_url' : youtube_url,
                'form' : form,
            }
            return render(request, 'youtube.html', context)
        except:
            error_message = 'リクエストにエラーが発生しました'
            context = {
                'error_message' : error_message,
                'keyword' : keyword,
                'form' : form,
            }
            return render(request, 'youtube.html', context)

def search_on_instagram(request):
    if request.method == 'GET':
        form = forms.SearchForm()
        return render(request, 'instagram.html',{'form':form})
    elif request.method == 'POST':
        form = forms.SearchForm(request.POST)
        keyword = request.POST['keyword']
        params = {}
        params['access_token'] = os.environ['INSTAGRAM_ACCESS_TOKEN']
        params['app_id'] = os.environ['INSTAGRAM_APP_ID']
        params['app_secret'] = os.environ['INSTAGRAM_APP_SECRET']
        params['instagram_account_id'] = os.environ['INSTAGRAM_ACCOUNT_ID']
        params['endpoint_url_base'] = 'https://graph.facebook.com/'

        try:
            posts_parameters_list = instagram.get_search(params, keyword)
            posts_length = len(posts_parameters_list)
            context = {
                'posts' : posts_parameters_list,
                'keyword' : keyword,
                'posts_length' : posts_length,
                'form' : form,
            }
            return render(request, 'instagram.html', context)
        except:
            error_message = 'リクエストにエラーが発生しました'
            context = {
                'error_message' : error_message,
                'keyword' : keyword,
                'form' : form,
            }
            return render(request, 'instagram.html', context)

def search_on_hotpepper(request):
    if request.method == 'GET':
        form = forms.SearchForm()
        return render(request, 'hotpepper.html',{'form':form})
    elif request.method == 'POST':
        form = forms.SearchForm(request.POST)
        keyword = request.POST['keyword']
        params = {}
        params['api_key'] = os.environ['HOTPEPPER_API_KEY']
        params['base_url'] = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
        
        try:
            shops_params_list = hotpepper.get_search(params, keyword)
            context = {
                    'shops' : shops_params_list,
                    'keyword' : keyword,
                    'form' : form,
            }
            return render(request, 'hotpepper.html', context)
        except:
            error_message = 'リクエストにエラーが発生しました'
            context = {
                'error_message' : error_message,
                'keyword' : keyword,
                'form' : form,
            }
            return render(request, 'hotpepper.html', context)

def search_on_rakuten_travel(request):
    if request.method == 'GET':
        form = forms.SearchForm()
        return render(request, 'rakuten_travel.html',{'form':form})
    elif request.method == 'POST':
        form = forms.SearchForm(request.POST)
        keyword = request.POST['keyword']
        params = {}
        params['rakuten_application_id'] = os.environ['RAKUTEN_APPLICATION_ID']
        params['base_url'] = 'https://app.rakuten.co.jp/services/api/Travel/KeywordHotelSearch/20170426'
        params['page'] = 1
        params['hits'] = 20
        params['hotel_thumbnail_size'] = 3
        params['response_type'] = 'large'

        try:
            hotels_params_list = rakuten_travel.get_search(params, keyword)
            context = {
                'hotels' : hotels_params_list,
                'keyword' : keyword,
                'form' : form,
            }
            return render(request, 'rakuten_travel.html', context)
        except:
            error_message = 'リクエストにエラーが発生しました'
            context = {
                'error_message' : error_message,
                'keyword' : keyword,
                'form' : form,
            }
            return render(request, 'rakuten_travel.html', context)

def search_on_rakuten_market(request):
    if request.method == 'GET':
        form = forms.SearchForm()
        return render(request, 'rakuten_market.html',{'form':form})
    elif request.method == 'POST':
        form = forms.SearchForm(request.POST)
        keyword = request.POST['keyword']
        params = {}
        params['rakuten_application_id'] = os.environ['RAKUTEN_APPLICATION_ID']
        params['base_url'] = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
        params['page'] = 1
        params['hits'] = 20

        try:
            items_params_list = rakuten_market.get_search(params, keyword)
            context = {
                'items' : items_params_list,
                'keyword' : keyword,
                'form' : form,
            }
            return render(request, 'rakuten_market.html', context)
        except:
            error_message = 'リクエストにエラーが発生しました'
            context = {
                'error_message' : error_message,
                'keyword' : keyword,
                'form' : form,
            }
            return render(request, 'rakuten_market.html', context)

def search_on_newsapi(request):
    if request.method == 'GET':
        form = forms.SearchForm()
        return render(request, 'newsapi.html',{'form':form})
    elif request.method == 'POST':
        form = forms.SearchForm(request.POST)
        keyword = request.POST['keyword']
        params = {}
        params['api_key'] = os.environ['NEWSAPI_API_KEY']
        params['page_size'] = 3

        ariticles_params_list = newsapi.get_search(params, keyword)
        context = {
                'articles' : ariticles_params_list,
                'keyword' : keyword,
                'form' : form,
            }
        return render(request, 'newsapi.html', context)

        """
        try:
            items_params_list = rakuten_market.get_search(params, keyword)
            context = {
                'items' : items_params_list,
                'keyword' : keyword,
                'form' : form,
            }
            return render(request, 'rakuten_market.html', context)
        except:
            error_message = 'リクエストにエラーが発生しました'
            context = {
                'error_message' : error_message,
                'keyword' : keyword,
                'form' : form,
            }
            return render(request, 'newsapi.html', context)
        """