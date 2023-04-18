# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'UI_example.ui'
##
# Created by: Qt User Interface Compiler version 6.4.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                               QLineEdit, QMainWindow, QMenuBar, QPushButton,
                               QSizePolicy, QStatusBar, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(830, 673)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_result = QLabel(self.centralwidget)
        self.label_result.setObjectName(u"label_result")
        font = QFont()
        font.setPointSize(40)
        self.label_result.setFont(font)
        self.label_result.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.gridLayout.addWidget(self.label_result, 2, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Line_name = QLineEdit(self.centralwidget)
        self.Line_name.setObjectName(u"Line_name")
        font1 = QFont()
        font1.setPointSize(30)
        self.Line_name.setFont(font1)
        self.Line_name.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.gridLayout_2.addWidget(self.Line_name, 0, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 1)

        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 830, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label_result.setText(QCoreApplication.translate(
            "MainWindow", u"Coisa de doido", None))
        self.Line_name.setText(QCoreApplication.translate(
            "MainWindow", u"Digite seu nome", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Seu nome:", None))
        self.pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"Enviar", None))
    # retranslateUi
