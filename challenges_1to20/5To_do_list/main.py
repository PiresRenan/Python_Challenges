# To-Do List: Construa um aplicativo de lista de tarefas simples utilizando Programação Orientada a Objetos (OOP)
# para representar as tarefas.
from to_do_list import TodoList


def main():
    todo_list = TodoList()

    print("Bem-vindo à sua Lista de Tarefas!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Marcar Tarefa como Concluída")
        print("4. Marcar Tarefa como Pendente")
        print("5. Mostrar Tarefas")
        print("6. Sair")

        choice = input("Digite o número da opção desejada: ")

        if choice == "1":
            description = input("Digite a descrição da tarefa: ")
            todo_list.add_task(description)
        elif choice == "2":
            index = int(input("Digite o número da tarefa a ser removida: ")) - 1
            todo_list.remove_task(index)
        elif choice == "3":
            index = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
            todo_list.mark_task_as_completed(index)
        elif choice == "4":
            index = int(input("Digite o número da tarefa a ser marcada como pendente: ")) - 1
            todo_list.mark_task_as_pending(index)
        elif choice == "5":
            todo_list.show_tasks()
        elif choice == "6":
            print("Obrigado por usar a Lista de Tarefas. Adeus!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções disponíveis.")


if __name__ == "__main__":
    main()
