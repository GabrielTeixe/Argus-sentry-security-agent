import streamlit as st
from src.predict import detectar_ataque
import random
import time

st.title("AI Cybersecurity Detector")
st.markdown("Logs de ataque em tempo real")

log_area = st.empty()
risco_area = st.empty()
contador_area = st.empty()

contador = 0
while True:
    log = [random.random() for _ in range(78)]
    resultado = detectar_ataque(log)

    contador += 1
    log_area.text(f"Ultimo log: {log}")
    risco_area.text(f"Status: {resultado['status']} | Risco: {resultado['risco']}%")
    contador_area.text(f"Logs processados: {contador}")

    time.sleep(1)