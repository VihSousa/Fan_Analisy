import json
import os
from datetime import datetime

class FanProfile:
    @staticmethod
    def create(nome, email, cpf, jogador_favorito):
        return {
            "nome": nome,
            "email": email,
            "cpf": cpf,
            "jogador_favorito": jogador_favorito,
            "cadastro": datetime.now().strftime("%d/%m/%Y")
        }