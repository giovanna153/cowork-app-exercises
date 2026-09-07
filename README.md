# Exercício — Sistema de Reservas de Salas

Esta é uma versão inicial do projeto de Coworking. Ela contém a estrutura de um projeto Flask, mas possui lacunas para serem implementadas.

As questões completas estão em [QUESTOES.md](QUESTOES.md).

## Instalação e execução

### Pré-requisitos

- Python 3.10 ou superior instalado e disponível no terminal;
- acesso a um terminal (Bash/Zsh no Linux e macOS ou PowerShell no Windows).

Clone ou baixe este repositório e entre na pasta do projeto antes de executar os
comandos abaixo.

### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask run --debug
```

Se o comando `python3` não estiver disponível, instale o Python e o módulo de
ambientes virtuais pela distribuição Linux. No Ubuntu/Debian, por exemplo:

```bash
sudo apt update
sudo apt install python3 python3-venv
```

### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask run --debug
```

Caso o Python não esteja instalado, instale-o pelo [site oficial do
Python](https://www.python.org/downloads/) ou pelo Homebrew (`brew install
python`).

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
flask run --debug
```

Se o PowerShell bloquear a ativação do ambiente virtual, execute uma vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Em seguida, abra o terminal novamente e repita os comandos de ativação.

### Windows (Prompt de Comando)

```bat
py -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
flask run --debug
```

### Acessar a aplicação

Com o servidor em execução, abra <http://127.0.0.1:5000> no navegador. Para
encerrar o servidor, pressione `Ctrl+C`. Para sair do ambiente virtual, use:

```bash
deactivate
```

O banco SQLite é criado automaticamente em `instance/coworking.sqlite3` na
primeira execução.

## Ordem sugerida

A numeração oficial é a da lista de exercícios em Pages:

1. Exercícios 1 a 5 — `app/models/`: crie `Sala`, `Reserva` e o relacionamento
   entre elas;
2. Exercícios 6 a 10 — `app/forms/`: crie `SalaForm` e `ReservaForm` com
   choices e validações;
3. Etapa de serviços — `app/services/`: implemente as operações de banco;
4. Etapa de regras de negócio — implemente a detecção de conflitos de horários;
5. Etapa de rotas — `app/routes.py`: use os serviços e formulários;
6. Etapa de templates — complete `sala_form.html` e `reserva_form.html`;
7. Teste o fluxo completo no navegador.

Não implemente autenticação, autorização ou blueprints nesta atividade.
