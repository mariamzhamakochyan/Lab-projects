# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logZDOWdp.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(381, 404)
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 381, 411))
        self.listWidget.setStyleSheet(u"background-color:rgba(47, 49, 52,200);\n"
"border-radious:20px;\n"
"")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 170, 211, 31))
        self.lineEdit.setStyleSheet(u"border-radius:2px;\n"
"padding-left:10px;\n"
"border:px\n"
"")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 220, 211, 31))
        self.lineEdit_2.setStyleSheet(u"border-radius:2px;\n"
"padding-left:10px;\n"
"border:px\n"
"")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.b1 = QPushButton(Form)
        self.b1.setObjectName(u"b1")
        self.b1.setGeometry(QRect(120, 270, 151, 31))
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.b1.setFont(font)
        self.b1.setStyleSheet(u"QPushButton#b1{\n"
"background-color: rgb(255, 191, 16);	\n"
"color:rgb(1,12,0);\n"
"colorborder-radius:5px;\n"
"}\n"
"QPushButton#b1:pressed{\n"
"	background-color: rgb(255, 234, 87);\n"
"}\n"
"")
        self.b2 = QPushButton(Form)
        self.b2.setObjectName(u"b2")
        self.b2.setGeometry(QRect(90, 360, 211, 31))
        self.b2.setStyleSheet(u"QPushButton#b2{\n"
"background-color: rgb(255, 191, 16);	\n"
"color:rgb(1,12,0);\n"
"colorborder-radius:5px;\n"
"}\n"
"QPushButton#b2:pressed{\n"
"	background-color: rgb(255, 234, 87);\n"
"}\n"
"")
        QWidget.setTabOrder(self.listWidget, self.lineEdit)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter the username", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"password", None))
        self.b1.setText(QCoreApplication.translate("Form", u"L O G I N", None))
        self.b2.setText(QCoreApplication.translate("Form", u"REGISTER", None))
    # retranslateUi


