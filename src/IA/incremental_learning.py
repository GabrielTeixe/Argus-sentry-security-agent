import joblib
import numpy as np

MODEL_PATH = "models/model.pkl"

modelo = joblib.load(MODEL_PATH)

# mapping obrigatório para ML
LABEL_MAP = {
    "BENIGN": 0,
    "BruteForce": 1,
    "PortScan": 2,
    "DDoS": 3
}

def aprender(dados, label):

    # converte label -> número
    if label not in LABEL_MAP:
        print("⚠️ Ataque desconhecido - aprendizado ignorado")
        return

    X = np.array([dados])
    y = np.array([LABEL_MAP[label]])

    # só aprende se o modelo suportar
    if hasattr(modelo, "partial_fit"):

        modelo.partial_fit(X, y)

        joblib.dump(modelo, MODEL_PATH)

        print(" Modelo atualizado (incremental learning)")

    else:
        print(" Modelo não suporta aprendizado incremental")