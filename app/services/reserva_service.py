from sqlalchemy import select

from app import db
from app.models import Reserva


class ReservaService:

    @staticmethod
    def listar():
        return Reserva.query.all()

    @staticmethod
    def buscar_por_id(reserva_id):
        return db.session.get(Reserva, reserva_id)

    @staticmethod
    def salvar(formulario):
        reserva = Reserva()

        formulario.populate_obj(reserva)

        try:
            db.session.add(reserva)
            db.session.commit()
            return reserva

        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def atualizar(reserva, formulario):
        formulario.populate_obj(reserva)

        try:
            db.session.commit()
            return reserva

        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def remover(reserva):
        try:
            db.session.delete(reserva)
            db.session.commit()
            return True

        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def verificar_conflito(
        sala_id,
        data,
        hora_inicio,
        hora_fim,
        ignorar_id=None
    ):
        consulta = Reserva.query.filter(
            Reserva.sala_id == sala_id,
            Reserva.data == data,
            Reserva.hora_inicio < hora_fim,
            Reserva.hora_fim > hora_inicio
        )

        if ignorar_id is not None:
            consulta = consulta.filter(
                Reserva.id != ignorar_id
            )

        return consulta.first() is not None