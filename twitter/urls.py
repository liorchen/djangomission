from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^getTweets$', views.get_tweets),
    url(r'^postTweet$', views.post_tweet),
    url(r'^postLike$', views.post_like),
    url(r'^postRetweet$', views.post_retweet),
    url(r'^getRetweets', views.get_retweets),
]