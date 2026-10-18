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
        prioridade = input("Prioridade (Alta, Média ou Baixa): ").strip()

        if prioridade == "Alta":
            return "Alta"
        elif prioridade in ("Média", "Media"):
            return "Média"
        elif prioridade == "Baixa":
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


def visualizar_tarefas():
    print("\n--- Tarefas cadastradas ---")

    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")
        print("-" * 30)


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("\nAplicação encerrada.")
            break
        else:
            print("\nOpção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
