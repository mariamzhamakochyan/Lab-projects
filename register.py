# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerdMoiRl.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(380, 401)
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, -10, 381, 411))
        self.listWidget.setStyleSheet(u"background-color:rgba(47, 49, 52,200);\n"
"border-radious:20px;\n"
"")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 130, 211, 31))
        self.lineEdit.setStyleSheet(u"border-radius:2px;\n"
"padding-left:10px;\n"
"border:px\n"
"")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 230, 211, 31))
        self.lineEdit_2.setStyleSheet(u"border-radius:2px;\n"
"padding-left:10px;\n"
"border:px\n"
"")
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(90, 180, 211, 31))
        self.lineEdit_3.setStyleSheet(u"border-radius:2px;\n"
"padding-left:10px;\n"
"border:px\n"
"")
        self.b2 = QPushButton(Form)
        self.b2.setObjectName(u"b2")
        self.b2.setGeometry(QRect(90, 330, 211, 31))
        self.b2.setStyleSheet(u"QPushButton#b2{\n"
"background-color: rgb(255, 191, 16);	\n"
"color:rgb(1,12,0);\n"
"colorborder-radius:5px;\n"
"}\n"
"QPushButton#b2:pressed{\n"
"	background-color: rgb(255, 234, 87);\n"
"}\n"
"")
        self.Check = QCheckBox(Form)
        self.Check.setObjectName(u"Check")
        self.Check.setGeometry(QRect(110, 280, 181, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Email address", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.b2.setText(QCoreApplication.translate("Form", u"REGISTER", None))
        self.Check.setText(QCoreApplication.translate("Form", u"Check if you are a student", None))
    # retranslateUi


