# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 500)
        self.b1 = QPushButton(Form)
        self.b1.setObjectName(u"b1")
        self.b1.setGeometry(QRect(40, 430, 321, 41))
        self.b1.setStyleSheet(u"\n"
"background-color: rgb(1, 47, 82);")
        self.b3 = QPushButton(Form)
        self.b3.setObjectName(u"b3")
        self.b3.setGeometry(QRect(210, 320, 171, 31))
        self.b3.setStyleSheet(u"\n"
"background-color: rgb(1, 47, 82);")
        self.b2 = QPushButton(Form)
        self.b2.setObjectName(u"b2")
        self.b2.setGeometry(QRect(20, 320, 171, 31))
        self.b2.setStyleSheet(u"\n"
"background-color: rgb(1, 47, 82);")
        self.password = QLineEdit(Form)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(20, 250, 361, 41))
        self.password.setEchoMode(QLineEdit.Password)
        self.username = QLineEdit(Form)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(20, 190, 361, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.b1.setText(QCoreApplication.translate("Form", u"R E G I S T E R", None))
        self.b3.setText(QCoreApplication.translate("Form", u"Admin Login", None))
        self.b2.setText(QCoreApplication.translate("Form", u"Student Login", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Form", u"  Enter the password", None))
        self.username.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("Form", u"  Enter the username", None))
    # retranslateUi

