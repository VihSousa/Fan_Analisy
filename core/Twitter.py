#=================#
# CONEXÃO COM API #
#=================#

import os
import tweepy #  API do Twitter
from dotenv import load_dotenv

load_dotenv()

class TwitterAPI:
    def __init__(self):
        self.client = tweepy.Client(
            bearer_token=os.getenv("API_BEARER"),
            consumer_key=os.getenv("API_KEY"),
            consumer_secret=os.getenv("API_SECRET")
        )
    
    def get_tweets(self, query="#GoFURIA lang:pt -is:retweet", max_results=50):
        try:
            response = self.client.search_recent_tweets(
                query=query,
                max_results=max_results,
                tweet_fields=["created_at", "public_metrics"]
            )
            return response.data or []
        except tweepy.Unauthorized:
            print("Erro: Chaves da API inválidas. Verifique seu .env")
            return []
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return []