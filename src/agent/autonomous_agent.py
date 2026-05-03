from datetime import datetime
import time

from src.agent.collector import coletar_dados
from src.predict import detectar_ataque
from src.IA.incremental_learning import aprender

from src.core.database import salvar_incidente
from src.core.defense_mode import avaliar_defesa
from src.core.autonomous_defense import executar_defesa

from src.agent.response_engine import executar_resposta


print(">>> AGENT VERSAO NOVA CARREGADA <<<")


#CONTROLE GLOBAL DO AGENTE
agent_rodando = False

def iniciar_agente():

    global agent_rodando

    if agent_rodando:
        print("Agent já está rodando.")
        return

    agent_rodando = True

    print("Argus Sentry Autonomous Agent Online")

    while agent_rodando:
        try:
            executar_ciclo()

        except Exception as e:
            print(f"Erro no agente: {e}")

        time.sleep(5)

def parar_agente():
    global agent_rodando
    agent_rodando = False
    print("Argus Agent finalizado com segurança")

def executar_ciclo():

    #coleta
    dados = coletar_dados()

    #IA
    resultado = detectar_ataque(dados)

    # DEBUG
    print("INPUT:", dados)
    print("PRED:", resultado["label"])
    print("-" * 40)

    # resposta imediata
    executar_resposta(resultado)

    # salvar incidente
    salvar_incidente(
        datetime.utcnow().isoformat(),
        resultado["label"],
        resultado["risco"],
        resultado["status"]
    )

    # aprendizado contínuo
    aprender(dados, resultado["label"])

    # modo de defesa
    modo = avaliar_defesa(resultado["label"])

    print(
        f"{resultado['label']} | "
        f"RISCO:{resultado['risco']} | "
        f"MODO:{modo}"
    )

    # DEFESA AUTÔNOMA
    if resultado["label"] != "BENIGN":

        ip = "192.168.0.10"

        print(">>> CHAMANDO DEFESA")

        executar_defesa(resultado["label"], ip)