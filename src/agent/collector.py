import random

def coletar_dados():

    ataque = random.choice([
        "BENIGN",
        "BruteForce",
        "PortScan",
        "DDoS"
    ])

    if ataque == "BENIGN":
        return [random.uniform(0, 0.3) for _ in range(10)]

    if ataque == "BruteForce":
        return [random.uniform(0.7, 1.0) for _ in range(10)]

    if ataque == "PortScan":
        return [random.uniform(0.4, 0.6) for _ in range(10)]

    if ataque == "DDoS":
        return [random.uniform(0.8, 1.2) for _ in range(10)]