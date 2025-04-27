import streamlit as st # Dashboard web interativo
from core.Twitter import TwitterAPI
from core.Sentiment import SentimentAnalyzer 
from core.Data import DataProcessor
from wordcloud import WordCloud # Nuvem de palavras
import matplotlib.pyplot as plt


# Configuração inicial
twitter = TwitterAPI()
analyzer = SentimentAnalyzer()
processor = DataProcessor()

st.title("FURIAFALA") # Criar um título melhor"

if st.button("Buscar Tweets"):
    tweets = twitter.get_tweets()
    
    if not tweets:
        st.error("Nenhum tweet encontrado ou erro na API!")
    else:
        # === Métricas === #
        st.subheader(" Métricas")
        df = processor.tweets_to_df(tweets)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Tweets Coletados", len(df))
        with col2:
            positive = sum(analyzer.analyze(t.text)["polarity"] > 0 for t in tweets)
            st.metric("Tweets Positivos", f"{positive}/{len(df)}")
        with col3:
            st.metric("Palavras Únicas", len(set(" ".join(df["text"]).split())))

        # === Tweets Destacados === #
        st.subheader("Top Tweets")
        for tweet in sorted(tweets, key=lambda x: x.public_metrics["like_count"], reverse=True)[:3]:
            sentiment = analyzer.analyze(tweet.text)
            emoji = "🔥" if sentiment["polarity"] > 0.5 else "💬"
            st.write(f"{emoji} {tweet.text[:100]}... (Likes: {tweet.public_metrics['like_count']})")

        # === Análise de Palavras === #
        st.subheader("Palavras Mais Usadas")
        words = processor.top_words(tweets, exclude=["furia", "go", "é"])
        for word, count in words:
            st.progress(count / words[0][1], text=f"{word}: {count}x")

        # === Gera nuvem de palavras === #
        text = " ".join(t.text for t in tweets)
        wordcloud = WordCloud().generate(text)
        plt.imshow(wordcloud)
        st.pyplot(plt)