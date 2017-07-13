# djangomission

This is a django example with an example of type twitter.

This is the api:

GET:
Return all Tweets with additional data.
/twitter/getTweets
[
 {
   "id": [INT],
   "content": [STRING],
   "username: [STRING],
   "timestamp": [ISO_FORMATED_STRING],
   "likes_count: [INT]
    "retweets_count": [INT]
 }
]

POST
Create a new tweet.
Return a the new tweet object.
/twitter/postTweet
{
 "content": [STRING],
  "username: [STRING]
}

POST
Create a like of a spsific id by parameter and send the user name that perform the like opration.
Return a the new like object.
This 
/twitter/postLike?tweet_id=
{
  "username": [STRING]
}

POST
Create a retweet of a spsific id by parameter and send the user name that perform the like opration.
Return a the new retweet object.
/twitter/post_retweet?tweet_id=
{
  "username": [STRING]
}

GET
Return all retweets with additional data.
/tweets/getRetweets
[
 {
 "content",[STRING]
 "retweet_user": [STRING]
  "tweet_id": [INT]
  "tweet_user": [STRING]
  "timestamp": [ISO_FORMATED_STRING]
}
