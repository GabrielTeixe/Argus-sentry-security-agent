from datetime import datetime
import json
from pathlib import Path

LOG_PATH = Path("logs/incidents.jsonl")

LOG_PATH.parent.mkdir(exist_ok=True)

def registrar_incidente(resultado: dict):

    incidente = {
        "timestamp": datetime.utcnow().isoformat(),
        **resultado
    }

    with open(LOG_PATH,"a") as f:
        f.write(json.dumps(incidente)+ "\n")

        print("Incidente registrado")