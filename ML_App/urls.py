from django.urls import path

from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('twitter/', views.search_on_twitter, name='twitter'),
    path('qiita/', views.search_on_qiita, name='qiita'),
    path('youtube/', views.search_on_youtube, name='youtube'),
    path('instagram/', views.search_on_instagram, name='instagram'),
    path('hotpepper/', views.search_on_hotpepper, name='hotpepper'),
    path('rakuten-travel/', views.search_on_rakuten_travel, name='RakutenTravel'),
    path('rakuten-market/', views.search_on_rakuten_market, name='RakutenMarket'),
    path('sports-news/', views.search_on_newsapi, name='newsApi'),
]