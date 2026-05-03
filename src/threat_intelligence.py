MITRE_MAP = {
    "BENIGN": {
        "technique": None,
        "description": "Tráfego normal"
    },
    "DoS": {
        "technique": "T1499",
        "description": "Endpoint Denial of Service"
    },
    "DDoS": {
        "technique": "T1498",
        "description": "Network Denial of Service"
    },
    "PortScan": {
        "technique": "T1046",
        "description": "Network Service Discovery"
    },
    "BruteForce": {
        "technique": "T1110",
        "description": "Brute Force"
    },
    "WebAttack": {
        "technique": "T1190",
        "description": "Exploit Public-Facing Application"
    }
}

def obter_mitre(label):
    return MITRE_MAP.get(label, {
        "technique": "UNKNOWN",
        "description": "Ataque desconhecido"
    })