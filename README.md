# <img src="https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png" width="35"> FURIA FALA - Chat Interativo para Fãs (Protótipo)

Plataforma para fãs acompanharem o time de CS da FURIA Esports, de fã para fã.

### 🚀 Núcleo do Sistema
| Módulo                     | Descrição                                            |
|----------------------------|------------------------------------------------------|
| **Chat Inteligente**       | Respostas contextualizadas com informações do time   |
| **Simulador de partidas**  | Visualização integrada de todas as métricas          |
| **API do Twitter**         | Avaliação dos fãs através dos cometários FURIA       |

### 🤖 Chat Inteligente
- Respostas contextualizadas sobre times e jogadores
- Navegação hierárquica por categorias
- Histórico de conversas persistente

### 🎮 Simulador de Partidas
- Placares atualizados em tempo real
- Estatísticas detalhadas (KDA, Rating HLTV)
- Replay de lances importantes
- Comparativo entre times

### 📚 Bibliotecas Principais

| Categoria       | Tecnologias                                                                                  | Versão   | Uso Específico                                                                 |
|-----------------|----------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------|
| **Interface**   | <img src="https://img.shields.io/badge/Streamlit-000000?logo=streamlit">                     | 1.28+    | Framework principal para construção da UI                                      |
| **API**         | <img src="https://img.shields.io/badge/Tweepy-000000?logo=twitter">                          | 4.14     | Coleta de tweets em tempo real                                                 |
| **NLP**         | <img src="https://img.shields.io/badge/NLTK-000000">                                         | 3.8      | Pré-processamento de texto                                                     |
|                 | <img src="https://img.shields.io/badge/TextBlob-000000">                                     | 0.17     | Análise de sentimentos                                                         |
| **Visualização**| <img src="https://img.shields.io/badge/WordCloud-000000">                                    | 1.9      | Nuvem de palavras                                                              |
|                 | <img src="https://img.shields.io/badge/Matplotlib-000000?logo=python">                       | 3.7      | Geração de gráficos                                                            |
| **Dados**       | <img src="https://img.shields.io/badge/Pandas-000000?logo=pandas">                           | 2.1      | Manipulação de dados                                                           |

### ⚙️ Infraestrutura

```bash
Python 3.10+  # Versão base
dotenv        # Gerenciamento de variáveis de ambiente
```

## 🚀 Configuração e Execução

### Pré-requisitos
- Python 3.10+
- Conta de Desenvolvedor do Twitter ([crie aqui](https://developer.twitter.com/))
- Git (para clonagem)

### ⚙️ Instalação Passo-a-Passo

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/furia-fala.git
cd furia-fala

# Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Instale as dependências
pip install -r docs/requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env 
```

Edite o .env com suas credenciais:

.env:
```
API_KEY=sua_chave_aqui
API_SECRET=seu_segredo_aqui
API_BEARER=seu_token_bearer_aqui
```

▶️ Execução
```bash
streamlit run App.py
Acesse: http://localhost:8501
```

🏗️ Estrutura do Código
```
furia-fala/
├── core/
│   ├── Twitter.py      → Conexão com API Twitter
│   ├── FuriaData.py    → Dados sobre o time e a equipe
│   ├── ChatInfo.py     → Organização e manipulação dos dados
│   ├── Sentiment.py    → Análise de sentimentos
│   ├── Data.py         → Processamento de dados
│   └── Utils.py        → Funções auxiliares
├── static/
│   └── furia_logo.png  → Assets visuais
├── App.py              → Aplicação principal
├── Index.html          → Introduço web
├── IDEA.md             → Aprendizado e ideias do desenvolvedor
└── README.md           → Documentação
```

## Autor ✍️ 

João Vítor Costa Sousa - Desafio FURIA 2025

Primeira vez codando um projeto 90% em python

## Suporte emocional 🫂

Johan Santos - https://github.com/JohanVPS

Lino Menezes - https://github.com/LinoGomes54


Para visualizar a documentação completa do projeto planejado, acesse [IDEA.md](IDEA.md).
