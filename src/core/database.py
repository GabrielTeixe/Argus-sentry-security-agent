import sqlite3

conn = sqlite3.connect("argus.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS incidents(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    label TEXT,
    risco INTEGER,
    status TEXT
)
""")

conn.commit()


def salvar_incidente(timestamp, label, risco, status):
    cursor.execute(
        "INSERT INTO incidents(timestamp,label,risco,status) VALUES(?,?,?,?)",
        (timestamp, label, risco, status)
    )
    conn.commit()