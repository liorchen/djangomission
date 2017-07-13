import datetime
from django.db import models
from twitter import configuration


class Tweet(models.Model):
    """
    This class represent as a single tweet.
    """
    username = models.CharField(max_length=configuration.CHAR_FIELD_MAX_LENGTH, auto_created=True)
    text_content = models.CharField(max_length=configuration.CHAR_FIELD_MAX_LENGTH, auto_created=True)
    timestamp = models.DateTimeField(auto_now=True)
    tweet_id = models.AutoField(auto_created=True, primary_key=True, unique=True)

    def __init__(self, id, text_content, username, timestamp=datetime.datetime.now(), *args, **kwargs):
        """
        Initialize a new instance of tweet class
        :param id: The id of the tweet. (should be provided by the framework).
        :param username: The publisher user name.
        :param text_content: The content of tweet.
        :param timestamp: The publish time of the tweet.
        """
        super(Tweet, self).__init__(*args, **kwargs)
        self.tweet_id = id
        self.username = username
        self.text_content = text_content
        self.timestamp = timestamp
