# Exercício — Sistema de Reservas de Salas

Esta é uma versão inicial do projeto de Coworking. Ela contém a estrutura de um projeto Flask, mas possui lacunas para serem implementadas seguindo a lista de exercícios `lista_exercicios_coworking.docx`.

## Execução

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python run.py
```

## Ordem sugerida

1. `app/models/`: crie `Sala`, `Reserva` e o relacionamento entre elas;
2. `app/forms/`: crie `SalaForm` e `ReservaForm` com validações;
3. `app/services/`: implemente as operações de banco e o conflito de horários;
4. `app/routes.py`: implemente as rotas usando os serviços e os formulários;
5. `app/templates/`: complete `sala_form.html` e `reserva_form.html`;
6. Teste o fluxo completo no navegador.

Não implemente autenticação, autorização ou blueprints nesta atividade.
