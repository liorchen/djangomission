import datetime
from django.db import models
from twitter import configuration
from twitter.models.Tweet import Tweet


class Like(models.Model):
    """
    This class represent as a single like on a tweet.
    """
    id = models.AutoField(auto_created=True, primary_key=True, unique=True)
    related_tweet = models.ForeignKey(Tweet)
    timestamp = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=configuration.CHAR_FIELD_MAX_LENGTH)