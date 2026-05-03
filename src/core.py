from fastapi import HTTPException
from typing import List
import joblib
import hashlib
import numpy as np
from sklearn.ensemble import IsolationForest
import pandas as pd

from src.threat_intelligence import obter_mitre
from src.explain import carregar_explainer, explicar
from src.agent.response_engine import executar_resposta

CAMINHO_MODELO = "models/model.pkl"
CAMINHO_HASH = "models/model_hash.txt"

# CARREGAR MODELO

try:
    model = joblib.load(CAMINHO_MODELO)
except Exception:
    raise RuntimeError("Erro ao carregar modelo")

NUM_FEATURES = model.n_features_in_

explainer = carregar_explainer(model)

# DETECTOR

X_normal = np.random.rand(1000, NUM_FEATURES)

iso = IsolationForest(
    contamination=0.01,
    random_state=42
)

iso.fit(X_normal)

# VALIDAÇÃO

def validar_dados(dados: List[float]):

    if not isinstance(dados, list):
        raise HTTPException(400, "Dados devem ser uma lista")

    if len(dados) != NUM_FEATURES:
        raise HTTPException(
            400,
            f"Número de features inválido. Esperado: {NUM_FEATURES}"
        )

    if not all(isinstance(x, (int, float)) for x in dados):
        raise HTTPException(
            400,
            "Todas as features devem ser números"
        )


def verificar_integridade_modelo():

    with open(CAMINHO_MODELO, "rb") as f:
        dados_modelo = f.read()

    with open(CAMINHO_HASH, "r") as f:
        hash_original = f.read().strip()

    hash_atual = hashlib.sha256(dados_modelo).hexdigest()

    if hash_atual != hash_original:
        raise HTTPException(
            500,
            "Modelo corrompido ou alterado!"
        )

# IA PRINCIPAL

def detectar_ataque(dados):

    validar_dados(dados)

    if hasattr(model, "feature_names_in_"):
        df = pd.DataFrame(
            [dados],
            columns=model.feature_names_in_
        )
        pred = model.predict(df)[0]
    else:
        pred =model.predict([dados])[0]

    mitre = obter_mitre(pred)

    feature_importances = explicar(explainer, dados)

    adversarial_pred = iso.predict([dados])[0]
    adversarial = bool(adversarial_pred == -1)

    resultado = {
        "status": "normal" if pred == "BENIGN" else "ataque",
        "label": str(pred),
        "mitre_technique": mitre["technique"],
        "mitre_description": mitre["description"],
        "risco": 0 if pred == "BENIGN" else 90,
        "feature_importances": feature_importances,
        "adversarial": adversarial,
    }

    resultado["response_actions"] = executar_resposta(resultado)

    return resultado