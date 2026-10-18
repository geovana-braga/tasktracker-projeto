# TaskTracker - Bootcamp II


tarefas = []


def mostrar_menu():
    print("\n=== TASKTRACKER ===")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\nCadastro de tarefa")
        elif opcao == "2":
            print("\nVisualização de tarefas")
        elif opcao == "3":
            print("\nAplicação encerrada.")
            break
        else:
            print("\nOpção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
