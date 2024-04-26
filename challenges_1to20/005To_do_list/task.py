class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "Concluída" if self.completed else "Pendente"
        return f"Tarefa: {self.description} - Status: {status}"

    def mark_as_completed(self):
        self.completed = True

    def mark_as_pending(self):
        self.completed = False
