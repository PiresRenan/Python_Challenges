import sys

from gui.board_widget import BoardWidget

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Jogo da Velha')
        self.setGeometry(100, 100, 300, 300)

        self.board_widget = BoardWidget()
        self.setCentralWidget(self.board_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
