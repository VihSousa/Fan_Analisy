import pandas as pd
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

class DataProcessor:
    @staticmethod
    def tweets_to_df(tweets):                       # Converte lista de tweets para DataFrame.

        return pd.DataFrame([{
            "text": tweet.text,
            "created_at": tweet.created_at,
            "likes": tweet.public_metrics.get("like_count", 0),
            "sentiment": None  # Será preenchido depois
        } for tweet in tweets])
    
    @staticmethod
    def top_words(tweets, n=10, exclude=None):         # Retorma palavras filtradas

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

    @staticmethod
    def generate_stats_plot(player_stats):           #Gera gráfico de radar para stats de jogadores.

        stats = {
            'Rating': player_stats.get('rating', 0),
            'Kills': player_stats.get('kills', 0) / 1000,
            'Clutches': player_stats.get('clutches', 0) / 10
        }
        
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
        angles = list(stats.keys())
        values = list(stats.values())
        
        ax.fill(angles, values, color='red', alpha=0.25)
        ax.set_yticklabels([])
        ax.set_title('Performance do Jogador', pad=20)
        
        return fig