from flask import flash, redirect, render_template, request, url_for

from app import app
from app.forms import ReservaForm, SalaForm
from app.services.reserva_service import ReservaService
from app.services.sala_service import SalaService

sala_service = SalaService()
reserva_service = ReservaService()


@app.route("/")
def home():
    salas = sala_service.listar()
    reservas = reserva_service.listar
    
    resumo = {
        "hoje": 0,
        "total": len(reservas),
        "proximas": reservas
    }

    return render_template("index.html", salas=salas)

@app.route("/salas")
def listar_salas():
    # ETAPA DE ROTAS: liste as salas usando SalaService.
    salas = sala_service.listar()
    return render_template("salas.html", salas=salas)



@app.route("/salas/nova", methods=["GET", "POST"])
def nova_sala():
    # ETAPA DE ROTAS: crie SalaForm, valide e salve uma sala.
    form = SalaForm()

    if form.validate_on_submit():
        sala = sala_service.salvar(form)

        if sala:
            flash("Sala cadastrada com sucesso!", "success")
            return redirect(url_for("listar_salas"))

    return render_template("sala_form.html", form=form)
        

@app.route("/salas/<int:sala_id>/editar", methods=["GET", "POST"])
def editar_sala(sala_id):
    # ETAPA DE ROTAS: busque, preencha, valide e atualize uma sala.

    sala = sala_service.buscar_por_id(sala_id)

    if sala is None:
        flash("Sala não encontrada.", "warning")
        return redirect(url_for("listar_salas"))

    form = SalaForm(obj=sala)

    if form.validate_on_submit():
        sala_atualizada = sala_service.atualizar(sala, form)

        if sala_atualizada:
            flash("Sala atualizada com sucesso!", "success")
            return redirect(url_for("listar_salas"))

        flash("Não foi possível atualizar a sala.", "danger")

    return render_template("sala_form.html", form=form)
        


@app.post("/salas/<int:sala_id>/excluir")
def excluir_sala(sala_id):
    sala = sala_service.buscar_por_id(sala_id)

    if sala is None:
        flash("Sala não encontrada.", "warning")
        return redirect(url_for("listar_salas"))

    if sala.reservas:
        flash(
            "Não é possível excluir uma sala que possui reservas.",
            "warning"
        )
        return redirect(url_for("listar_salas"))

    removida = sala_service.remover(sala)

    if removida:
        flash("Sala excluída com sucesso!", "success")
    else:
        flash("Não foi possível excluir a sala.", "danger")

    return redirect(url_for("listar_salas"))

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
