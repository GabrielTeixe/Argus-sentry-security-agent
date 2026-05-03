MITRE_MAP = {
    "BENIGN": {"technique": None, "description": "Tráfego normal"},
    "DDoS": {"technique": "T1498", "description": "Network Denial of Service"},
    "PortScan": {"technique": "T1046", "description": "Network Service Discovery"},
    "BruteForce": {"technique": "T1110", "description": "Credential Access"}
}

def obter_mitre(label):
    return MITRE_MAP.get(label, {
        "technique": "UNKNOWN",
        "description": "Ataque desconhecido"
    })