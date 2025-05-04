import streamlit as st
from core.FuriaData import FuriaData
from core.Twitter import TwitterAPI
from core.Sentiment import SentimentAnalyzer
from datetime import datetime
from core.ChatInfo import ChatbotEngine

# ================= CONFIGURAÇÃO INICIAL ================= #
furia_data = FuriaData()
twitter = TwitterAPI()

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
if 'chat_initialized' not in st.session_state:
    st.session_state.chat_initialized = False

# ================= SIDEBAR ================= #
def show_sidebar():
    """Sidebar com informações do usuário"""
    with st.sidebar:
        st.markdown("""
            <style>
                div[data-testid="stImage"] {
                    margin: 0 auto !important;
                    display: block !important;
                    text-align: center !important;
                }
            </style>
        """, unsafe_allow_html=True)
        
        st.image("https://camo.githubusercontent.com/3c10bb133a88bd018c8c3c4ebdee572c404271504e3985b0a063000aba96acec/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f70742f662f66392f46757269615f4573706f7274735f6c6f676f2e706e67", 
                width=100)

        st.markdown("---")
        if st.session_state.user_data and 'nome' in st.session_state.user_data:
            st.subheader("Seu Perfil")
            st.write(f"👤 {st.session_state.user_data['nome']}")
            st.write(f"📅 Cadastro: {st.session_state.user_data.get('data', 'N/A')}")
            st.write(f"🎮 Jogador Favorito: {st.session_state.user_data.get('jogador', 'N/A')}")
            
        st.markdown("---")
        if st.button("🔙 Voltar"):
            st.rerun()

# ================= TELA DE LOGIN ================= #
def show_login():
    st.title("Acesso FURIA FanHub")
    
    with st.form("login_form"):
        nome = st.text_input("Nome Completo*")
        email = st.text_input("Email*")
        jogador = st.selectbox("Jogador Favorito*", ["KSCERATO", "arT", "yuurih", "chelo", "drop"])
        
        with st.expander("Informações Adicionais (Opcional)"):
            jogo_favorito = st.selectbox("Jogo Favorito", ["CS:GO", "Valorant", "LOL", "Outro"])
            engajamento = st.radio("Nível de Engajamento", ["Casual", "Fan", "Super Fan"])
        
        if st.form_submit_button("Entrar no Chat"):
            if nome and email:
                st.session_state.user_data = {
                    "nome": nome,
                    "email": email,
                    "jogador": jogador,
                    "data": datetime.now().strftime("%d/%m/%Y"),
                    "jogo_favorito": jogo_favorito,
                    "engajamento": engajamento,
                    "chat_state": "primeira_interacao",
                    "historico_estados": []
                }
                st.session_state.chat_initialized = True
                st.rerun()

# ================= CHAT PRINCIPAL ================= #
def show_chat():
    # Inicializa o chat se necessário
    if not st.session_state.chat_initialized:
        st.session_state.user_data = {
            **st.session_state.user_data,
            "chat_state": "primeira_interacao",
            "historico_estados": []
        }
        st.session_state.chat_initialized = True

    # Inicializa dependências
    analyzer = SentimentAnalyzer()  
    chatbot = ChatbotEngine(furia_data)
    
    show_sidebar()
    
    st.title(f"Chat FURIA - Olá {st.session_state.user_data['nome'].split()[0]}!")
    
    # Abas de funcionalidades
    tab1, tab2, tab3 = st.tabs(["Tweets", "Simulador", "Chat"])
    
    with tab1:
        try:
            tweets = twitter.get_formatted_tweets()
            st.metric("Tweets Coletados", len(tweets))
            
            for tweet in tweets[:5]:
                with st.expander(f"{tweet['engagement']} - {tweet['author']}"):
                    st.write(tweet['full_text'])
                    st.caption(tweet['date'])
        except Exception as e:
            st.error(f"Erro ao processar tweets: {e}")
            st.write("FURIA venceu a partida! #GoFURIA")
        
    with tab2:
        st.subheader("Simulador Ao Vivo")
        col1, col2, col3 = st.columns(3)
        col1.metric("FURIA", "12")
        col2.metric("VS", "")
        col3.metric("MIBR", "9")
        st.progress(65)
        st.write("Últimos lances:")
        st.write("- KSCERATO 3 kills na B")
        st.write("- arT faz clutch 1v2")
    
    with tab3:
        st.subheader("Chat da Torcida")
        
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])
        
        if prompt := st.chat_input("Digite sua mensagem..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            response = chatbot.generate_response(prompt, st.session_state.user_data)
            
            st.session_state.messages.append(
                {"role": "assistant", "content": f"FURIA Bot: {response}"}
            )
            st.rerun()

# ================= ROTEAMENTO PRINCIPAL ================= #
def main():
    if st.session_state.user_data:
        show_chat()
    else:
        show_login()

if __name__ == "__main__":
    main()