from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from App.src.infra.sqlalchemy.config.database import Base

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    dia_mes = Column(String)
    hora = Column(String)
    deseja_fazer = Column(String)

    servicos = relationship('Servico', back_populates='cliente')

class Servico(Base):
    __tablename__ = 'servico'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    cliente_id = Column(Integer, ForeignKey('cliente.id', name = 'fk_cliente'))

    cliente = relationship('Cliente', back_populates='servicos')