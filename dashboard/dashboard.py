import streamlit as st
import sqlite3
import pandas as pd
import time

st.set_page_config(page_title="Dashboard AI Cybersecurity Detector")
st.title("AI Cybersecurity Detector")

conn = sqlite3.connect("logs.db")
placeholder_stats = st.empty()
placeholder_table = st.empty()

while True:
    df = pd.read_sql_query("SELECT * FROM logs ORDER BY timestamp DESC LIMIT 50", conn)

    total_logs = len(df)
    ataques = len(df[df['status']=='ataque'])
    risco_medio = df['risco'].mean() if total_logs > 0 else 0

    placeholder_stats.text(f"Total logs: {total_logs} | Ataques detectados: {ataques} | Risco médio: {risco_medio:.2f}%")
    placeholder_table.dataframe(df)

    time.sleep(1)
