import qdarktheme
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLabel, QLineEdit, QWidget
from variables import (BIG_FONT_SIZE, DARKER_P_COLOR, DARKEST_P_COLOR,
                       MINIMUM_WIDTH, PRIMARY_COLOR, SMALL_FONT_SIZE,
                       TEXT_MARGING, is_empty, is_num_or_dot)

# ? Define cor padrão, selecionado e clicado do botão
qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_P_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_P_COLOR};
    }}

"""


class Display(QLineEdit):
    # ? Sinais das teclas do computador
    eq_pressed = Signal()
    del_pressed = Signal()
    clear_pressed = Signal()
    input_pressed = Signal(str)
    operator_pressed = Signal(str)
    invert_signal_pressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style_display()

    # ? Define formato, margem e alinhamento do display
    def style_display(self):
        margins = [TEXT_MARGING for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    # ? Define teclas e as ações que elas fazem
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        is_enter = key in [KEYS.Key_Return, KEYS.Key_Enter, KEYS.Key_Equal]
        is_delete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        is_esc = key in [KEYS.Key_Escape, KEYS.Key_C]
        is_operator = key in [KEYS.Key_Plus, KEYS.Key_Minus,
                              KEYS.Key_Slash, KEYS.Key_Asterisk, KEYS.Key_P,
                              KEYS.Key_M, KEYS.Key_X]

        if is_enter:
            self.eq_pressed.emit()
            return event.ignore()

        if is_delete:
            self.del_pressed.emit()
            return event.ignore()

        if is_esc:
            self.clear_pressed.emit()
            return event.ignore()

        if text.lower() == 'n':
            self.invert_signal_pressed.emit()
            return event.ignore()

        if is_operator:
            if text.lower() == 'm':
                text = '+'
            if text.lower() == 'p':
                text = '^'
            if text.lower() == 'x':
                text = '*'

            self.operator_pressed.emit(text)
            return event.ignore()

        if is_empty(text):
            return event.ignore()

        if is_num_or_dot(text):
            self.input_pressed.emit(text)
            return event.ignore()

        #  ? Retirando o super, a função bloqueia as teclas do teclado
        # return super().keyPressEvent(event)


class PreviousCalculation(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.style_calculations

    # ? Define fonte e alinhamento dos cálculos anteriores
    def style_calculations(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE} px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)


def setup_theme():
    # ? Define o tema da aplicação
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}",
            },
        },
        additional_qss=qss
    )
