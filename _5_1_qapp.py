# type:ignore

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QStatusBar, QWidget)


@Slot()
def slot_example(status_bar: QStatusBar):
    status_bar.showMessage('A situação é nova')


@Slot()
def slot_2(checked):
    print('Está marcado ?', checked)


@Slot()
def slot_3(action):
    def inner():
        slot_2(action.isChecked())
    return inner


# A aplicação tem que ser executada ao fim do código
app = QApplication(sys.argv)
#  O widget maior é quem deve ter show
window = QMainWindow()
central_widget = QWidget()

window.setCentralWidget(central_widget)
window.setWindowTitle('Minha primeira janela')


botao1 = QPushButton('texto de botão')
botao1.setStyleSheet('font-size: 40px;')

botao2 = QPushButton('texto de botão')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('texto de botão')
botao3.setStyleSheet('font-size: 40px;')


layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 2, 1, 1, 1)

status_bar = window.statusBar()
status_bar.showMessage('O status está completo')

menu = window.menuBar()
primeiro_menu = menu.addMenu('Menu')

primeira_acao = menu.addAction('Primeira ação')
primeira_acao.triggered.connect(  # type:ignore
    lambda: slot_example(status_bar))

segunda_acao = menu.addAction('Segunda ação')
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(slot_2)  # type:ignore
segunda_acao.hovered.connect(slot_3(segunda_acao))

botao1.clicked.connect(slot_3(segunda_acao))
window.show()

app.exec()
