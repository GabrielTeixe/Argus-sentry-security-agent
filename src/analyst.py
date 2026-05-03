def gerar_relatorio(resultado):

    return f"""
Ataque Detectado.

Tipo: {resultado['label']}
MITRE: {resultado['mitre_technique']}
Status: {resultado['status']}
Risco Estimado: {resultado['risco']}%

Recomendação:
Executar contramedidas automáticas e rastrear origem do incidente.
"""