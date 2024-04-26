import random


class HangmanGame:
    def __init__(self):
        self.word_list = [
            ("brasil", ["País localizado na América do Sul.", "Sede do Carnaval mais famoso do mundo.", "Possui a maior floresta tropical do planeta."]),
            ("avatar", ["Filme dirigido por James Cameron.", "Passa-se no planeta Pandora.", "Foi um grande sucesso de bilheteria."]),
            ("python", ["Linguagem de programação de alto nível.", "Criada por Guido van Rossum.", "Muito utilizada em inteligência artificial."]),
            ("internet", ["Rede global de computadores.", "Inventada na década de 1960.", "Revolucionou a comunicação e o acesso à informação."]),
            ("futebol", ["Esporte mais popular do mundo.", "É jogado com uma bola.", "Possui uma Copa do Mundo."]),
            ("matrix", ["Filme de ficção científica estrelado por Keanu Reeves.", "Dirigido pelos irmãos Wachowski.", "Explora a ideia de uma realidade simulada."]),
            ("einstein", ["Famoso cientista conhecido por sua teoria da relatividade.", "Ganhou o Prêmio Nobel de Física em 1921.", "Nasceu na Alemanha."]),
            ("frança", ["País europeu famoso pela Torre Eiffel.", "Conhecido por sua culinária sofisticada.", "Possui a Catedral de Notre-Dame."]),
            ("harrypotter", ["Série de livros escrita por J.K. Rowling.", "Conta a história de um jovem bruxo.", "Tem uma escola chamada Hogwarts."]),
            ("inception", ["Filme dirigido por Christopher Nolan.", "Explora a ideia de sonhos dentro de sonhos.", "Estrelado por Leonardo DiCaprio."]),
        ]
        self.secret_word = ""
        self.guesses_left = 6
        self.guessed_letters = set()
        self.hints_left = 3
        self.used_hints = []

    def _choose_secret_word(self):
        return random.choice(self.word_list)

    def _reveal_letter(self, letter):
        if letter in self.secret_word[0]:
            print(f"A letra '{letter}' está na palavra!")
        else:
            print(f"A letra '{letter}' não está na palavra.")
            self.guesses_left -= 1

    def _display_word(self):
        display = ''
        for letter in self.secret_word[0]:
            if letter in self.guessed_letters:
                display += letter + ' '
            else:
                display += '_ '
        return display.strip()

    def _show_hints_left(self):
        print(f"Você usou {len(self.used_hints)} dicas e tem {self.hints_left} dicas restantes.")

    def _display_guessed_letters(self):
        sorted_letters = sorted(self.guessed_letters)
        guessed_str = ', '.join(sorted_letters)
        print(f"Letras usadas anteriormente: {guessed_str}")

    def new_game(self):
        self.secret_word = self._choose_secret_word()
        self.guesses_left = 6
        self.guessed_letters = set()
        self.hints_left = 3
        self.used_hints = []

    def display_game_status(self):
        print("Palavra secreta:", self._display_word())
        print("Tentativas restantes:", self.guesses_left)
        self._show_hints_left()
        self._display_guessed_letters()

    def guess(self, letter):
        if letter in self.guessed_letters:
            print("Você já tentou essa letra antes.")
            return

        self.guessed_letters.add(letter)
        self._reveal_letter(letter)

    def give_hint(self):
        if self.hints_left > 0:
            available_hints = [hint for hint in self.secret_word[1] if hint not in self.used_hints]
            if available_hints:
                hint = random.choice(available_hints)
                print(f"Dica: {hint}")
                self.used_hints.append(hint)
                self.hints_left -= 1
            else:
                print("Todas as dicas já foram usadas!")
        else:
            print("Você já usou todas as dicas!")

    def is_game_over(self):
        if self.guesses_left <= 0:
            print(f"Você perdeu! A palavra secreta era '{self.secret_word[0]}'.")
            return True
        elif set(self.secret_word[0]) <= self.guessed_letters:
            print("Parabéns, você ganhou!")
            return True
        return False
