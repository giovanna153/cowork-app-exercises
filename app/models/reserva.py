from app import db


class Reserva(db.Model):
    # EXERCÍCIO 2: defina as colunas do modelo Reserva.
    # EXERCÍCIO 3: crie o relacionamento com Sala.
 
 
    id = db.Column(db.Integer, primary_key=True)
    sala_id = db.Column(
        db.Integer,
        db.ForeignKey("sala.id"),
        nullable=False
    )

    responsavel = db.Column(db.String(100), nullable=False)

    equipe = db.Column(db.String(100))

    data = db.Column(db.Date, nullable=False)

    hora_inicio = db.Column(db.Time, nullable=False)

    hora_fim = db.Column(db.Time, nullable=False)

    finalidade = db.Column(db.String(255))

    sala = db.relationship("Sala", back_populates ="reservas")

    # EXERCÍCIO 4: defina quais campos podem ser opcionais.
    # EXERCÍCIO 5: confira os nomes da tabela e das colunas antes de create_all().
    # TODO: acrescente as demais colunas e a chave estrangeira para "sala.id".
