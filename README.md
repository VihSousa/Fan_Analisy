# <img src="https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png" width="40"> FURIA FALA - Chat Interativo para Fãs (Protótipo)

Plataforma para fãs acompanharem o time de CS da FURIA Esports, com análise de sentimentos em redes sociais, simulador de partidas e chat comunitário.

### 🚀 Núcleo do Sistema
| Módulo | Descrição |
|--------|-----------|
| **Chat Inteligente** | Respostas contextualizadas com personalidade do time |
| **Painel Unificado** | Visualização integrada de todas as métricas |
| **API em Tempo Real** | Conexão direta com serviços da FURIA |

### 🔍 Análise de Dados

+  Monitoramento de Twitter: #GoFURIA 
+  Análise de Sentimentos (Positivo/Negativo/Neutro)
+  Nuvem de Palavras em tempo real

🎮 Simulação

+ Placares dinâmicos de partidas
+ Estatísticas de jogadores (KDA, Rating HLTV)
+ Replay de lances importantes

### 📚 Bibliotecas Principais

| Categoria       | Tecnologias                                                                                  | Versão   | Uso Específico                                                                 |
|-----------------|----------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------|
| **Interface**  | <img src="https://img.shields.io/badge/Streamlit-000000?logo=streamlit">                     | 1.28+    | Framework principal para construção da UI                                      |
| **API**        | <img src="https://img.shields.io/badge/Tweepy-000000?logo=twitter">                          | 4.14     | Coleta de tweets em tempo real                                                |
| **NLP**        | <img src="https://img.shields.io/badge/NLTK-000000">                                         | 3.8      | Pré-processamento de texto                                                    |
|                 | <img src="https://img.shields.io/badge/TextBlob-000000">                                     | 0.17     | Análise de sentimentos                                                        |
| **Visualização**| <img src="https://img.shields.io/badge/WordCloud-000000">                                    | 1.9      | Nuvem de palavras                                                             |
|                 | <img src="https://img.shields.io/badge/Matplotlib-000000?logo=python">                      | 3.7      | Geração de gráficos                                                           |
| **Dados**      | <img src="https://img.shields.io/badge/Pandas-000000?logo=pandas">                           | 2.1      | Manipulação de dados                                                          |

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
│   ├── Sentiment.py    → Análise de sentimentos
│   ├── Data.py         → Processamento de dados
│   └── Utils.py        → Funções auxiliares
├── static/
│   └── furia_logo.png  → Assets visuais
├── App.py              → Aplicação principal
└── README.md           → Documentação
```

## Vídeo Demonstrativo

Possibilidade

## Autor ✍️ 

João Vítor Costa Sousa - Desafio FURIA 2025

Primeira vez codando um projeto em python

## Suporte emocional 🫂

Johan Santos - https://github.com/JohanVPS

Lino Menezes - https://github.com/LinoGomes54