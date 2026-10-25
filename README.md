# TaskTracker

Projeto desenvolvido no Bootcamp II.

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
- Docker
- Docker Compose

## Estrutura do projeto

```text
tasktracker-projeto/
├── .gitignore
├── .dockerignore
├── docs/
│   └── Planejamento Lógico TaskTracker - Geovana Cavalcante Braga.pdf
├── src/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Como executar com Python

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

## Como executar com Docker

### 1. Construir a imagem

Na raiz do projeto, execute:

```bash
docker build -t tasktracker-app .
```

Esse comando utiliza o `Dockerfile` para criar a imagem da aplicação.

### 2. Executar diretamente com Docker

Depois da construção da imagem, execute:

```bash
docker run -it tasktracker-app
```

A opção `-it` mantém o terminal interativo para que seja possível utilizar o menu do TaskTracker.

### 3. Executar com Docker Compose

Também é possível executar a aplicação usando o arquivo `docker-compose.yml`:

```bash
docker compose run tasktracker
```

O `docker-compose.yml` mantém a entrada padrão e o terminal interativo habilitados por meio de `stdin_open: true` e `tty: true`.

## Arquivos de containerização

### Dockerfile

O `Dockerfile` utiliza a imagem `python:3.11-slim`, define `/app` como diretório de trabalho, copia o conteúdo da pasta `src` para o container e inicia a aplicação pelo arquivo `src/main.py`.

### docker-compose.yml

O arquivo `docker-compose.yml` cria o serviço `tasktracker` a partir do `Dockerfile` e configura a interatividade necessária para a aplicação de linha de comando.

## Observações

- Os comandos Docker exigem que o Docker Desktop esteja em execução com o mecanismo de containers Linux disponível.
- As tarefas ficam apenas na memória enquanto o programa está aberto. Ao encerrar a aplicação ou o container, os dados cadastrados nesta execução não são preservados.
