from app import db


class Reserva(db.Model):
    # EXERCÍCIO 1: defina as colunas do modelo Reserva.
    # Crie também o relacionamento com Sala.
    __tablename__ = "reservas"
    id = db.Column(db.Integer, primary_key=True)

    # TODO: acrescente as demais colunas e a chave estrangeira.
