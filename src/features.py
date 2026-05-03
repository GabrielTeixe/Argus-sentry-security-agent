import pandas as pd
from sklearn.preprocessing import StandardScaler

def preparar_dados(df):
    df = df.dropna()

    colunas_remover = ["Flow ID", "Source IP", "Destination IP"]
    df = df.drop(columns=colunas_remover, errors="ignore")

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df