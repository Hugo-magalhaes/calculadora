import sys

from buttons import ButtonsGrid
from display import Display, PreviousCalculation, setup_theme
from mainwindow import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setup_theme()
    window = MainWindow()

    # ? Define o ícone
    icon = QIcon(str(WINDOW_ICON))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # ?  Cálculos anteriores
    info = PreviousCalculation('')
    window.add_to_vlayout(info)
    info.style_calculations()

    # ? Display
    display = Display()
    display.setPlaceholderText('Digite suas contas')
    window.add_to_vlayout(display)

    # ? Grid de botões
    grid = ButtonsGrid(display, info, window)
    window.v_layout.addLayout(grid)

    window.adjust_fixed_size()
    window.show()
    app.exec()
