from core.FuriaData import FuriaData
from core.Sentiment import SentimentAnalyzer
import random

class ChatbotEngine:
    def __init__(self, furia_data: FuriaData):
        self.furia_data = furia_data
        self.analyzer = SentimentAnalyzer()

    def _voltar_menu(self, user_data: dict, fluxo: dict) -> str:
        if user_data['historico_estados']:
            estado_anterior = user_data['historico_estados'].pop()
            user_data['chat_state'] = estado_anterior
            
            if estado_anterior == 'menu_principal':
                return self._formatar_mensagem_inicial(fluxo)
            elif estado_anterior == 'escolha_jogo':
                return "Escolha um jogo:\n- CS 2\n- Valorant"
            elif estado_anterior == 'menu_cs':
                return "Escolha um time CS 2:\n- Masculino\n- Feminino\n- Treinador"
            elif estado_anterior == 'menu_valorant':
                return "Escolha um time:\n- Time masculino Valorant\n- Time feminino Valorant"
        
        user_data['chat_state'] = 'menu_principal'
        return self._formatar_mensagem_inicial(fluxo)

    def generate_response(self, prompt: str, user_data: dict) -> str:
        try:
            fluxo = self.furia_data.get_fluxo()
            prompt = prompt.lower().strip()

            # --- PRIMEIRA INTERAÇÃO ---
            if user_data.get('chat_state') == 'primeira_interacao':
                user_data.update({
                    'chat_state': 'menu_principal',
                    'historico_estados': ['primeira_interacao']
                })
                return self._formatar_mensagem_inicial(fluxo)

            # --- MENU PRINCIPAL ---
            elif user_data.get('chat_state') == 'menu_principal':
                if any(p in prompt for p in ['jogos', 'games']):
                    user_data.update({
                        'chat_state': 'escolha_jogo',
                        'historico_estados': user_data['historico_estados'] + ['menu_principal']
                    })
                    return "Escolha um jogo:\n- CS 2\n- Valorant"
                
                elif any(p in prompt for p in ['liderança', 'lider', 'ceo', 'criadores']):
                    return self._formatar_detalhes(
                        fluxo['fluxo']['Liderança'], 
                        "Liderança FURIA"
                    )
                
                elif 'voltar' in prompt:
                    return self._voltar_menu(user_data, fluxo)
                
                else:
                    return "Opções:\n- Jogos\n- Liderança\n(Digite 'voltar')"

            # --- ESCOLHA DE JOGO ---
            elif user_data.get('chat_state') == 'escolha_jogo':
                if 'cs' in prompt:
                    user_data.update({
                        'chat_state': 'menu_cs',
                        'jogo_selecionado': 'CS 2',
                        'historico_estados': user_data['historico_estados'] + ['escolha_jogo']
                    })
                    return "Escolha um time:\n- Masculino\n- Feminino\n- Treinador"
                
                elif 'valorant' in prompt:
                    user_data.update({
                        'chat_state': 'menu_valorant',
                        'jogo_selecionado': 'Valorant',
                        'historico_estados': user_data['historico_estados'] + ['escolha_jogo']
                    })
                    return "Escolha um time:\n- Masculino\n- Feminino"
                
                elif 'voltar' in prompt:
                    return self._voltar_menu(user_data, fluxo)
                
                else:
                    return "Escolha:\n- CS 2\n- Valorant\n('voltar' para menu)"

            # --- MENU CS ---
            elif user_data.get('chat_state') == 'menu_cs':
                if 'masculino' in prompt:
                    return self._formatar_detalhes(
                        fluxo['fluxo']['menu_jogos']['CS 2']['Time masculino CS'],
                        "CS 2 - Time Masculino"
                    )
                
                elif 'feminino' in prompt:
                    return self._formatar_detalhes(
                        fluxo['fluxo']['menu_jogos']['CS 2']['Time feminino CS'],
                        "CS 2 - Time Feminino"
                    )
                
                elif 'treinador' in prompt:
                    return self._formatar_detalhes(
                        {"Treinador CS": fluxo['fluxo']['menu_jogos']['CS 2']['Treinador CS']},
                        "Treinador CS 2"
                    )
                
                elif 'voltar' in prompt:
                    return self._voltar_menu(user_data, fluxo)
                
                else:
                    return "Escolha:\n- Masculino\n- Feminino\n- Treinador"

            # --- MENU VALORANT ---
            elif user_data.get('chat_state') == 'menu_valorant':
                if 'masculino' in prompt:
                    return self._formatar_detalhes(
                        fluxo['fluxo']['menu_jogos']['Valorant']['Time masculino Valorant'],
                        "Valorant - Time Masculino"
                    )
                
                elif 'feminino' in prompt:
                    return self._formatar_detalhes(
                        fluxo['fluxo']['menu_jogos']['Valorant']['Time feminino Valorant'],
                        "Valorant - Time Feminino"
                    )
                
                elif 'voltar' in prompt:
                    return self._voltar_menu(user_data, fluxo)
                
                else:
                    return "Escolha:\n- Masculino\n- Feminino"

            return self._fallback_response(prompt)

        except Exception as e:
            print(f"ERRO: {str(e)}")
            return "Erro temporário. Digite 'voltar' para recomeçar."

    def _formatar_detalhes(self, dados: dict, titulo: str) -> str:
        if not dados:
            return f"Nenhuma informação disponível para {titulo}.\n\nDigite 'voltar' para menu anterior."
        
        response = f"**{titulo}**\n\n"
        
        for i, (id_item, item) in enumerate(dados.items()):
            if i > 0:  # Adiciona linha antes de cada jogador, exceto o primeiro
                response += "______________________________________________________________________________\n\n"
                
            if isinstance(item, str):
                response += f"{item}\n\n"
                continue
                
            response += f"**{item.get('pseudonimo', id_item)}**\n\n"  # Duas quebras de linha após o nome
            
            # Info básica com espaçamento
            campos = ["nome", "\nposicao", "\nnacionalidade", "\nstatus", "\ndata_entrada"]
            for campo in campos:
                if campo in item:
                    response += f"• **{campo.title()}:** {item[campo]}\n"  # Quebra de linha após cada item
            
            response += "\n"  # Espaço entre seções
            
            # Seções especiais formatadas
            secoes = {
                "estatisticas": "Estatísticas",
                "premios": "Prêmios",
                "agentes_preferidos": "Agentes Preferidos",
                "carreira": "Carreira"
            }
            
            for secao, titulo_secao in secoes.items():
                if secao in item and item[secao]:
                    response += f"**{titulo_secao}:**\n"
                    if isinstance(item[secao], dict):
                        for k, v in item[secao].items():
                            response += f"- {k}: {v}\n"
                    elif isinstance(item[secao], list):
                        for elem in item[secao]:
                            response += f"- {elem}\n"
                    else:
                        response += f"- {item[secao]}\n"
                    response += "\n"  # Espaço após cada seção
        
        response += "\nDigite 'voltar' para menu anterior."
        return response

    def _formatar_mensagem_inicial(self, fluxo: dict) -> str:
        return (fluxo['fluxo']['primeira_interacao']['mensagem'] + "\n" +
               "\n".join([f"- {opcao}" for opcao in fluxo['fluxo']['primeira_interacao']['opcoes'].values()]))

    def _fallback_response(self, prompt: str) -> str:
        return "Opção inválida. Digite 'voltar' para menu."