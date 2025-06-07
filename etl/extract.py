import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

def extract_tweets(user_id, max_results=50):
    bearer_token = os.getenv("BEARER_TOKEN")
    client = tweepy.Client(bearer_token=bearer_token)

    response = client.get_users_tweets(
        id=user_id,
        max_results=max_results,
        tweet_fields=["created_at", "public_metrics"]
    )

    tweets = []
    if response.data:
        for tweet in response.data:
            tweets.append({
                "text": tweet.text,
                "id": tweet.id,
                "created_at": tweet.created_at
            })
    return tweets
