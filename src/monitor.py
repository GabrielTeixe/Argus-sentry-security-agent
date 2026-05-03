import random
import time
import sqlite3
from src.predict import detectar_ataque
from sklearn.ensemble import IsolationForest
import numpy as np

conn = sqlite3.connect("logs.db")
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT,
    risco REAL,
    adversarial INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

def salvar_log(status, risco, adversarial):
    c.execute("INSERT INTO logs (status, risco, adversarial) VALUES (?, ?, ?)",
              (status, risco, adversarial))
    conn.commit()

X_normal = np.random.rand(1000, 78)  # logs normais simulados
iso = IsolationForest(contamination=0.01, random_state=42)
iso.fit(X_normal)

def validar_adversarial(log):

    pred = iso.predict([log])
    return pred[0]  # 1 = normal, -1 = anomalia

def enviar_alerta(email):
    print(f"[ALERTA] {email}")


ataques_detectados = 0
total_logs = 0

while True:
    log = [random.random() for _ in range(78)]
    total_logs += 1

    adversarial = validar_adversarial(log)
    resultado = detectar_ataque(log)

    if resultado['status'] == "ataque":
        ataques_detectados += 1

    if resultado['risco'] > 90 or adversarial == -1:
        enviar_alerta(f"Possível ataque detectado! Verifique imediatamente. Status: {resultado['status']} | Adversarial: {adversarial}")

    salvar_log(resultado['status'], resultado['risco'], adversarial)

    print(f"[LOG] Total: {total_logs} | Ataques: {ataques_detectados} | Status: {resultado['status']} | Risco: {resultado['risco']}% | Anomalia: {adversarial}")

    time.sleep(1)