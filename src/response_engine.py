from datetime import datetime

def executar_resposta(label, ip="unknown"):

    acoes = []

    if label == "Bruteforce":
        acoes.append("Bloquear IP")
        acoes.append("Aumentar nível de monitoramento")

    elif label == "PortScan":
        acoes.append("Limitar conexões")
        acoes.append("Registrar atividade suspeita")

    elif label == "DDoS":
        acoes.append("Ativar rate limit")
        acoes.append("Notificar administrador")

    else:
        acoes.append("Monitoramento Padrão")

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "acoes_executadas": acoes
    }