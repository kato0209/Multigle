from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.top, name='top'),
    #path('twitter/', views.search_on_twitter, name='twitter'),
    path('categorize-search-query/', views.categorize_search_query, name='CategorizeQuery'),
    path('google/', views.search_on_google, name='google'),
    path('qiita/', views.search_on_qiita, name='qiita'),
    re_path(r'^qiita/(?P<keyword>\w+)/?$', views.search_on_qiita, name='qiita'),
    path('youtube/', views.search_on_youtube, name='youtube'),
    re_path(r'^youtube/(?P<keyword>\w+)/?$', views.search_on_youtube, name='youtube'),
    path('instagram/', views.search_on_instagram, name='instagram'),
    re_path(r'^instagram/(?P<keyword>\w+)/?$', views.search_on_instagram, name='instagram'),
    path('hotpepper/', views.search_on_hotpepper, name='hotpepper'),
    re_path(r'^hotpepper/(?P<keyword>\w+)/?$', views.search_on_hotpepper, name='hotpepper'),
    path('rakuten-travel/', views.search_on_rakuten_travel, name='RakutenTravel'),
    re_path(r'^rakuten-travel/(?P<keyword>\w+)/?$', views.search_on_rakuten_travel, name='RakutenTravel'),
    path('rakuten-market/', views.search_on_rakuten_market, name='RakutenMarket'),
    re_path(r'^rakuten-market/(?P<keyword>\w+)/?$', views.search_on_rakuten_market, name='RakutenMarket'),
    path('sports-news/', views.search_on_newsapi, name='newsApi'),
    re_path(r'^sports-news/(?P<keyword>\w+)/?$', views.search_on_newsapi, name='newsApi'),
]