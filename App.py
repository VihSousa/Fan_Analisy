import streamlit as st # Dashboard web interativo
from core.Twitter import TwitterAPI
from core.Sentiment import SentimentAnalyzer 
from core.Data import DataProcessor
from wordcloud import WordCloud # Nuvem de palavras
import matplotlib.pyplot as plt
plt.switch_backend('Agg')  # Fix para o Streamlit
import nltk
nltk.download('stopwords', quiet=True) # Donwload "silencioso" (adicionar às notas no obsidian) ==============TIRAR DPS=============
from nltk.corpus import stopwords 
import random  # Respostas aleatórias do bot
from collections import Counter


# === Configuração inicial === #
twitter = TwitterAPI()
analyzer = SentimentAnalyzer()
processor = DataProcessor()

st.set_page_config(
    page_title="FURIAFALA", # Criar um título melhor ================================
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        .stApp {
            background-color: #0c1414 !important;
        }
    </style>
""", unsafe_allow_html=True)


# === Botão de recarregar === #
if st.button("Recarregar Tweets"):
    tweets = twitter.get_tweets() 
    st.rerun()


# === Tratamento de erros na  === #
try:
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
            st.subheader("🔥 Top Palavras da Torcida")
            words = processor.top_words(tweets, exclude=["furia", "go", "é", "pra", "para"])
            col1, col2, col3 = st.columns(3)
            for i, (word, count) in enumerate(words[:9]):  # Mostra 9 palavras (3 por linha)
                with (col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3):
                    st.metric(label=word.capitalize(), value=f"{count}x")


            # === Nuvem de palavras === #
            stopwords_pt = set(stopwords.words("portuguese")) | {"furia", "go", "é", "pra"}
            text = " ".join(t.text for t in tweets)
            if text.strip():
                wordcloud = WordCloud(
                    width=800,
                    height=400,
                    background_color="#0c1414",
                    colormap="Blues",
                    contour_width=0,            # Remove bordas
                    stopwords=stopwords_pt,
                    max_words=50,
                    margin=0                    # Remove espaçamento externo
                ).generate(text)

                plt.figure(figsize=(10, 5), facecolor="#0c1414")  # Fundo do gráfico
                plt.imshow(wordcloud, interpolation="bilinear")
                plt.axis("off")
                plt.tight_layout(pad=0)
                st.pyplot(plt, facecolor="#0c1414")  # Fundo ao redor da imagem
                
            
except Exception as e:  # Atualização: Captura erros genéricos
    st.error(f"Erro inesperado: {e}")


# === CHATBOT FURIA === #                      # Atualização: respostas inteligentes
st.subheader("Chat da Torcida FURIA")  

if "messages" not in st.session_state:  
    st.session_state.messages = []  

# === Histórico === #  
for msg in st.session_state.messages:  
    st.chat_message(msg["role"]).write(msg["content"])  

# === Input do usuário === # 
if prompt := st.chat_input("Digite algo pro bot..."):  
    
    sentiment = analyzer.analyze(prompt)
    
    if sentiment["polarity"] > 0.3:
        resposta = random.choice([
            "FURIA Bot: TÁ PEGANDO FOGO, PORRA! 🐯🔥",
            "FURIA Bot: É ISSO, ENCHAPA DE EMOÇÃO! 💥"
        ])
    elif "!grito" in prompt.lower():
        resposta = "FURIA Bot: " + random.choice([
            "VAMO QUE VAMO! 🚀", 
            "AQUI É BRABO! 💪",
            "TÁ CHEIRANDO A VITÓRIA! 👃"
        ])
    else:
        resposta = "FURIA Bot: BORA JOGAR! 🔥"

    # === Histórico === # 
    st.session_state.messages.append({"role": "user", "content": prompt})  
    st.session_state.messages.append({"role": "assistant", "content": resposta})  
    st.rerun()


# === Simulador de jogos === #                             EM PRODUÇÃO
if st.button("Simular Jogo Ao Vivo 🎮"):
    st.write("🔴 LIVE: FURIA 10-5 MIBR (Mapa: Mirage)")
    st.write("KSCERATO: 20 kills | arT: 15 assists")
    st.write("Última rodada: Clutch do KSCERATO 1v3!")