import random


class DiceSimulator:
    def roll_dice(self, num_dice, num_faces):
        # Simula o lançamento de dados
        rolls = [random.randint(1, num_faces) for _ in range(num_dice)]
        return rolls
