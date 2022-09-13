# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
        self.stdreg = QPushButton(Form)
        self.stdreg.setObjectName(u"stdreg")
        self.stdreg.setGeometry(QRect(20, 310, 171, 31))
        self.stdreg.setStyleSheet(u"\n"
"background-color: rgb(1, 47, 82);")
        self.adreg = QPushButton(Form)
        self.adreg.setObjectName(u"adreg")
        self.adreg.setGeometry(QRect(210, 310, 171, 31))
        self.adreg.setStyleSheet(u"\n"
"background-color: rgb(1, 47, 82);")
        self.username = QLineEdit(Form)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(20, 120, 361, 41))
        self.password = QLineEdit(Form)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(20, 180, 361, 41))
        self.password.setEchoMode(QLineEdit.Password)
        self.confirmpassword = QLineEdit(Form)
        self.confirmpassword.setObjectName(u"confirmpassword")
        self.confirmpassword.setGeometry(QRect(20, 240, 361, 41))
        self.confirmpassword.setEchoMode(QLineEdit.Password)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.stdreg.setText(QCoreApplication.translate("Form", u"Registrate as student", None))
        self.adreg.setText(QCoreApplication.translate("Form", u"Registrate as admin", None))
        self.username.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("Form", u"  Enter the username", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("Form", u"  Enter the password", None))
        self.confirmpassword.setText("")
        self.confirmpassword.setPlaceholderText(QCoreApplication.translate("Form", u"  Confirm the password", None))
    # retranslateUi

