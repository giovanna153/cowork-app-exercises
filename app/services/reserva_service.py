from sqlalchemy import select

from app import db
from app.models import Reserva


class ReservaService:
    # EXERCÍCIO 4: implemente CRUD para reservas.

    def listar(self):
        pass

    def buscar_por_id(self, reserva_id):
        pass

    def verificar_conflito(self, sala_id, data, hora_inicio, hora_fim, ignorar_id=None):
        # EXERCÍCIO 5: detecte reservas sobrepostas no mesmo dia e sala.
        pass

    def salvar(self, formulario):
        pass

    def atualizar(self, reserva, formulario):
        pass

    def remover(self, reserva):
        pass
