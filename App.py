import streamlit as st
from core.Twitter import TwitterAPI
from core.Sentiment import SentimentAnalyzer 
from core.Data import DataProcessor
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.switch_backend('Agg')
import nltk
from nltk.corpus import stopwords 
import random
from collections import Counter
from datetime import datetime
from streamlit.components.v1 import html

# ================= CONFIGURAÇÃO INICIAL ================= #
st.set_page_config(
    page_title="FURIA FanHub",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= ESTADO DA SESSÃO ================= #
if 'user_data' not in st.session_state:
    st.session_state.user_data = None
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'show_html' not in st.session_state:
    st.session_state.show_html = True


# ================= SIDEBAR ================= #
def show_sidebar():
    """Sidebar com informações do usuário"""
    with st.sidebar:
        # CSS customizado (solução definitiva)
        st.markdown("""
            <style>
                div[data-testid="stImage"] {
                    margin: 0 auto !important;
                    display: block !important;
                    text-align: center !important;
                }
            </style>
""", unsafe_allow_html=True)
        
        # Imagem (agora vai centralizar)
        st.image("https://camo.githubusercontent.com/3c10bb133a88bd018c8c3c4ebdee572c404271504e3985b0a063000aba96acec/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f70742f662f66392f46757269615f4573706f7274735f6c6f676f2e706e67", 
                width=100)
        
        # Restante do conteúdo
        st.markdown("---")
        if st.session_state.user_data:
            st.subheader("Seu Perfil")
            st.write(f"👤 {st.session_state.user_data['nome']}")
            st.write(f"📅 Cadastro: {st.session_state.user_data['data']}")
            st.write(f"🎮 Jogador Favorito: {st.session_state.user_data['jogador']}")
            
        st.markdown("---")
        if st.button("🔙 Voltar"):
            st.session_state.show_html = True
            st.rerun()

# ================= TELA DE LOGIN ================= #
def show_login():
    """Tela de cadastro/login"""
    st.title("🔐 Acesso FURIA FanHub")
    
    with st.form("login_form"):
        nome = st.text_input("Nome Completo*")
        email = st.text_input("Email*")
        jogador = st.selectbox("Jogador Favorito*", ["KSCERATO", "arT", "yuurih", "chelo", "drop"])
        
        if st.form_submit_button("👉 Entrar no Chat"):
            if nome and email:
                st.session_state.user_data = {
                    "nome": nome,
                    "email": email,
                    "jogador": jogador,
                    "data": datetime.now().strftime("%d/%m/%Y")
                }
                st.session_state.show_html = False
                st.rerun()
            else:
                st.error("Preencha os campos obrigatórios!")

# ================= CHATBOT PRINCIPAL ================= #
def show_chat():
    """Tela principal do chatbot"""
    twitter = TwitterAPI()
    analyzer = SentimentAnalyzer()
    processor = DataProcessor()
    
    show_sidebar()
    
    st.title(f"💬 Chat FURIA - Olá {st.session_state.user_data['nome'].split()[0]}!")
    
    # Abas de funcionalidades
    tab1, tab2, tab3 = st.tabs(["🐦 Tweets", "🎮 Simulador", "💬 Chat"])
    
    with tab1:
        try:
            tweets = twitter.get_tweets() or []
            
            if not tweets:
                st.warning("Nenhum tweet encontrado. Usando dados de exemplo.")
                tweets = [{
                    "text": "FURIA venceu a partida! #GoFURIA",
                    "user": {"screen_name": "furia_fan"},
                    "public_metrics": {"like_count": 150},
                    "created_at": datetime.now().strftime("%H:%M")
                }]
            
            # Métricas
            col1, col2, col3 = st.columns(3)
            col1.metric("Tweets", len(tweets))
            col2.metric("Positivos", f"{sum(1 for t in tweets if analyzer.analyze(t.text)['polarity'] > 0)}")
            
            # Tweets destacados
            for tweet in sorted(tweets, key=lambda x: x.public_metrics.get('like_count', 0), reverse=True)[:3]:
                with st.expander(f"❤️ {tweet.public_metrics.get('like_count', 0)} likes - @{tweet.user.screen_name}"):
                    st.write(tweet.text)
                    st.caption(tweet.created_at)
        
        except Exception as e:
            st.error(f"Erro ao buscar tweets: {str(e)}")
        
    with tab2:
        st.subheader("🎮 Simulador Ao Vivo")
        col1, col2, col3 = st.columns(3)
        col1.metric("FURIA", "12")
        col2.metric("VS", "")
        col3.metric("MIBR", "9")
        st.progress(65)
        st.write("⚡ Últimos lances:")
        st.write("- KSCERATO 3 kills na B")
        st.write("- arT faz clutch 1v2")
    
    with tab3:
        st.subheader("💬 Chat da Torcida")
        
        # Histórico de mensagens
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])
        
        # Input do usuário
        if prompt := st.chat_input("Digite sua mensagem..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Respostas inteligentes
            sentiment = analyzer.analyze(prompt)
            if sentiment["polarity"] > 0.3:
                resposta = random.choice([
                    "TÁ PEGANDO FOGO, PORRA! 🐯🔥",
                    "É ISSO, ENCHAPA DE EMOÇÃO! 💥"
                ])
            else:
                resposta = random.choice([
                    "BORA JOGAR! 🔥",
                    "VAMO QUE VAMO! 🚀"
                ])
            
            st.session_state.messages.append(
                {"role": "assistant", "content": f"FURIA Bot: {resposta}"}
            )
            st.rerun()

# ================= ROTEAMENTO PRINCIPAL ================= #
def main():
    # Verifica mensagens do HTML
    try:
        from streamlit.components.v1 import components
        event = components.receive_message()
        if event and event.get("action") == "change_page":
            st.session_state.show_html = False
            st.rerun()
    except:
        pass
    
    # Mostra a página apropriada
    if False:
        show_html_page()
        show_login()  # Mostra login abaixo do HTML
    else:
        if st.session_state.user_data:
            show_chat()
        else:
            show_login()

if __name__ == "__main__":
    main()