from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from fastapi import Depends

from src.security import verificar_api_key
from src.core import (
    detectar_ataque,
    validar_dados,
    verificar_integridade_modelo,
    NUM_FEATURES
)

router = APIRouter()

class DadosEntrada(BaseModel):
    dados: list[float]

@router.get("/")
def home():
    return {
        "status":"API online",
        "features_esperadas": NUM_FEATURES
    }

@router.post("/detectar")
def detectar_endpoint(
    entrada: DadosEntrada,
    _: str = Depends(verificar_api_key)
):

    dados = entrada.dados

    validar_dados(dados)
    verificar_integridade_modelo()

    resultado = detectar_ataque(dados)

    return resultado