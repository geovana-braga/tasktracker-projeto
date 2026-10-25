# TaskTracker

Projeto desenvolvido no Bootcamp II.

O TaskTracker é uma aplicação de linha de comando para organizar tarefas. O programa permite cadastrar, visualizar e guardar as tarefas para a próxima execução.

## Funcionalidades

- Cadastrar uma nova tarefa
- Validar título obrigatório
- Validar prioridade
- Definir o status inicial como `Pendente`
- Visualizar todas as tarefas cadastradas
- Informar quando ainda não existem tarefas
- Salvar as tarefas em um arquivo JSON para que continuem disponíveis após sair e abrir novamente

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
- JSON

## Estrutura do projeto

```text
tasktracker-projeto/
├── .gitignore
├── .dockerignore
├── .github/workflows/docker-smoke.yml
├── docs/
│   └── Planejamento Lógico TaskTracker - Geovana Cavalcante Braga.pdf
├── src/
│   └── main.py
├── scripts/testar-docker.ps1
├── tests/test_cli.py
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

No menu, digite `1` para cadastrar uma tarefa, `2` para visualizar as tarefas e `3` para sair. Ao cadastrar, o programa pede título, descrição, prioridade e data limite. O arquivo `data/tarefas.json` é criado automaticamente na primeira tarefa salva. A pasta `data/` não é enviada ao GitHub.

## Como executar com Docker

Neste projeto, **imagem Docker** significa o pacote de software usado para iniciar um container. Não é uma figura ou fotografia. O build é feito pelo terminal; depois você pode conferir a imagem na aba **Images** do Docker Desktop ou com `docker image ls tasktracker-app`.

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

O comando acima atende à demonstração básica, mas cada `docker run` cria um novo container. Para **guardar as tarefas entre execuções**, use sempre o mesmo volume nomeado:

```bash
docker run -it -v tasktracker-data:/app/data tasktracker-app
```

Se executar novamente esse comando com `-v`, as tarefas anteriores aparecerão na opção `2` do menu.

### 3. Executar com Docker Compose

Também é possível executar a aplicação usando o arquivo `docker-compose.yml`:

```bash
docker compose run tasktracker
```

O `docker-compose.yml` mantém a entrada padrão e o terminal interativo habilitados por meio de `stdin_open: true` e `tty: true`. Também monta o volume `tasktracker-data` em `/app/data`; por isso as tarefas continuam disponíveis quando você sai e executa o Compose novamente. O comando Docker com `-v` usa esse mesmo volume.

## Arquivos de containerização

### Dockerfile

O `Dockerfile` utiliza a imagem `python:3.11-slim`, define `/app` como diretório de trabalho, copia o conteúdo da pasta `src` para o container e inicia a aplicação pelo arquivo `src/main.py`.

### docker-compose.yml

O arquivo `docker-compose.yml` cria o serviço `tasktracker` a partir do `Dockerfile`, configura a interatividade necessária para a aplicação de linha de comando e guarda os dados em um volume Docker.

## Testes

Para testar as regras do menu e a persistência com Python:

```bash
python -m unittest discover -s tests -v
```

No Windows, com o Docker Desktop em execução, rode o teste completo de build, container e persistência:

```powershell
pwsh -NoProfile -File .\scripts\testar-docker.ps1
```

Esse teste usa um volume temporário próprio e o remove ao terminar. As suas tarefas não são apagadas. O GitHub Actions também executa o build e a CLI em containers Linux a cada envio para a branch `main`.

## Observações

- Os comandos Docker exigem que o Docker Desktop esteja em execução com o mecanismo de containers Linux disponível.
- Em Python local, as tarefas ficam em `data/tarefas.json`.
- No Docker, o comando básico sem `-v` não preserva as tarefas entre containers. Use o comando com `-v` ou o Docker Compose para persistir os dados.
- A data limite é armazenada como texto nesta versão; o programa não verifica o formato da data.
