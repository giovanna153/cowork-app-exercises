from app import db


class Sala(db.Model):
    # EXERCÍCIO 1: defina as colunas do modelo Sala.
    # EXERCÍCIO 4: defina quais campos podem ser opcionais.
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable= False)
    capacidade = db.Column(db.Integer, nullable =False)
    descricao = db.Column(db.String(255))
    disponivel = db.Column(db.Boolean, nullable=False, default=True) # descrição
    reservar = db.relationship("Reserva", back_populates = "sala")

    # Sugestão: id, nome, tipo, capacidade, descricao e disponivel.
    id = db.Column(db.Integer, primary_key=True)

    # TODO: acrescente as demais colunas.
