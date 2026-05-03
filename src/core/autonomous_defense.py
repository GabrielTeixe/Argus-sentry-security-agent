from src.core.response_engine import (
    bloquear_ip,
    registrar_evento,
    aprender
)

def executar_defesa(label, ip):

    print("ENTREI NA FUNÇÃO executar_defesa")
    print("DEFESA AUTÔNOMA ATIVADA")

    bloquear_ip(ip)
    registrar_evento(label)
    aprender(label)

    print("IP BLOQUEADO")

    return "AUTONOMOUS_DEFENSE_EXECUTED"