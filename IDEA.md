# <img src="https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png" width="40">  Resultado ideal - Furia Fala

Esse arquivo é feito, exclusivamente, para representar a ideia inicial, as dificuldades e aprendizado passados durante o projeto, e as mudanças feitas para alcançar o resultado final, prensente no README.md

## Objetivo Inicial
Unir os desafios **Experiência Conversacional** e **Know Your Fan** em uma solução integrada:  
- **Chatbot web** para interação do fãs (datas de jogos, lives, históricos).  
- **Painel analítico** que obtenha o maior número de informações dos fãs, através das suas redes sociais. 

## Plano

Criar uma web chatbot que possa tirar duvidas dos fãs, com respostas predeterminadas para data dos jogos, onde serão disponibilizados, as lives em andamento, placares antigos. Além desse proposito básico, o chatbot deveria trazer um resumo das discursões no twitter (comentarios mais curtidos, palavras chaves, dashbord, etc.), mostrar as redes sociais da empresa, informações básicas dos players e seus perfis publicos.

#### Tecnologias planejadas aplicadas

| Módulo             | Descrição                                            |
|--------------------|------------------------------------------------------|
| **GPT-3.5 Turbo**  | Respostas contextualizadas com personalidade do time |
| **Twitter API v2** | Coleta de dados do Twitter/X                         |
| **Tweepy**         | Processar os dados da API                            | 
| **Streamlit**      | painéis interativos                                  |
| **Liquipedia**     | Dados de jogadores, partidas e históricos            |
| **Twitch API**     | Informações em tempo real sobre transmissões         |
| **Firebase**       | Armazenar informações                                |
| **Streamlit**      | painéis interativos                                  |

### Resultado real

Essa foi a minha primeira vez trabalhando com Pythom para um projeto desse nível, minha linguagem principal é Java. Me orgulho da minha determinação e competitividade, vi muitos repositorios de, possiveis, candidatos para a mesma vaga, não podia ficar para trás, aprendi o máximo da linguaguem, fugi do desafio convencional e superei os milhares de erros que apareciam. Porém, o tempo não permitiu que eu entregasse esse resultado planejado. Quem sabe, no final do semestre, use esse projeto para treinar Python, e adicionar um pouco do meu estilo.

Algumas das ideias tiveram que ser descartadas ou reduzidas, como:

#### Ideias Descartadas/Reduzidas

| Feature Planejada                | Motivo                            | Alternativa Adotada                  |
|----------------------------------|-----------------------------------|--------------------------------------|
| Upload de imagens                | Complexidade backend              | Removido do MVP                      |
| Validação por IA custom          | Limitações do GPT-3.5 Turbo       | Filtros manuais com TextBlob         |
| Dados Twitter em tempo real      | Rate limit da API (100 tweets)    | Dataset estático, em caso de erro    |
| Menor número de bibliotecas      | Tempo de entrega                  | Foco no Streamlit                    |

### Bibliotecas Python Aprendidas

#### Análise de Dados

+ pandas  # Manipulação de DataFrames
+ TextBlob  # Análise de sentimentos (básica)
+ wordcloud  # Nuvem de palavras

#### APIs

+ tweepy  # Consumo da Twitter API
+ python-twitch  # Integração com Twitch

#### Visualização

+ matplotlib  # Gráficos estáticos
+ plotly  # Gráficos interativos
+ streamlit  # UI web rápida

#### Utilitários

+ dotenv  # Gerenciamento de credenciais
+ firebase-admin  # Conexão com Firebase
