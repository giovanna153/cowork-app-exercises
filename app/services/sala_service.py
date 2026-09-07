from sqlalchemy import select

from app import db
from app.models import Sala


class SalaService:
    # EXERCÍCIO 4: implemente os métodos abaixo.
    # Use try/except nas operações que alteram o banco, com rollback e False.

    def listar(self):
        pass

    def buscar_por_id(self, sala_id):
        pass

    def salvar(self, formulario):
        pass

    def atualizar(self, sala, formulario):
        pass

    def remover(self, sala):
        pass
