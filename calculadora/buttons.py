
import math
from typing import TYPE_CHECKING

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton
from variables import (MID_FONT_SIZE, convert_number, is_empty, is_num_or_dot,
                       is_valid_num)

# ? Para evitar importações circulares
if TYPE_CHECKING:
    from display import Display, PreviousCalculation
    from mainwindow import MainWindow


class Button(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.style_button()

    # ? Define tamanho e fonte dos botões
    def style_button(self):
        font = self.font()
        font.setPixelSize(MID_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)

        # ? Tem chance de sobrescrever o estilo definido antes
        # self.setStyleSheet(f'font-size: {MID_FONT_SIZE} px;')
        # ? Mantém pressionado
        # self.setCheckable(True)
        # ? Define a propiedade do botão
        # self.setProperty('cssClass', 'specialButton')


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'PreviousCalculation',
                 window: 'MainWindow', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # ? Configuração da grid de botões e suas funções
        self._grid_mask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N', '0', '.', '='],
        ]
        self.window = window
        self.display = display
        self.info = info
        self._equation = ''
        self._initial_equation = 'Sua conta'
        self.equation = self._initial_equation
        self._left = None
        self._right = None
        self._operator = None
        self._make_grid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    # ? Descreve os botões no grid de botçoes
    def _make_grid(self):

        self.display.eq_pressed.connect(self._equal)
        self.display.del_pressed.connect(self._backspace)
        self.display.clear_pressed.connect(self._clear)
        self.display.input_pressed.connect(self._insert_in_display)
        self.display.operator_pressed.connect(self._operator_config)

        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                if not is_num_or_dot(button_text) and \
                        not is_empty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._special_button(button)

                self.addWidget(button, i, j)
                # ? Aciona os botões e seu texto
                button_slot = self._connection_slot(
                    self._insert_in_display, button_text)

                self._connect_button_clicked(button, button_slot)

    # ? Conecta a função clicar ao método do slot
    def _connect_button_clicked(self, button, slot):
        button.clicked.connect(slot)

    # ? Chama a função slot para aplicar funções aos botões
    @Slot()
    def _connection_slot(self, func, *args, **kwargs):
        @Slot(bool)
        # ? O Checked já é padrão, caso o queira utilize '_'
        def real_slot(_):
            func(*args, **kwargs)
        return real_slot

    # ? Slot real que aplica a função texto dos botões ao display
    @Slot()
    def _insert_in_display(self, text):
        new_display_value = self.display.text() + text

        if not is_valid_num(new_display_value):
            return

        self.display.insert(text)
        self.display.setFocus()
        # print(button.text())

    # ? Define as funções dos botões especiais
    def _special_button(self, button: 'Button'):
        text = button.text()
        if text.lower() == 'c':
            # sb_slot = self._connection_slot(self.display.clear)
            self._connect_button_clicked(button, self._clear)

        if text.lower() == 'd':
            self._connect_button_clicked(
                button, self._backspace)

        if text.lower() == 'n':
            self._connect_button_clicked(button,
                                         self._invert_signal)

        if text in '+-/*^':
            self._connect_button_clicked(
                button,
                self._connection_slot(self._operator_config, text)
            )

        if text == '=':
            self._connect_button_clicked(
                button, self._equal)

    # ? Limpa todo o display
    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._operator = None
        self.equation = self._initial_equation
        self.display.clear()
        self.display.setFocus()

    # ? Inverte o sinal do número para negativo
    @Slot()
    def _invert_signal(self):
        display_text = self.display.text()

        if not is_valid_num(display_text):
            return
        new_number = -convert_number(display_text)

        self.display.setText(str(new_number))
        self.display.setFocus()

    # ? Salva as operações já realizadas no display
    @Slot()
    def _operator_config(self, text):
        display_text = self.display.text()
        self.display.clear()

        if not is_valid_num(display_text) and self._left is None:
            self._show_error('Você ainda não digitou nada.')
            return

        # ? Define o valor da esquerda como num
        if self._left is None:
            self._left = convert_number(display_text)

        self._operator = text
        self.equation = f'{self._left} {self._operator} __'
        self.display.setFocus()

    # ? Define a função do operador de igual

    @Slot()
    def _equal(self):
        display_text = self.display.text()

        if not is_valid_num(display_text):
            self._show_error('Valor inválido.')
            return

        if self._operator is None:
            self._show_error('Você não digitou um operador.')
            return

        self._right = convert_number(display_text)
        self.equation = f'{self._left} {self._operator} {self._right}'
        result = ''

        # ? Corrigi alguns erros matemáticos e problema do ^
        try:
            if '^' in self.equation and isinstance(self._left, float | int):
                # result = eval(self.equation.replace('^', '**'))
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
            # print(result)
        except ZeroDivisionError:
            self._show_error('Não se pode dividir por zero.')
        except OverflowError:
            self._show_error('Valor acima do alcance.')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self.display.setText(str(result))
        self._left = self.display.setText(str(result))
        self._right = None
        self.display.setFocus()

        # ? Limpa a seleção se o resultado for um erro
        if result == 'error':
            self._left = None

    # ? Define a função ' apagar'
    @ Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    # ? Define a função dos avisos
    def _make_dialog(self, text):
        msg_box = self.window.message_box()
        msg_box.setText(text)
        return msg_box

    #  ? Caixa de diálogo de erro
    def _show_error(self, text):
        msg_box = self._make_dialog(text)
        msg_box.setIcon(msg_box.Icon.Critical)
        msg_box.exec()
        self.display.setFocus()

    #  ? Caixa de diálogo de aviso
    def _show_info(self, text):
        msg_box = self._make_dialog(text)
        msg_box.setIcon(msg_box.Icon.Information)
        msg_box.exec()
        self.display.setFocus()

        # ? Pode configurar botões da janela de aviso e o que eles fazem
        # msg_box.setStandardButtons(
        #     msg_box.StandardButton.Ok |
        #     msg_box.StandardButton.Cancel |
        #     msg_box.StandardButton.Save
        # )

        # result = msg_box.exec()

        # if result == msg_box.StandardButton.Ok:
        #     print(' Você pode fazer algo com o ok')

        # elif result == msg_box.StandardButton.Cancel:
        #     print(' Você pode fazer algo com o Cancel ')

        # elif result == msg_box.StandardButton.Save:
        #     print(' Você pode fazer algo com o Save')
