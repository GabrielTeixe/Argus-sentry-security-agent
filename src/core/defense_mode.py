historico = []

ATAQUES_CRITICOS = ["BruteForce", "PortScan", "DDoS"]

def avaliar_defesa(label):

    historico.append(label)

    # manter histórico pequeno (evita crescer infinito)
    if len(historico) > 20:
        historico.pop(0)

    ultimos = historico[-5:]

    if label in ATAQUES_CRITICOS and ultimos.count(label) >= 3:
        return "DEFESA_AUTONOMA_ATIVADA"

    return "MONITORANDO"