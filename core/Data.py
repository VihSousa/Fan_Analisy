#========================#
# Processamento de Dados #
#========================#

import pandas as pd # Organiza em tabelas
from collections import Counter

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
    def top_words(tweets, n=5, exclude=None):
        """Retorna as n palavras mais comuns."""
        exclude = exclude or []
        all_words = " ".join(t.text for t in tweets).split()
        filtered = [w for w in all_words if w.lower() not in exclude]
        return Counter(filtered).most_common(n)
