from app import db


class Sala(db.Model):
    # EXERCÍCIO 1: defina as colunas do modelo Sala.
    # EXERCÍCIO 4: defina quais campos podem ser opcionais.
    # Sugestão: id, nome, tipo, capacidade, descricao e disponivel.
    __tablename__ = "salas"
    id = db.Column(db.Integer, primary_key=True)

    # TODO: acrescente as demais colunas.
