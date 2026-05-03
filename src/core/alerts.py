alertas = []

def verificar_alerta(label):

    if label == "desconhecido":

        alerta = {
            "type": "UNKNOWN_ATTACK",
            "message": "POSSIVEL ATAQUE DESCONHECIDO DETECTADO"
        }

        alertas.append(alerta)

        print(alerta["message"])