from pydantic import BaseModel
from typing import Optional, List

class ClienteSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    dia_mes: str
    hora: str

    class Config:
        orm_mode = True

class Servico(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float
    disponivel: bool
    cliente_id: Optional[int]
    cliente: Optional[ClienteSimples]

    class Config:
        orm_mode = True

class Cliente(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    dia_mes: str
    hora: str
    deseja_fazer: str
    servicos: List[Servico] = []
    
    class Config:
        orm_mode = True