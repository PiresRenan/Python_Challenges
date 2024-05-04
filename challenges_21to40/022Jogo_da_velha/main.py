import sys

from core.game import Game
from gui.main_window import MainWindow

from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    board = MainWindow()
    board.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
