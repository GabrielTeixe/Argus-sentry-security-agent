import joblib
import pandas as pd

MODEL_PATH = "models/model.pkl"

try:
    modelo = joblib.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Erro ao carregar modelo: {e}")

if hasattr(modelo, "feature_names_in_"):
    FEATURE_NAMES = list(modelo.feature_names_in_)
else:
    raise RuntimeError(
        "Modelo não possui feature_names_in_. "
        "Treine o modelo usando DataFrame com nomes de colunas."
    )

NUM_FEATURES = len(FEATURE_NAMES)

def validar_dados(dados):

    if not isinstance(dados, list):
        raise ValueError("Dados devem ser uma lista")

    if len(dados) != NUM_FEATURES:
        raise ValueError(
            f"Esperando {NUM_FEATURES} features"
        )

    for valor in dados:
        if not isinstance(valor, (int, float)):
            raise ValueError("Todas as features devem ser numéricas")


def verificar_integridade_modelo():

    if modelo is None:
        raise RuntimeError("Modelo não carregado")


def detectar_ataque(dados):

    validar_dados(dados)
    verificar_integridade_modelo()

    # cria dataframe com nomes corretos
    df = pd.DataFrame([dados], columns=FEATURE_NAMES)

    pred = modelo.predict(df)[0]
    prob = modelo.predict_proba(df).max()

    label = str(pred)

    return {
        "label": label,
        "risco": int(prob * 100),
        "status": "ANALISANDO"
    }