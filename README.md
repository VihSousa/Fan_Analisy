# FURIA FALA - Chat Oficial para Fãs

Plataforma interativa para fãs do time de CS da FURIA Esports acompanharem jogos, interagirem com outros torcedores e visualizarem análises em tempo real.

## Funcionalidades Principais

### 💬 Chat Oficial
- Interface conversacional intuitiva
- Navegação entre diferentes módulos
- Respostas interativas baseadas nas escolhas do usuário

### 🐦 Análise de Tweets
- Coleta de tweets em tempo real com a hashtag #GoFURIA
- Análise de sentimentos (positivo/negativo/neutro)
- Métricas de engajamento da torcida
- Nuvem de palavras mais usadas pelos fãs

### 🎮 Simulador de Partidas ao Vivo
- Acompanhamento do placar em tempo real
- Estatísticas detalhadas dos jogadores (K/D/A e rating)
- Eventos da partida atualizados ao longo do tempo
- Simulação realista da progressão do jogo

### 👥 Chat da Torcida
- Interação com outros torcedores simulados
- Sistema de mensagens em tempo real
- Respostas dinâmicas baseadas no contexto da partida
- Interface personalizada que diferencia mensagens do usuário

### 📊 Dashboard Completo
- Visualização integrada de todas as funcionalidades
- Métricas e estatísticas consolidadas
- Interface intuitiva e responsiva

## Tecnologias Utilizadas

- **Python 3.10+**: Linguagem base do projeto
- **Streamlit**: Framework para interface web interativa
- **Tweepy**: API para conexão com Twitter
- **TextBlob**: Biblioteca para análise de sentimentos
- **WordCloud**: Visualização de texto em nuvem de palavras
- **Pandas**: Manipulação e análise de dados
- **Matplotlib**: Geração de gráficos e visualizações
- **NLTK**: Processamento de linguagem natural

## Como Executar

1. Clone este repositório
2. Instale as dependências:
```
pip install -r docs/requirements.txt
```
3. Crie um arquivo `.env` na raiz do projeto com suas credenciais do Twitter:
```
API_KEY=sua_chave_aqui
API_SECRET=seu_segredo_aqui
API_BEARER=seu_token_bearer_aqui
```
4. Execute a aplicação:
```
streamlit run App.py
```

## Estrutura do Projeto

- **App.py**: Aplicação principal e interface do usuário
- **core/**: Módulos principais
  - **Twitter.py**: Conexão com API do Twitter
  - **Sentiment.py**: Análise de sentimentos
  - **Data.py**: Processamento de dados
  - **Utils.py**: Funções utilitárias

## Próximos Passos

- Implementação de perfil de usuário
- Sistema de notificações em tempo real
- Integração com transmissões ao vivo
- Enquetes e votações interativas
- Conteúdo exclusivo para membros

## Vídeo Demonstrativo

[Link para o vídeo de demonstração]

## Autor

João Vítor Costa Sousa - Desafio FURIA 2025

## Suporte com o Layout

Johan Santos - https://github.com/JohanVPS