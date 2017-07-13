import json

import datetime
from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view
from twitter import util
from twitter.models.Like import Like
from twitter.models.Retweet import Retweet
from twitter.models.Tweet import Tweet
import configuration


@api_view(['GET'], False)
def get_tweets(request):
    """
    A Get tweet handler.
    :param request: get params, not something spacial.
    :return:All tweets info.
    """

    actual_data = []
    for tweet_obj in Tweet.objects.all():
        json_obj = serializers.serialize(configuration.PYTHON_STRING, [tweet_obj, ])[0]["fields"]
        json_obj["like_counts"] =tweet_obj.like_set.count()
        json_obj["retweet_counts"] =tweet_obj.retweet_set.count()
        actual_data.append(json_obj)

    output = json.dumps(actual_data, default=util.date_handler)
    return HttpResponse(output)


@api_view(['POST'], False)
def post_tweet(request):
    """
    Create a new tweet in the db.
    :param request: Tweet content and username.
    :return: The saved tweet object.
    """
    username, content = util._get_username_content(request)
    tweet_obj = Tweet(None, username=username, text_content=content)
    tweet_obj.save()
    json_to_return = serializers.serialize("json", [tweet_obj])
    return HttpResponse(json_to_return)


@api_view(['POST'], False)
def post_like(request):
    """
    Create a new like in the db.
    :param request: tweets id and username.
    :return: The saved like object.
    """
    user_name, tweet_id = util._get_username_and_tweetid(request)
    related_tweet = Tweet.objects.filter(tweet_id=tweet_id).first()
    if not related_tweet:
        return HttpResponse(configuration.INVALID_TWEET_ID_ERROR)

    like_obj = Like()
    like_obj.related_tweet = related_tweet
    like_obj.username = user_name
    like_obj.save()

    json_to_return = serializers.serialize("json", [like_obj])
    return HttpResponse(json_to_return)


@api_view(['POST'], False)
def post_retweet(request):
    """
    Create a new retweet in the db.
    :param request: tweets id and username.
    :return: The saved retweet object.
    """
    user_name, tweet_id = util._get_username_and_tweetid(request)
    related_tweet = Tweet.objects.filter(tweet_id=tweet_id).first()
    if not related_tweet:
        return HttpResponse(configuration.INVALID_TWEET_ID_ERROR)
    retweet_obj = Retweet()
    retweet_obj.related_tweet = related_tweet
    retweet_obj.username = user_name
    retweet_obj.timestamp = datetime.datetime.now()
    retweet_obj.save()

    json_to_return = serializers.serialize("json", [retweet_obj])
    return HttpResponse(json_to_return)


@api_view(['GET'], False)
def get_retweets(request):
    """
    A Get retweet handler.
    :param request: get params, not something spacial.
    :return:All tweets info.
    """

    actual_data = []

    for retweet_obj in Retweet.objects.all():
        json_obj = serializers.serialize(configuration.PYTHON_STRING, [retweet_obj, ])[0]["fields"]
        json_obj["content"] = retweet_obj.related_tweet.text_content
        json_obj["retweet_user"] = retweet_obj.username
        json_obj["tweet_id"] = retweet_obj.related_tweet.tweet_id
        json_obj["tweet_user"] = retweet_obj.related_tweet.username
        json_obj["timestamp"] = retweet_obj.timestamp
        actual_data.append(json_obj)

    output = json.dumps(actual_data, default=util.date_handler)
    return HttpResponse(output)
