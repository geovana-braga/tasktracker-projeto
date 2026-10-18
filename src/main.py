# TaskTracker - Bootcamp II


tarefas = []


def mostrar_menu():
    print("\n=== TASKTRACKER ===")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def pedir_titulo():
    while True:
        titulo = input("Título: ").strip()

        if titulo:
            return titulo

        print("O título é obrigatório. Digite um título válido.")


def pedir_prioridade():
    while True:
        prioridade = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()

        if prioridade == "alta":
            return "Alta"
        elif prioridade in ("média", "media"):
            return "Média"
        elif prioridade == "baixa":
            return "Baixa"

        print("Prioridade inválida. Digite Alta, Média ou Baixa.")


def cadastrar_tarefa():
    print("\n--- Cadastro de nova tarefa ---")

    titulo = pedir_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = pedir_prioridade()
    data_limite = input("Data limite: ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            print("\nVisualização de tarefas")
        elif opcao == "3":
            print("\nAplicação encerrada.")
            break
        else:
            print("\nOpção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
