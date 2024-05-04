import sys

from core.game import Game
from gui.board import Board

from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)

    game = Game()

    board = Board(game)

    board.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
