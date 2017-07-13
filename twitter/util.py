from django.http import HttpResponse

from twitter import configuration
from twitter.models.Tweet import Tweet


def date_handler(obj):
    """
    Formatting obj to iso format
    :return:obj in iso format
    :param obj:obj
    :return:obj in iso format
    """
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError


def _get_username_and_tweetid(request):
    return request.POST["username"], request.GET["tweetid"]


def _get_username_content(request):
    return request.POST["username"], request.POST["content"]


def _get_related_tweet(tweet_id):
    related_tweet = Tweet.objects.filter(tweet_id=tweet_id).first()
    if not related_tweet:
        return HttpResponse(configuration.INVALID_TWEET_ID_ERROR)
