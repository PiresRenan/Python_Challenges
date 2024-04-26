from task import Task


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        del self.tasks[index]

    def mark_task_as_completed(self, index):
        self.tasks[index].mark_as_completed()

    def mark_task_as_pending(self, index):
        self.tasks[index].mark_as_pending()

    def show_tasks(self):
        if not self.tasks:
            print("Lista de tarefas vazia.")
        else:
            print("Lista de Tarefas:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
