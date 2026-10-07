from sqlalchemy import select

from app import db
from app.models import Sala


class SalaService:

    @staticmethod
    def listar():
        return Sala.query.all()

    @staticmethod
    def buscar_por_id(sala_id):
        return db.session.get(Sala, sala_id)

    @staticmethod
    def salvar(formulario):
        sala = Sala()

        formulario.populate_obj(sala)

        try:
            db.session.add(sala)
            db.session.commit()
            return sala

        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def atualizar(sala, formulario):
        formulario.populate_obj(sala)

        try:
            db.session.commit()
            return sala

        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def remover(sala):
        try:
            db.session.delete(sala)
            db.session.commit()
            return True

        except Exception:
            db.session.rollback()
            return False