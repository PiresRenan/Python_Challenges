from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QMessageBox
from core.game import Game


class BoardWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.game = Game()
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()
        layout.setSpacing(0)

        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = QPushButton('')
                button.setFixedSize(100, 100)
                button.clicked.connect(lambda state, row=row, col=col: self.handle_click(row, col))
                layout.addWidget(button, row, col)
                button_row.append(button)
            self.buttons.append(button_row)
        self.setLayout(layout)

    def handle_click(self, row, col):
        button = self.buttons[row][col]
        if button.text() == '':
            button.setText('X' if self.game.current_player == 'X' else 'O')
            self.game.make_move(row, col)
            winner = self.game.check_winner()
            if winner:
                self.game.current_player = 'O' if self.game.current_player == 'X' else 'X'
                QMessageBox.information(self, 'Acabou!', f'O jogador "{self.game.current_player}" venceu o jogo!')
                self.reset_game()
            elif self.game.is_draw():
                QMessageBox.information(self, 'Acabou!', 'O resultado é empate!')
                self.reset_game()

    def reset_game(self):
        self.game.reset()
        for row in self.buttons:
            for button in row:
                button.setText('')