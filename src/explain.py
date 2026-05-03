import shap
import numpy as np

def carregar_explainer(model):
    return shap.TreeExplainer(model)

def explicar(explainer,dados):

    dados = np.array(dados).reshape(1, -1)

    shap_values = explainer.shap_values(dados)

    if isinstance(shap_values,list):
        shap_values = shap_values[1]

    valores = np.array(shap_values).flatten()

    resultado = {
        f"feature_{i}": float(v)
        for i,v in enumerate(valores)
    }

    return resultado