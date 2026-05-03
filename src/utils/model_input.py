import pandas as pd

def preparar_input(modelo, dados):
    if hasattr(modelo, "feature_names_in_"):
        return pd.DataFrame([dados], columns=modelo.feature_name_in_)
    return [dados]