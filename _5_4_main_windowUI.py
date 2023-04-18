# pyside6-uic (path do ui gerado) -o (path de onde o .py será gerado)

import sys
import time
from typing import cast

from PySide6.QtCore import QEvent, QObject, QThread, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QApplication, QMainWindow

from example_ui import Ui_MainWindow


class Worker(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)
        self.finished.emit(value)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.change_result)  # type:ignore
        self.Line_name.installEventFilter(self)

    def change_result(self):
        self._worker = Worker()
        self._thread = QThread()

        # -- Só para o python não jogá-los fora depois da execução e dar erro
        worker = self._worker
        thread = self._thread

        # -- Mover a worker para thread
        worker.moveToThread(thread)
        # -- Run
        thread.started.connect(worker.run)  # type:ignore
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)  # type:ignore
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.messages1)
        worker.progressed.connect(self.messages2)
        worker.finished.connect(self.messages3)

        thread.start()

    # ! Problema de lambda é que ela pode ser chamada quando
    # ! Já está sendo executada
    def messages1(self, value):
        self.label_result.setText(value)
        self.pushButton.setDisabled(True)
        print('Worker iniciado')

    def messages2(self, value):
        self.label_result.setText(value)
        print('Em progresso')

    def messages3(self, value):
        self.label_result.setText(value)
        self.pushButton.setDisabled(False)
        print('Worker finalizado')

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            text = self.Line_name.text()
            self.label_result.setText(text + event.text())
        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
