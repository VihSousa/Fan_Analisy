import os
import tweepy
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()

class TwitterAPI:
    def __init__(self):
        self.client = self._authenticate()
    
    def _authenticate(self): # Autentica na API do Twitter

        try:
            return tweepy.Client(
                bearer_token=os.getenv("BEARER_TOKEN"),
                consumer_key=os.getenv("API_KEY"),
                consumer_secret=os.getenv("API_SECRET"),
                wait_on_rate_limit=True
            )
        except Exception as e:
            print(f"Erro na autenticação: {e}")
            return None
    
    def _normalize_tweet(self, tweet):  #Tweets tenham a mesma estrutura
        if hasattr(tweet, 'text'):
            return {
                'text': tweet.text,
                'likes': tweet.public_metrics.like_count,
                'retweets': tweet.public_metrics.retweet_count,
                'user': {'screen_name': tweet.user.screen_name},
                'created_at': tweet.created_at.isoformat()
            }
        else:  # Tweet de fallback
            return {
                'text': tweet.get('text', ''),
                'likes': tweet.get('likes', 0),
                'retweets': tweet.get('retweets', 0),
                'user': {'screen_name': tweet.get('user', {}).get('screen_name', 'unknown')},
                'created_at': tweet.get('created_at', '')
            }
    
    def get_tweets(self, query="", max_results=50):
        try:
            response = self.client.search_recent_tweets(
                query=query,
                max_results=max_results,
                tweet_fields=["created_at", "public_metrics"],
                user_fields=["username"]
            )
            
            if not response or not response.data:
                return self._get_fallback_tweets()
                
            return [self._normalize_tweet(tweet) for tweet in response.data]
            
        except Exception as e:
            print(f"Erro na API: {e}")
            return self._get_fallback_tweets()
        
    
    def _format_tweet(self, tweet, users_map: Dict) -> Dict:    #Formata um tweet para estrutura consistente
        return {
            "text": tweet.text,
            "created_at": tweet.created_at.isoformat(),
            "likes": tweet.public_metrics['like_count'],
            "user": {"screen_name": users_map[tweet.author_id]},
            "retweets": tweet.public_metrics['retweet_count']
        }
    
# ================= DADOS DE FALLBACK ================= #
    
    def _get_fallback_tweets(self) -> List[Dict]:
        return [
            {
                "text": "FURIA venceu na ESL Pro League! #GoFURIA",
                "created_at": "2023-05-01T10:00:00Z",
                "likes": 215,
                "user": {"screen_name": "furia_news"},
                "retweets": 42
            },
            
            {
                "text": "FURIA venceu! KSCERATO monstro! #GoFURIA",
                "created_at": "2023-05-01T10:05:00Z",
                "likes": 150,
                "user": {"screen_name": "furia_fan"},
                "retweets": 25
            },
            
            {
                "text": "FURIA venceu! KSCERATO monstro! #GoFURIA",
                "created_at": "2023-05-01T10:00:00Z",
                "likes": 150,
                "retweets": 25,
                "user": {"screen_name": "furia_fan"}
            },
            
            {
                "text": "Que jogo incrível da FURIA no major!",
                "created_at": "2023-05-01T10:05:00Z",
                "likes": 200,
                "retweets": 42,
                "user": {"screen_name": "furia_fan"}
            },
            
            {
                "text": "arT está fazendo uma partida sensacional hoje!",
                "created_at": "2023-05-01T10:10:00Z",
                "likes": 120,
                "retweets": 18,
                "user": {"screen_name": "furia_fan"}
            },
            
            {
                "text": "yuurih mostrando porque é um dos melhores jogadores do Brasil! #GoFURIA",
                "created_at": "2023-05-01T10:15:00Z",
                "likes": 180,
                "retweets": 35,
                "user": {"screen_name": "furia_fan"}
            },
            
            {
                "text": "drop com clutch incrível na última rodada! Esse time é demais!",
                "created_at": "2023-05-01T10:20:00Z",
                "likes": 165,
                "retweets": 28,
                "user": {"screen_name": "furia_fan"}
            },
            
            {
                "text": "FURIA classificada para as semifinais! Vamos com tudo!",
                "created_at": "2023-05-01T10:25:00Z",
                "likes": 250,
                "retweets": 50,
                "user": {"screen_name": "furia_fan"}
            }
        ]
        
# ================= MELHOR LEITURA DOS DADOS ================= #
        
    def get_formatted_tweets(self, max_chars=280):
        tweets = self.get_tweets()  # Reaproveita a lógica existente
        return [
            {
                "preview": f"{tweet['text'][:max_chars]}...",
                "author": f"@{tweet['user']['screen_name']}",
                "engagement": f"♥️ {tweet['likes']} | 🔄 {tweet['retweets']}",
                "date": tweet["created_at"][:10],
                "full_text": tweet["text"]  # Mantém o texto completo
            }
            for tweet in tweets
        ]
        
# =================================== TESTE =================================== #
        
if __name__ == "__main__":
    print("=== TESTE DO TWITTER API ===")
    api = TwitterAPI()
    
    # Teste com dados reais (se credenciais estiverem no .env)
    print("\n🔍 Tentando buscar tweets reais...")
    real_tweets = api.get_tweets()
    print(f"→ {len(real_tweets)} tweets encontrados")
    print(f"→ Exemplo: {real_tweets[0]['text'][:50]}...")
    
    # Teste com fallback
    print("\n🔄 Usando dados de fallback...")
    fallback_tweets = api._get_fallback_tweets()
    print(f"→ {len(fallback_tweets)} tweets de exemplo")
    print(f"→ Primeiro tweet: {fallback_tweets[0]['text']}")