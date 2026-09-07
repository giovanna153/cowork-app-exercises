from app import db


class Reserva(db.Model):
    # EXERCÍCIO 2: defina as colunas do modelo Reserva.
    # EXERCÍCIO 3: crie o relacionamento com Sala.
    id = db.Column(db.Integer, primary_key=True)

    # EXERCÍCIO 4: defina quais campos podem ser opcionais.
    # EXERCÍCIO 5: confira os nomes da tabela e das colunas antes de create_all().
    # TODO: acrescente as demais colunas e a chave estrangeira para "sala.id".
