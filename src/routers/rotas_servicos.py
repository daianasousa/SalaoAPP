from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Servico
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_servico \
    import RepositorioServico

router = APIRouter()

@router.post('/servico',
             status_code=status.HTTP_201_CREATED,
            response_model=Servico)

def criar_servico(servico: Servico, db: Session = Depends(get_db)):
    servico_criado = RepositorioServico(db).criar(servico)
    return servico_criado

@router.get('/servico', response_model=List[Servico])
def listar_servico(db: Session = Depends(get_db)):
    servicos = RepositorioServico(db).listar()
    return servicos

@router.get('/servico/{id}')
def exibir_servico(id: int, session: Session = Depends(get_db)):
    servico_localizado = RepositorioServico(session).buscarPorId(id)
    if not servico_localizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Serviço com o ID {id} não encontrado')
    return servico_localizado

@router.get('/servico/{id}/servico', response_model=List[Servico])
def listar_servico_id(id: int, session: Session = Depends(get_db)):
    servicos = RepositorioServico(session).listar_meus_servico_por_cliente_id(id)
    if not  servicos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Cliente {id} não localizado')
    return servicos

@router.put('/servico/{id}', response_model=Servico)
def atualizar_servico(id: int, servico: Servico, 
                  session: Session = Depends(get_db)):
    RepositorioServico(session).editar(id, servico)
    servico.id = id
    servico_atualizado = RepositorioServico(session).buscarPorId(id)
    if not servico_atualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Serviço com o ID {id} não encontrado')
    return servico

@router.delete('/servico/{id}')
def excluir_servico(id: int, session: Session = Depends(get_db)):
    servico_localizado = RepositorioServico(session).buscarPorId(id)
    if not servico_localizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Servico com o ID {id} não encontrado')

    RepositorioServico(session).remover(id)
    return {"msg": "Removido com sucesso"}