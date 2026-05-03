from fastapi import FastAPI
from src.api import router
import threading

from src.agent.autonomous_agent import (
    iniciar_agente,
    parar_agente
)

app = FastAPI()

app.include_router(router)

thread_agente = None


@app.on_event("startup")
def iniciar_sistema():
    global thread_agente

    print("Argus Sentry Online")

    thread_agente = threading.Thread(
        target=iniciar_agente,
        daemon=True
    )

    thread_agente.start()


@app.on_event("shutdown")
def encerrar_sistema():
    print("Encerrando Argus Agent...")
    parar_agente()