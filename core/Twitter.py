#=================#
# CONEXÃO COM API #
#=================#

import os
import tweepy #  API do Twitter
from dotenv import load_dotenv
import time

load_dotenv()

class TwitterAPI:
    def __init__(self):
        self.client = tweepy.Client(
            bearer_token=os.getenv("API_BEARER"),
            consumer_key=os.getenv("API_KEY"),
            consumer_secret=os.getenv("API_SECRET")
        )
    
    # =================== Método Funcional =================== #
    
    """def get_tweets(self, query="#GoFURIA lang:pt -is:retweet", max_results=50):
        time.sleep(2) 
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
            return []"""
            
            
    # =================== Método de Testes =================== #
    def get_tweets(self, query="", max_results=50):
        time.sleep(2) 
        fake_tweets = [
            type('Tweet', (), {
                'text': 'FURIA venceu! KSCERATO monstro! #GoFURIA', 
                'public_metrics': {'like_count': 150},
                'created_at': "2023-05-01"
            }),
            type('Tweet', (), {
                'text': 'Que jogo incrível da FURIA no major!', 
                'public_metrics': {'like_count': 200},
                'created_at': "2023-05-01"
            })
        ]
        return fake_tweets