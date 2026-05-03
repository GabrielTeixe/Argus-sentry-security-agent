def executar_resposta(resultado):

    ataque = resultado.get("attack")

    if ataque == "BruteForce":
        print("Bloqueando IP suspeito")

    elif ataque == "Portscan":
        print("Aplicacando rate limit")

    elif ataque == "DDoS":
        print("Alertando Firewall")

    else:
        print("Tráfego normal")