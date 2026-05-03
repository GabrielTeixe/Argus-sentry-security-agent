from pydantic import BaseModel
from typing import List

class DadosEntrada(BaseModel):
    dados: List[float]