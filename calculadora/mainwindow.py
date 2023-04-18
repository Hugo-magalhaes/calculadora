from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # ? Configuração de layout básico
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        # ? Título da janela
        self.setWindowTitle('Calculadora')

    # ? Última coisa a ser feita: Fixar o formato da janela
    def adjust_fixed_size(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # ? Adiciona coisas à box em formato vertical
    def add_to_vlayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)

    #  ? Caixa de diálogo
    def message_box(self):
        return QMessageBox(self)
