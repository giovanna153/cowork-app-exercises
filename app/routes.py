from flask import flash, redirect, render_template, request, url_for

from app import app
from app.forms import ReservaForm, SalaForm
from app.services.reserva_service import ReservaService
from app.services.sala_service import SalaService

sala_service = SalaService()
reserva_service = ReservaService()


@app.route("/")
def home():
    return "Sistema de reservas de salas"

@app.route("/salas")
def listar_salas():
    # ETAPA DE ROTAS: liste as salas usando SalaService.
    salas = sala_service.listar()
    return render_template("salas/listar.html", salas=salas)



@app.route("/salas/nova", methods=["GET", "POST"])
def nova_sala():
    # ETAPA DE ROTAS: crie SalaForm, valide e salve uma sala.
    pass


@app.route("/salas/<int:sala_id>/editar", methods=["GET", "POST"])
def editar_sala(sala_id):
    # ETAPA DE ROTAS: busque, preencha, valide e atualize uma sala.
    pass


@app.post("/salas/<int:sala_id>/excluir")
def excluir_sala(sala_id):
    # ETAPA DE ROTAS: implemente a remoção de uma sala.
    pass


@app.route("/reservas")
def listar_reservas():
    # ETAPA DE ROTAS: liste todas as reservas.
    pass


@app.route("/reservas/nova", methods=["GET", "POST"])
def nova_reserva():
    # ETAPA DE ROTAS: configure as choices do campo sala_id e salve a reserva.
    # Antes de salvar, use verificar_conflito().
    pass


@app.route("/reservas/<int:reserva_id>/editar", methods=["GET", "POST"])
def editar_reserva(reserva_id):
    # ETAPA DE ROTAS: implemente a edição e a validação de conflito.
    pass


@app.post("/reservas/<int:reserva_id>/excluir")
def excluir_reserva(reserva_id):
    # ETAPA DE ROTAS: implemente o cancelamento da reserva.
    pass
