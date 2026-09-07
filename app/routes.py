from flask import flash, redirect, render_template, request, url_for

from app import app
from app.forms import ReservaForm, SalaForm
from app.services.reserva_service import ReservaService
from app.services.sala_service import SalaService

sala_service = SalaService()
reserva_service = ReservaService()


@app.route("/")
def home():
    # EXERCÍCIO 6: mostre o resumo e as próximas reservas no dashboard.
    pass


@app.route("/salas")
def listar_salas():
    # EXERCÍCIO 6: liste as salas usando SalaService.
    pass


@app.route("/salas/nova", methods=["GET", "POST"])
def nova_sala():
    # EXERCÍCIO 6: crie SalaForm, valide e salve uma sala.
    pass


@app.route("/salas/<int:sala_id>/editar", methods=["GET", "POST"])
def editar_sala(sala_id):
    # EXERCÍCIO 6: busque, preencha, valide e atualize uma sala.
    pass


@app.post("/salas/<int:sala_id>/excluir")
def excluir_sala(sala_id):
    # EXERCÍCIO 6: implemente a remoção de uma sala.
    pass


@app.route("/reservas")
def listar_reservas():
    # EXERCÍCIO 7: liste todas as reservas.
    pass


@app.route("/reservas/nova", methods=["GET", "POST"])
def nova_reserva():
    # EXERCÍCIO 7: configure as choices do campo sala_id e salve a reserva.
    # Antes de salvar, use verificar_conflito().
    pass


@app.route("/reservas/<int:reserva_id>/editar", methods=["GET", "POST"])
def editar_reserva(reserva_id):
    # EXERCÍCIO 7: implemente a edição e a validação de conflito.
    pass


@app.post("/reservas/<int:reserva_id>/excluir")
def excluir_reserva(reserva_id):
    # EXERCÍCIO 7: implemente o cancelamento da reserva.
    pass
