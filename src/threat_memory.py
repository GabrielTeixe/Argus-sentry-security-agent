import sqlite3
from datetime import datetime

conn = sqlite3.connect("threat_memory.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ataques(
    ip TEXT,
    label,TEXT,
    timestamp TEXT
)
""")

def registrar_ataque(ip,label):
    cursor.execute(
        "INSERT INTO ataques VALUE (?,?,?)",
        (ip, label, datetime.utcnow().isoformat())
    )
    conn.commit()

def contar_ataques(ip):
    cursor.execute(
        "SELECT COUNT(*) FROM ataques WHERE ip=?",
        (ip,)
    )
    return cursor.fetchone()[0]