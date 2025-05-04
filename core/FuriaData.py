class FuriaData:
    def __init__(self, use_firebase=False):
        self.use_firebase = False  # Modo offline

    def get_fluxo(self):

        return {
            "fluxo": {
                "primeira_interacao": {
                    "mensagem": "Bem-vindo ao FURIA FanHub! Para nos conhecer escolha uma opção:",
                    "opcoes": {
                        "jogos": "Jogos",
                        "lideranca": "Liderança"
                    }
                },
                "menu_jogos": {
                    "CS 2": {
                        "Time feminino CS": {
                            "izaa": {
                                "nome": "Izabella Galle",
                                "pseudonimo": "izaa",
                                "data_nascimento": "2000-02-26",
                                "nacionalidade": "Brasileira",
                                "posicao": "AWPer",
                                "redes_sociais": ["@izaacsgo"],
                                "data_entrada": "2020-02-26",
                                "status": "ativo",
                                "estatisticas": {
                                    "rating": 1.10,
                                    "kills": 1200,
                                    "awp_kills": 856,
                                    "clutches": 42
                                }
                            },
                            "gabs": {
                                "nome": "Gabriela Freindorfer",
                                "pseudonimo": "gabs",
                                "data_nascimento": "1998-03-15",
                                "nacionalidade": "Brasileira",
                                "posicao": "Entry Fragger",
                                "redes_sociais": ["@gabscsgo"],
                                "data_entrada": "2023-03-15",
                                "status": "ativo",
                                "estatisticas": {
                                    "rating": 1.05,
                                    "kills": 980,
                                    "entry_sucesso": "72%",
                                    "clutches": 28
                                }
                            }
                        },
                        "Time masculino CS": {
                            "yuurih": {
                                "nome": "Yuri Boian",
                                "pseudonimo": "yuurih",
                                "data_nascimento": "1999-11-08",
                                "nacionalidade": "Brasileiro",
                                "posicao": "Rifle/Lurker",
                                "redes_sociais": ["@yuurihcs"],
                                "data_entrada": "2017-11-08",
                                "status": "ativo",
                                "estatisticas": {
                                    "rating": 1.12,
                                    "kills": 5320,
                                    "multi_kills": 287,
                                    "clutches": 156
                                }
                            },
                            "KSCERATO": {
                                "nome": "Kaike Cerato",
                                "pseudonimo": "KSCERATO",
                                "data_nascimento": "1999-02-06",
                                "nacionalidade": "Brasileiro",
                                "posicao": "Entry Fragger",
                                "redes_sociais": ["@kscerato"],
                                "data_entrada": "2018-02-06",
                                "status": "ativo",
                                "estatisticas": {
                                    "rating": 1.18,
                                    "kills": 6450,
                                    "hs_percent": "58%",
                                    "clutches": 189
                                },
                                "premios": [
                                    "MVP Major Rio 2022",
                                    "TOP 20 HLTV 2021-2023"
                                ]
                            },
                            "FalleN": {
                                "nome": "Gabriel Toledo",
                                "pseudonimo": "FalleN",
                                "data_nascimento": "1991-05-30",
                                "nacionalidade": "Brasileiro",
                                "posicao": "AWPer/IGL",
                                "redes_sociais": ["@fallen"],
                                "data_entrada": "2023-07-03",
                                "status": "ativo",
                                "estatisticas": {
                                    "rating": 1.08,
                                    "kills": 12450,
                                    "awp_kills": 8760,
                                    "clutches": 432
                                },
                                "premios": [
                                    "2x Campeão Major",
                                    "TOP 1 HLTV 2016-2017"
                                ]
                            }
                        },
                        "Treinador CS": {
                            "sidde": {
                                "nome": "Sidnei Macedo",
                                "pseudonimo": "sidde",
                                "nacionalidade": "Brasileiro",
                                "redes_sociais": ["@siddecs"],
                                "data_entrada": "2024-01-01",
                                "status": "ativo",
                                "carreira": [
                                    "Ex-jogador profissional",
                                    "Campeão Brasileiro 2019"
                                ]
                            }
                        }
                    },
                    "Valorant": {
                        "Time masculino Valorant": {
                            "raafa": {
                                "nome": "Rafael Lima",
                                "pseudonimo": "raafa",
                                "data_entrada": "2024-12-09",
                                "nacionalidade": "Brasileiro",
                                "status": "ativo",
                                "agentes_preferidos": ["Jett", "Reyna"],
                                "funcao": "Duelista"
                            },
                            "pryze": {
                                "nome": "Luis Henrique",
                                "pseudonimo": "pryze",
                                "data_entrada": "2025-03-13",
                                "nacionalidade": "Brasileiro",
                                "status": "ativo",
                                "agentes_preferidos": ["Omen", "Astra"],
                                "funcao": "Controlador"
                            }
                        },
                        "Time feminino Valorant": {
                            "Pannshi": {
                                "nome": "Pamella Shibuya",
                                "pseudonimo": "Pannshi",
                                "data_entrada": "2024-03-14",
                                "nacionalidade": "Brasileira",
                                "status": "ativo",
                                "agentes_preferidos": ["Sage", "Killjoy"],
                                "funcao": "Sentinela"
                            },
                            "PaulaNobre": {
                                "nome": "Paula Nobre",
                                "pseudonimo": "Paula Nobre",
                                "data_entrada": "2024-03-14",
                                "nacionalidade": "Brasileira",
                                "status": "ativo",
                                "agentes_preferidos": ["Raze", "Neon"],
                                "funcao": "Duelista"
                            }
                        }
                    }
                },
                "Liderança": {
                    "jaime_padua": {
                        "nome": "Jaime Pádua",
                        "cargo": "CEO & Co-fundador",
                        "redes_sociais": ["@jaimepadua"],
                        "bio": "Responsável pela expansão global da FURIA.",
                        "carreira": [
                            "Fundador da FURIA em 2017",
                            "Investidor em esports desde 2010"
                        ]
                    },
                    "andre_akkari": {
                        "nome": "André Akkari",
                        "cargo": "Presidente de Games & Co-fundador",
                        "redes_sociais": ["@andreakkari"],
                        "bio": "Estrategista de negócios e ex-jogador profissional de poker.",
                        "premios": [
                            "Campeão Mundial de Poker 2011",
                            "Hall da Fama do Poker Brasileiro"
                        ]
                    },
                    "cris_guedes": {
                        "nome": "Cris Guedes",
                        "cargo": "COO & Co-fundadora",
                        "redes_sociais": ["@crisguedes"],
                        "bio": "Lidera operações e parcerias comerciais.",
                        "formacao": "Administração de Empresas - USP"
                    }
                }
            }
        }

    def save_interaction(self, user_id: str, question: str, response: str = None):
        print(f"Interação salva localmente - Pergunta: {question}")
        
    def save_tweet_analysis(self, tweet_data: dict):
        print(f"Tweet analisado (não salvo): {tweet_data.get('text')}")