from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Cliente, ClienteSimples
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.repositorio_cliente \
    import RepositorioCliente

#criar_bd()

router = APIRouter()

@router.post('/agendamento', 
                status_code=status.HTTP_201_CREATED, 
                                    response_model=ClienteSimples)

def agendar_h(cliente: Cliente, session: Session = Depends(get_db)):
    agenda_horario = RepositorioCliente(session).agendamento(cliente)
    return agenda_horario

@router.get('/cliente', response_model=List[ClienteSimples])
def listar_agendamentos(session: Session = Depends(get_db)):
    clientes = RepositorioCliente(session).listar()
    return clientes

@router.put('/cliente/{id}', response_model=ClienteSimples)
def atualizar_agendamento(id: int, cliente: Cliente, 
                                            session: Session = Depends(get_db)):
    RepositorioCliente(session).editar(id, cliente)
    cliente.id = id
    cliente_localizado = RepositorioCliente(session).buscarPorId(id)
    if not cliente_localizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Cliente com o ID {id} não encontrado')
    return cliente     