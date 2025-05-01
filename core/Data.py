#========================#
# Processamento de Dados #
#========================#

import pandas as pd # Organiza em tabelas
from nltk.corpus import stopwords
from collections import Counter
import random


class DataProcessor:
    @staticmethod
    def tweets_to_df(tweets):
        """Converte lista de tweets para DataFrame."""
        return pd.DataFrame([{
            "text": tweet.text,
            "created_at": tweet.created_at,
            "likes": tweet.public_metrics["like_count"]
        } for tweet in tweets])
    
    @staticmethod
    def top_words(tweets, n=10, exclude=None):
        """Retorna palavras filtradas (sem stopwords, hashtags ou menções)."""
        exclude = exclude or []
        stopwords_pt = set(stopwords.words("portuguese"))
        
        all_words = [
            word.lower() for tweet in tweets 
            for word in tweet.text.split() 
            if (word.lower() not in stopwords_pt and 
                word.lower() not in exclude and 
                len(word) > 2 and 
                not word.startswith(("#", "@")))
        ]
        
        return Counter(all_words).most_common(n)
    
class FanDataProcessor:
    def __init__(self):
        self.profiles = []
        
    def validate_document(self, doc_file):
        # Implementar validação básica de documento
        return {
            "valid": len(doc_file.getvalue()) > 1000,  # Exemplo simples
            "type": "CPF" if "cpf" in doc_file.name.lower() else "RG"
        }
    
    def analyze_social_media(self, twitter_handle):
        # Implementar análise básica
        return {
            "follows_furia": True,  # Placeholder
            "activity_score": random.randint(1, 100)
        }