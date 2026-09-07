# Lista de exercícios — Flask

## Instruções

Use a estrutura básica deste projeto Flask como base.

1. Crie e ative um ambiente virtual.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Abra a pasta do projeto no Visual Studio Code.
4. Mantenha a separação entre `models`, `forms`, `services`, `routes` e `templates`.
5. Implemente cada exercício de forma incremental.
6. Teste cada funcionalidade antes de prosseguir para o próximo exercício.

Não implemente autenticação, autorização ou blueprints nesta atividade.

## Preparação do ambiente

### Pré-requisitos

Você precisa ter:

- Python 3.10 ou superior;
- acesso a um terminal;
- Visual Studio Code ou outro editor de código;
- um navegador para testar a aplicação.

Faça o download ou clone o projeto e entre na pasta raiz antes de executar os comandos abaixo. A pasta correta é aquela que contém `requirements.txt`, `run.py`, `app/` e `config.py`.

### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
flask run --debug
```

Se `python3` ou o módulo de ambientes virtuais não estiver disponível, instale o Python e o pacote de ambientes virtuais da sua distribuição. No Ubuntu/Debian, por exemplo:

```bash
sudo apt update
sudo apt install python3 python3-venv
```

### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
flask run --debug
```

Se o Python não estiver instalado, instale-o pelo [site oficial do Python](https://www.python.org/downloads/) ou pelo Homebrew:

```bash
brew install python
```

### Windows — PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
flask run --debug
```

Se o PowerShell impedir a ativação do ambiente virtual, execute uma vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Depois, abra o terminal novamente e repita a ativação.

### Windows — Prompt de Comando

```bat
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
flask run --debug
```

### Acessar e encerrar a aplicação

Com o servidor em execução, abra <http://127.0.0.1:5000> no navegador. Para encerrar o servidor, pressione `Ctrl+C` no terminal.

Para sair do ambiente virtual depois de encerrar o servidor, execute:

```bash
deactivate
```

O comando `flask run --debug` reinicia automaticamente o servidor quando arquivos Python são alterados. O modo de depuração deve ser usado somente durante o desenvolvimento local.

### Banco SQLite durante os exercícios

O banco é criado automaticamente em:

```text
instance/coworking.sqlite3
```

O diretório `instance/` é criado pela aplicação na primeira execução. Os dados cadastrados permanecem no arquivo mesmo depois de parar e iniciar o servidor novamente.

Durante os exercícios iniciais, alterações nas colunas ou nos relacionamentos não atualizam automaticamente um banco SQLite já existente. Se o esquema precisar ser recriado:

1. encerre o servidor;
2. faça uma cópia de segurança de `instance/coworking.sqlite3`, caso queira preservar os dados;
3. remova somente o arquivo `instance/coworking.sqlite3`;
4. inicie a aplicação novamente para que `db.create_all()` crie as tabelas atuais.

Não remova a pasta inteira do projeto nem outros arquivos. Em uma aplicação real, alterações de esquema devem ser controladas com migrações; nesta atividade, o banco é recriado apenas para facilitar os exercícios iniciais.

## Sistema de reservas de salas — coworking

Construa, de forma incremental, uma aplicação web para cadastrar salas e registrar reservas de espaços compartilhados.

Uma reserva deve indicar a sala, o responsável, a data, o horário e a finalidade do uso.

## Roteiro de implementação

Implemente os exercícios na ordem abaixo. Não avance para a próxima fase enquanto o ponto de verificação da fase atual não estiver funcionando.

### Fase 0 — Preparação

Antes do Exercício 1:

1. crie e ative o ambiente virtual;
2. instale as dependências;
3. execute a aplicação inicial;
4. confirme que o servidor inicia sem erro. Nesta fase, as rotas ainda estão incompletas e a página inicial será implementada posteriormente.

### Fase 1 — Modelos e banco

Implemente os Exercícios 1 a 5.

Ao concluir, verifique:

- a aplicação inicia sem erro;
- as tabelas `sala` e `reserva` são criadas;
- a chave estrangeira `sala_id` aponta para `sala.id`;
- é possível acessar `reserva.sala` e `sala.reservas`;
- os nomes das tabelas e colunas correspondem ao esquema esperado.

### Fase 2 — Formulários e validações de entrada

Implemente os Exercícios 6 a 10.

Antes de criar as rotas, confira os formulários em isolamento ou por meio de testes simples. Verifique campos obrigatórios, opções do tipo de sala, capacidade inválida, data passada, horário final inválido e mensagens em português.

Nesta fase, valide apenas os dados fornecidos pelo usuário. A consulta de salas para preencher `sala_id` e a verificação de conflitos serão feitas nas fases seguintes.

### Fase 3 — Serviços de persistência

Implemente os Exercícios 11 e 12.

Teste os serviços antes de conectá-los às rotas. Confirme o contrato de retorno, o `commit()` em operações bem-sucedidas e o `rollback()` quando ocorrer uma falha. As rotas ainda não devem conter consultas diretamente ao banco.

### Fase 4 — Regra de negócio

Implemente o Exercício 13.

Teste `verificar_conflito()` com reservas sobrepostas, horários adjacentes, salas diferentes e edição da própria reserva. A regra deve funcionar no serviço independentemente da validação do formulário.

### Fase 5 — Rotas de salas

Implemente o Exercício 14.

Teste o fluxo completo de salas: cadastrar, listar, editar e tentar excluir uma sala com e sem reservas. Confirme as mensagens e os redirecionamentos.

### Fase 6 — Rotas de reservas

Implemente o Exercício 15.

Teste o fluxo completo de reservas: criar, listar, editar e cancelar. Confirme o preenchimento das salas, a ordenação da agenda, a validação de conflito e a preservação dos dados quando houver erro.

### Fase 7 — Templates

Implemente o Exercício 16. Complete os templates usados pelas rotas, renderize os erros de validação, mantenha os valores preenchidos na edição e preserve o token CSRF nos formulários POST.

### Fase 8 — Integração final

Depois de concluir todas as fases:

- execute o fluxo completo pelo navegador;
- teste entradas válidas e inválidas;
- confirme que os erros aparecem sem apagar os dados digitados;
- reinicie a aplicação e verifique se os dados persistem no SQLite;
- revise se cada camada continua respeitando sua responsabilidade.

## Critérios de aceitação

Use os critérios abaixo para verificar cada exercício antes de avançar.

### Exercício 1

- A classe `Sala` herda de `db.Model`.
- A tabela criada se chama `sala`.
- O modelo possui chave primária inteira `id`.
- Os campos de nome, tipo, capacidade, descrição e disponibilidade possuem tipos compatíveis com o esquema.

### Exercício 2

- A classe `Reserva` herda de `db.Model`.
- A tabela criada se chama `reserva`.
- A data usa `Date`.
- Os horários usam `Time`.
- Os campos textuais usam `String`.

### Exercício 3

- `Reserva.sala_id` referencia `sala.id`.
- `reserva.sala` retorna a sala associada.
- `sala.reservas` retorna as reservas da sala.
- A aplicação cria os modelos sem erro de relacionamento.

### Exercício 4

- Os campos obrigatórios rejeitam valores nulos no modelo.
- `descricao`, `equipe` e `finalidade` podem ficar vazios quando permitido pelo esquema.
- `disponivel` possui valor padrão `True` quando não for informado.
- `capacidade` não aceita valor zero ou negativo na validação correspondente.

### Exercício 5

- Ao iniciar a aplicação, as tabelas `sala` e `reserva` são criadas.
- Os nomes das tabelas e das colunas correspondem ao esquema documentado.
- O banco pode ser consultado sem erro depois da criação.

### Exercício 6

- `SalaForm` herda de `FlaskForm`.
- O formulário possui todos os campos solicitados e um botão de envio.
- O formulário pode ser instanciado sem erro.

### Exercício 7

- O campo `tipo` é um `SelectField`.
- As três opções solicitadas aparecem na interface.
- Cada opção possui valor e texto definidos.

### Exercício 8

- `nome`, `tipo` e `capacidade` rejeitam valores vazios.
- Textos acima do limite definido são rejeitados.
- Capacidade zero ou negativa é rejeitada.
- As mensagens de validação aparecem em português.

### Exercício 9

- `ReservaForm` possui todos os campos solicitados.
- `sala_id` usa `SelectField(coerce=int)`.
- As opções de sala podem ser atribuídas pela rota sem consulta ao banco dentro do formulário.
- O formulário pode ser usado tanto para criação quanto para edição.

### Exercício 10

- Datas são exibidas e interpretadas no formato `%d/%m/%Y`.
- Horários são exibidos e interpretados no formato `%H:%M`.
- Data anterior ao dia atual é rejeitada.
- Horário final menor ou igual ao inicial é rejeitado.
- Mensagens de validação são exibidas em português.
- Os formulários enviados contêm o token CSRF.

### Exercício 11

- `SalaService.listar()` retorna todas as salas ou uma lista vazia.
- `SalaService.buscar_por_id()` retorna a sala ou `None`.
- `salvar()` cria uma sala persistida.
- `atualizar()` altera uma sala existente.
- `remover()` remove uma sala sem reservas quando permitido.
- Erros de escrita não deixam a sessão em estado pendente.

### Exercício 12

- `ReservaService` implementa o CRUD com o mesmo contrato definido na atividade.
- `salvar()` e `atualizar()` usam `populate_obj()`.
- Operações bem-sucedidas executam `commit()`.
- Falhas executam `rollback()` e retornam `False`.
- `buscar_por_id()` retorna `None` quando a reserva não existe.
- Serviços não executam redirecionamentos, renderização ou mensagens flash.

### Exercício 13

- Reservas sobrepostas na mesma sala e data são rejeitadas.
- Reservas adjacentes são permitidas.
- Reservas em salas diferentes são permitidas.
- Reservas em datas diferentes são permitidas.
- A edição não entra em conflito com a própria reserva quando `ignorar_id` é usado.
- `verificar_conflito()` retorna `True` somente quando existe conflito.

### Exercício 14

- O dashboard `/` exibe o resumo e as próximas reservas.
- É possível criar uma sala válida pelo navegador.
- Sala inválida retorna ao formulário com os erros e dados preenchidos.
- A lista de salas exibe os registros persistidos.
- A edição carrega os valores atuais e salva as alterações.
- Sala inexistente recebe tratamento adequado.
- Sala com reservas não é excluída e gera mensagem explicativa.
- Operações concluídas exibem mensagem e redirecionam para uma página adequada.

### Exercício 15

- É possível criar uma reserva válida selecionando uma sala existente.
- As opções de `sala_id` são preenchidas antes da validação do formulário.
- Reserva conflitante permanece no formulário e apresenta mensagem de erro.
- A listagem exibe reservas ordenadas por data e horário.
- A edição mantém as opções de sala e não acusa conflito com a própria reserva.
- Reserva inexistente recebe tratamento adequado.
- O cancelamento exige CSRF e remove a reserva após confirmação.

### Exercício 16

- Os dois formulários exibem todos os campos necessários.
- Cada campo possui um `label` associado.
- Erros são exibidos próximos aos respectivos campos.
- Valores digitados são preservados quando a validação falha.
- Valores atuais são exibidos durante a edição.
- Formulários POST possuem proteção CSRF.
- Os templates continuam herdando de `base.html` e usando os estilos existentes.

### Aceitação do fluxo completo

A atividade será considerada concluída quando:

- o servidor iniciar sem erros;
- salas e reservas puderem ser criadas, listadas, editadas e removidas ou canceladas conforme as regras;
- entradas inválidas forem rejeitadas com mensagens claras;
- conflitos forem bloqueados somente quando realmente houver sobreposição;
- horários adjacentes forem aceitos;
- os dados permanecerem disponíveis após reiniciar a aplicação;
- nenhuma consulta SQL ou operação de transação ficar implementada diretamente nas rotas;
- não houver erro de CSRF nos formulários POST.

## Modelos

Objetivo: representar as salas e as reservas no SQLite.

### Exercício 1 — Modelo `Sala`

Em `app/models/sala.py`, crie a classe `Sala` herdando de `db.Model`. Defina `id` como chave primária e use tipos adequados para nome, tipo, capacidade, descrição e disponibilidade.

### Exercício 2 — Modelo `Reserva`

Em `app/models/reserva.py`, crie a classe `Reserva`. Use `Date` para a data, `Time` para `hora_inicio` e `hora_fim` e `String` para os textos.

### Exercício 3 — Relacionamento entre os modelos

Crie `sala_id` como chave estrangeira para `sala.id`. Configure o relacionamento bidirecional: uma `Sala` possui várias reservas e uma `Reserva` pertence a uma `Sala`.

O relacionamento deve permitir acessar:

- `reserva.sala`;
- `sala.reservas`.

### Exercício 4 — Obrigatoriedade dos campos

Use `nullable=False` nos campos obrigatórios. Considere como opcionais `descricao`, `equipe` e `finalidade`.

### Exercício 5 — Tabelas e criação do banco

Confira os nomes das tabelas e das colunas antes de executar `db.create_all()`.

Ao iniciar a aplicação, as tabelas `sala` e `reserva` devem ser criadas sem erro.

### Esquema esperado dos modelos

Não declare `__tablename__` nos modelos. O Flask-SQLAlchemy deve derivar os nomes das tabelas a partir das classes: `Sala` gera `sala` e `Reserva` gera `reserva`.

#### `Sala` — tabela `sala`

| Campo | Tipo | Obrigatoriedade e regras |
|---|---|---|
| `id` | `Integer` | Chave primária |
| `nome` | `String` | Obrigatório (`nullable=False`) |
| `tipo` | `String` | Obrigatório (`nullable=False`); sala de reunião, estação de trabalho ou auditório |
| `capacidade` | `Integer` | Obrigatório (`nullable=False`) e maior que zero |
| `descricao` | `String` | Opcional |
| `disponivel` | `Boolean` | Obrigatório; valor padrão `True` |

#### `Reserva` — tabela `reserva`

| Campo | Tipo | Obrigatoriedade e regras |
|---|---|---|
| `id` | `Integer` | Chave primária |
| `sala_id` | `Integer` | Chave estrangeira para `sala.id`; obrigatório (`nullable=False`) |
| `responsavel` | `String` | Obrigatório (`nullable=False`) |
| `equipe` | `String` | Opcional |
| `data` | `Date` | Obrigatório (`nullable=False`) |
| `hora_inicio` | `Time` | Obrigatório (`nullable=False`) |
| `hora_fim` | `Time` | Obrigatório (`nullable=False`) e posterior ao início |
| `finalidade` | `String` | Opcional |

Configure o relacionamento para que uma sala tenha muitas reservas e uma reserva tenha exatamente uma sala. Uma sala que possui reservas não deve ser excluída: preserve a integridade dos dados e informe o usuário.

## Formulários

Objetivo: validar os dados de entrada antes de enviá-los ao banco. Os formulários devem cuidar da validação dos campos, formatos e mensagens para o usuário; regras que dependem de outras reservas ou do banco serão tratadas nos serviços.

### Exercício 6 — Estrutura do `SalaForm`

Em `app/forms/sala_form.py`, crie `SalaForm` herdando de `FlaskForm`.

Inclua:

- `nome` como `StringField`;
- `tipo` como `SelectField`;
- `capacidade` como `IntegerField`;
- `descricao` como `StringField`;
- `disponivel` como `BooleanField`;
- `submit` como `SubmitField`.

### Exercício 7 — Campos e opções do `SalaForm`

No `SelectField`, use as opções:

- Sala de reunião;
- Estação de trabalho;
- Auditório.

Cada opção deve possuir um valor e um texto. Use os nomes de campo definidos no esquema dos modelos.

### Exercício 8 — Validadores do `SalaForm`

Aplique:

- `DataRequired` em `nome`, `tipo` e `capacidade`;
- `Length` para limitar os textos;
- `NumberRange` para impedir capacidade zero ou negativa.

### Exercício 9 — Estrutura e escolhas do `ReservaForm`

Em `app/forms/reserva_form.py`, crie `ReservaForm` com:

- `responsavel`;
- `equipe`;
- `sala_id`;
- `data`;
- `hora_inicio`;
- `hora_fim`;
- `finalidade`;
- `submit`.

Use `SelectField(coerce=int)` para `sala_id`. As opções serão preenchidas pelas rotas, pois vêm do banco de dados. O formulário não deve consultar o banco diretamente.

### Exercício 10 — Validação da reserva e CSRF

Configure:

- `DateField` com formato `%d/%m/%Y`;
- `TimeField` com formato `%H:%M`;
- mensagens de erro em português;
- `validate_data` para impedir datas anteriores ao dia atual;
- `validate_hora_fim` para exigir que o horário final seja posterior ao inicial.

Inclua `{{ form.hidden_tag() }}` nos templates para enviar o token CSRF.

Os formulários devem validar os dados básicos de entrada. A validação do formulário não substitui a validação da regra de conflito no serviço.

## Serviços

Objetivo: concentrar o acesso ao banco nas classes de serviço. As rotas devem orquestrar o fluxo HTTP, mas não devem conter consultas SQL ou detalhes de `db.session`.

### Exercício 11 — `SalaService`

Em `SalaService`, implemente:

- `listar()`;
- `buscar_por_id(sala_id)`;
- `salvar(formulario)`;
- `atualizar(sala, formulario)`;
- `remover(sala)`.

### Exercício 12 — `ReservaService` e contrato dos serviços

Em `ReservaService`, implemente os mesmos métodos para a entidade `Reserva`.

Nos métodos `salvar` e `atualizar`:

- receba o formulário;
- use `formulario.populate_obj(objeto)` para copiar os campos;
- confirme a transação com `db.session.commit()`;
- retorne o objeto salvo ou atualizado em caso de sucesso.

Adote o seguinte contrato:

| Método | Retorno em sucesso | Retorno em falha ou ausência |
|---|---|---|
| `listar()` | Lista de entidades | Lista vazia quando não houver registros |
| `buscar_por_id(id)` | Entidade encontrada | `None` |
| `salvar(formulario)` | Entidade salva | `False` |
| `atualizar(entidade, formulario)` | Entidade atualizada | `False` |
| `remover(entidade)` | `True` | `False` |
| `verificar_conflito(...)` | `True` quando houver conflito | `False` quando não houver conflito |

Nas operações de escrita:

- use `try/except` para tratar erros do banco;
- execute `db.session.rollback()` em caso de erro;
- não deixe uma transação parcialmente concluída;
- registre ou disponibilize o erro para depuração sem expor detalhes técnicos ao usuário final.

Os serviços não devem executar `flash()`, `redirect()` ou `render_template()`. Essas responsabilidades pertencem às rotas.

## Regra de negócio — conflito de horários

### Exercício 13 — Detecção de reservas sobrepostas

Crie `verificar_conflito(sala_id, data, hora_inicio, hora_fim, ignorar_id=None)` em `ReservaService`.

A consulta deve considerar somente reservas:

- da mesma sala;
- da mesma data;
- diferentes de `ignorar_id`, quando esse valor for informado.

Dois intervalos se sobrepõem quando:

```text
reserva_existente.hora_inicio < nova.hora_fim
e
reserva_existente.hora_fim > nova.hora_inicio
```

Assim, uma reserva termina antes de outra começar sem gerar conflito. Horários adjacentes são permitidos.

Ao editar, use `ignorar_id` para que a reserva atual não entre em conflito com ela mesma.

O serviço deve proteger essa regra independentemente da validação do formulário, pois a regra depende de outros registros do banco.

Teste os seguintes casos:

- uma reserva das 09:00 às 10:00 e outra das 09:30 às 10:30 devem conflitar;
- uma reserva das 09:00 às 10:00 e outra das 09:00 às 10:00 devem conflitar;
- uma reserva das 09:00 às 11:00 e outra das 10:00 às 10:30 devem conflitar;
- uma reserva das 09:00 às 10:00 e outra iniciando exatamente às 10:00 não devem conflitar;
- reservas em salas diferentes não devem conflitar;
- a edição de uma reserva sem alterar seu intervalo não deve gerar conflito consigo mesma.

## Rotas de salas

### Exercício 14 — CRUD de salas

Objetivo: conectar `SalaForm`, `SalaService` e os templates, além de montar o dashboard inicial.

Implemente:

- `GET /`;
- `GET/POST /salas/nova`;
- `GET /salas`;
- `GET/POST /salas/<int:sala_id>/editar`;
- `POST /salas/<int:sala_id>/excluir`.

Requisitos:

- no dashboard, mostre o resumo e as próximas reservas;
- no `GET`, mostre o formulário;
- no `POST`, use `validate_on_submit()`;
- use `sala_service.salvar(form)` e `sala_service.atualizar(...)`;
- use `SalaForm(obj=sala)` para preencher a edição;
- trate `None` quando uma sala não for encontrada;
- se a sala possuir reservas, não a exclua e mostre uma mensagem explicativa;
- use `flash()` para informar sucesso ou erro;
- use `redirect()` após uma operação concluída.

A rota deve interpretar o retorno do serviço, mas não deve implementar novamente as regras ou consultas do serviço.

## Rotas de reservas

### Exercício 15 — CRUD de reservas

Objetivo: conectar `ReservaForm`, `ReservaService` e a lista de salas.

Implemente:

- `GET/POST /reservas/nova`;
- `GET /reservas`;
- `GET/POST /reservas/<int:reserva_id>/editar`;
- `POST /reservas/<int:reserva_id>/excluir`.

Requisitos:

- liste as salas e preencha `form.sala_id.choices` com pares `(id, nome)`;
- preencha as opções antes de chamar `validate_on_submit()`;
- chame `verificar_conflito()` antes de salvar ou atualizar;
- permaneça no formulário e mostre uma mensagem se houver conflito;
- liste as reservas ordenadas por data e horário;
- use `ReservaForm(obj=reserva)` na edição;
- preencha as opções de sala novamente no `GET` e no `POST` da edição;
- trate `None` quando uma reserva não for encontrada;
- use CSRF no formulário de cancelamento.

A rota deve coordenar formulário e serviço. A consulta de conflito e as operações de banco devem permanecer nos serviços.

## Templates

### Exercício 16 — Formulários e mensagens

Objetivo: construir formulários acessíveis e integrados ao Flask-WTF.

Em `sala_form.html`:

- renderize `form.hidden_tag()`;
- renderize cada campo do `SalaForm`;
- renderize o botão de envio;
- mostre os erros de cada campo.

Em `reserva_form.html`:

- renderize `form.hidden_tag()`;
- renderize o campo de salas;
- renderize data, horários e finalidade;
- mostre as mensagens de erro.

Nos dois templates:

- use labels associados aos campos;
- use placeholders somente quando ajudarem o usuário;
- aproveite os valores preenchidos nos formulários de edição;
- nos formulários POST de exclusão sem `FlaskForm`, envie o token em `input type="hidden"`;
- mantenha a herança de `base.html` e os estilos Bootstrap existentes.

## Resultado esperado

Ao final, deve ser possível:

- cadastrar, listar, editar e remover salas;
- cadastrar, listar, editar e cancelar reservas;
- impedir reservas com dados inválidos;
- impedir reservas sobrepostas;
- permitir horários adjacentes;
- preservar a integridade quando uma sala possuir reservas;
- exibir mensagens claras de sucesso e erro.
