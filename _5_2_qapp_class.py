# type:ignore
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

app = QApplication(sys.argv)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.setWindowTitle('Janela de classe')

        # Botão 1
        self.botao1 = QPushButton('Botão 1')
        self.botao1.setStyleSheet('font-size: 60px;')
        self.botao1.clicked.connect(self.slot_2)

        self.botao2 = QPushButton('Botão 2')
        self.botao2.setStyleSheet('font-size: 40px;')

        self.botao3 = QPushButton('Botão 3')
        self.botao3.setStyleSheet('font-size: 80px;')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 2, 1, 1, 1)

        self.status_bar = self.statusBar()
        self.status_bar.showMessage('O status está completo')

        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Menu')

        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação')
        self.primeira_acao.triggered.connect(self.slot_1)

        self.segunda_acao = self.primeiro_menu.addAction('Segunda ação')
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.toggled.connect(self.slot_2)
        self.segunda_acao.hovered.connect(self.slot_2)

    @Slot()
    def slot_1(self):
        self.status_bar.showMessage('A situação é nova')

    @Slot()
    def slot_2(self):
        print('Está marcado ?', self.segunda_acao.isChecked())


window = MyWindow()

window.show()

app.exec()
