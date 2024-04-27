import random


class GuessTheNumber:
    def __init__(self, min_number=1, max_number=100):
        self.min_number = min_number
        self.max_number = max_number
        self.secret_number = random.randint(min_number, max_number)
        self.attempts = 0

    def guess(self, number):
        self.attempts += 1
        if number < self.secret_number:
            return "O número é maior."
        elif number > self.secret_number:
            return "O número é menor."
        else:
            return "Parabéns! Você acertou o número."

    def get_attempts(self):
        return self.attempts
