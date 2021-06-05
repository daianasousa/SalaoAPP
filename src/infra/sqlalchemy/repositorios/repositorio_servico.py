from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session, query
from App.src.schemas import schemas
from App.src.infra.sqlalchemy.models import models


class RepositorioServico():

    def __init__(self, db: Session):
        self.session = db

    def criar(self, servico: schemas.Servico):
        db_servico = models.Servico(nome=servico.nome,
                                    preco=servico.preco,
                                    disponivel=servico.disponivel,
                                    cliente_id=servico.cliente_id
                                    )
        self.session.add(db_servico)
        self.session.commit()
        self.session.refresh(db_servico)
        return db_servico

    def listar(self):
        query = select(models.Servico)
        servicos = self.session.execute(query).scalars().all()
        return servicos

    def buscarPorId(self, id: int):
        consulta = select(models.Servico).where(models.Servico.id == id)
        servico = self.session.execute(consulta).scalars().first()
        return servico

    def listar_meus_servico_por_cliente_id(self, client_id: int):
        localizar_cliente = select(models.Servico).where(models.Servico.cliente_id == client_id)
        resultado = self.session.execute(localizar_cliente).scalars().all()
        return resultado

    def editar(self, id: int, servico: schemas.Servico):
        update_stmt = update(models.Servico).where(
            models.Servico.id == id).values(nome=servico.nome,
                                            preco=servico.preco,
                                            disponivel=servico.disponivel,
                                            cliente_id=servico.cliente_id
                                            )
        self.session.execute(update_stmt)
        self.session.commit()

    def remover(self, id: int):
        delete_stmt = delete(models.Servico).where(
            models.Servico.id == id
        )

        self.session.execute(delete_stmt)
        self.session.commit()