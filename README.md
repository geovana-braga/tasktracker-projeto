# TaskTracker

Projeto desenvolvido na Fase 2 do Bootcamp II.

O TaskTracker é uma aplicação simples de linha de comando para organizar tarefas. O programa permite cadastrar novas tarefas e visualizar as tarefas já registradas.

## Funcionalidades

- Cadastrar uma nova tarefa
- Validar título obrigatório
- Validar prioridade
- Definir o status inicial como `Pendente`
- Visualizar todas as tarefas cadastradas
- Informar quando ainda não existem tarefas

## Dados de cada tarefa

Cada tarefa possui:

- Título
- Descrição
- Prioridade
- Data limite
- Status

## Tecnologias utilizadas

- Python 3
- Git
- GitHub

## Estrutura do projeto

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Como executar

1. Tenha o Python 3 instalado no computador.
2. Abra o terminal na pasta do projeto.
3. Execute:

```bash
python src/main.py
```

Em alguns computadores, o comando pode ser:

```bash
python3 src/main.py
```

Depois disso, basta escolher uma opção no menu exibido no terminal.
