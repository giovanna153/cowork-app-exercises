from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    IntegerField,
    BooleanField,
    SubmitField
)
from wtforms.validators import DataRequired, Length, NumberRange


class SalaForm(FlaskForm):

    nome = StringField(
        "Nome",
        validators=[
            DataRequired(message="Informe o nome da sala."),
            Length(max=100, message="O nome deve ter no máximo 100 caracteres.")
        ]
    )

    tipo = SelectField(
        "Tipo",
        choices=[
            ("reuniao", "Sala de reunião"),
            ("estacao", "Estação de trabalho"),
            ("auditorio", "Auditório")
        ],
        validators=[
            DataRequired(message="Selecione o tipo da sala.")
        ]
    )

    capacidade = IntegerField(
        "Capacidade",
        validators=[
            DataRequired(message="Informe a capacidade."),
            NumberRange(
                min=1,
                message="A capacidade deve ser maior que zero."
            )
        ]
    )

    descricao = StringField(
        "Descrição",
        validators=[
            Length(
                max=255,
                message="A descrição deve ter no máximo 255 caracteres."
            )
        ]
    )

    disponivel = BooleanField("Disponível")

    submit = SubmitField("Salvar")