from sqlalchemy import select, update
from sqlalchemy.orm import Session, query
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioCliente():
    
    def __init__(self, session: Session):
        self.session = session

    def agendamento(self, cliente: schemas.Cliente):
        cliente_bd = models.Cliente(nome=cliente.nome,
                                    telefone=cliente.telefone,
                                    dia_mes=cliente.dia_mes,
                                    hora=cliente.hora,
                                    deseja_fazer=cliente.deseja_fazer
                                    )
        self.session.add(cliente_bd)
        self.session.commit()
        self.session.refresh(cliente_bd)
        return cliente_bd

    def listar(self):
        stmt = select(models.Cliente)
        clientes = self.session.execute(stmt).scalars().all()
        return clientes

    def editar(self, id: int, cliente: schemas.Cliente):
        update_stmt = update(models.Cliente).where(
            models.Cliente.id == id).values(nome=cliente.nome,
                                            telefone=cliente.telefone,
                                            dia_mes=cliente.dia_mes,
                                            hora=cliente.hora,
                                            deseja_fazer=cliente.deseja_fazer)
        self.session.execute(update_stmt)
        self.session.commit()

    def buscarPorId(self, id: int):
        consul = select(models.Cliente).where(models.Cliente.id == id)
        clientes = self.session.execute(consul).scalars().first()
        return clientes