import datetime
from django.db import models
from twitter.models.Tweet import Tweet
from twitter import configuration


class Retweet(models.Model):
    """
    This class represent as share tweet object.
    """
    id = models.AutoField(auto_created=True, primary_key=True, unique=True)
    related_tweet = models.ForeignKey(Tweet)
    timestamp = models.DateTimeField()
    username = models.CharField(max_length=configuration.CHAR_FIELD_MAX_LENGTH)
