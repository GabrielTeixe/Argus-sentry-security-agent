import time

from src.agent.collector import coletar_dados
from src.agent.incident_logger import registrar_incidente
from src.agent.response_engine import executar_resposta

from src.predict import detectar_ataque
from src.api import (
    validar_dados,
    verificar_integridade_modelo,
    detectar_ataque
)

class ArgusAgent:

    def __init__(self, intervalo = 5):
        self.intervalo = intervalo

    def iniciar_agente(self):

        print("Argus Sentry Autonomous Agent Online")

        verificar_integridade_modelo()

        while True:
            try:
                dados = coletar_dados()

                validar_dados(dados)

                resultado = detectar_ataque(dados)

                executar_resposta(resultado)

                registrar_incidente(resultado)

                print(f"OFENSIVA DETECTADA: {resultado['label']}")

            except Exception as e:
                print(f"Erro no sistema: {e}")

            time.sleep(self.intervalo)

def iniciar_agente():
    agente = ArgusAgent(intervalo=5)
    agente.iniciar_agente()