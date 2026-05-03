import joblib
from fastapi import HTTPException
import pandas as pd

CAMINHO_MODELO = "models/model.pkl"

# Carregar modelo

try:
    modelo = joblib.load(CAMINHO_MODELO)
except Exception:
    raise RuntimeError("Erro ao carregar modelo de IA")

# Descobrir automaticamente
# quantas features o modelo espera

N_FEATURES = modelo.n_features_in_

# Validação automática
def validar_dados(dados):

    if not isinstance(dados, list):
        raise HTTPException(
            status_code=400,
            detail="Dados devem ser uma lista"
        )

    if len(dados) != N_FEATURES:
        raise HTTPException(
            status_code=400,
            detail=f"Número de features inválido. Esperado: {N_FEATURES}"
        )

    if not all(isinstance(x, (int,float)) for x in dados):
        raise HTTPException(
            status_code=400,
            detail="Todas as features devem ser números"
        )

# Detector principal

def detectar_ataque(dados):

    validar_dados(dados)

    if hasattr(modelo, "feature_names_in_"):
        df = pd.DataFrame(
            [dados],
            columns= modelo.feature_names_in_
        )
        pred = modelo.predict(df)[0]
    else:
        pred = modelo.predict([dados])[0]

    if pred == "BENIGN":
        return {
            "status": "normal",
            "label": str(pred),
            "risco": 0
        }

    return {
        "status": "ataque",
        "label": str(pred),
        "risco": 90
    }