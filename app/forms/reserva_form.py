from datetime import date

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DateField,
    TimeField,
    SubmitField
)
from wtforms.validators import DataRequired, Length, ValidationError


class ReservaForm(FlaskForm):

    responsavel = StringField(
        "Responsável",
        validators=[
            DataRequired(message="Informe o responsável."),
            Length(
                max=100,
                message="O responsável deve ter no máximo 100 caracteres."
            )
        ]
    )

    equipe = StringField(
        "Equipe",
        validators=[
            Length(
                max=100,
                message="A equipe deve ter no máximo 100 caracteres."
            )
        ]
    )

    sala_id = SelectField(
        "Sala",
        coerce=int,
        validators=[
            DataRequired(message="Selecione uma sala.")
        ]
    )

    data = DateField(
        "Data",
        format="%d/%m/%Y",
        validators=[
            DataRequired(message="Informe a data.")
        ]
    )

    hora_inicio = TimeField(
        "Hora de início",
        format="%H:%M",
        validators=[
            DataRequired(message="Informe a hora de início.")
        ]
    )

    hora_fim = TimeField(
        "Hora de fim",
        format="%H:%M",
        validators=[
            DataRequired(message="Informe a hora de fim.")
        ]
    )

    finalidade = StringField(
        "Finalidade",
        validators=[
            Length(
                max=255,
                message="A finalidade deve ter no máximo 255 caracteres."
            )
        ]
    )

    submit = SubmitField("Salvar")

    def validate_data(self, field):
        if field.data and field.data < date.today():
            raise ValidationError(
                "A data não pode ser anterior à data atual."
            )

    def validate_hora_fim(self, field):
        if (
            field.data
            and self.hora_inicio.data
            and field.data <= self.hora_inicio.data
        ):
            raise ValidationError(
                "A hora de fim deve ser posterior à hora de início."
            )