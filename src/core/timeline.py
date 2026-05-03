from src.core.database import cursor
from src.core.mitre import obter_mitre

def obter_timeline():

    cursor.execute("""
        SELECT timestamp, label, risco, status
        FROM incidents
        ORDER BY id DESC
        LIMIT 50
    """)

    registros = cursor.fetchall()

    timeline = []

    for r in registros:

        mitre = obter_mitre(r[1])

        timeline.append({
            "timestamp": r[0],
            "attack": r[1],
            "risk": r[2],
            "status": r[3],
            "mitre": mitre["technique"],
            "description": mitre["description"]
        })

    return timeline