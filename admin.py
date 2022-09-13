# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
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
from PyQt5.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 500)
        Dialog.setStyleSheet(u"")
        self.lineEdit_id = QLineEdit(Dialog)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setGeometry(QRect(10, 50, 211, 31))
        self.lineEdit_first = QLineEdit(Dialog)
        self.lineEdit_first.setObjectName(u"lineEdit_first")
        self.lineEdit_first.setGeometry(QRect(10, 90, 211, 31))
        self.lineEdit_last = QLineEdit(Dialog)
        self.lineEdit_last.setObjectName(u"lineEdit_last")
        self.lineEdit_last.setGeometry(QRect(10, 130, 211, 31))
        self.pushButton_add = QPushButton(Dialog)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setGeometry(QRect(280, 60, 101, 21))
        self.pushButton_add.setStyleSheet(u"background-color: rgb(61, 62, 255);")
        self.lineEdit_email = QLineEdit(Dialog)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(10, 170, 211, 31))
        self.pushButton_modify = QPushButton(Dialog)
        self.pushButton_modify.setObjectName(u"pushButton_modify")
        self.pushButton_modify.setGeometry(QRect(280, 110, 101, 21))
        self.pushButton_modify.setStyleSheet(u"background-color: rgb(61, 62, 255);")
        self.pushButton_delet = QPushButton(Dialog)
        self.pushButton_delet.setObjectName(u"pushButton_delet")
        self.pushButton_delet.setGeometry(QRect(280, 160, 101, 21))
        self.pushButton_delet.setStyleSheet(u"background-color: rgb(61, 62, 255);\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 10, 181, 31))
        self.label.setStyleSheet(u"")
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(15, 231, 371, 261))
        self.pushButton_load = QPushButton(Dialog)
        self.pushButton_load.setObjectName(u"pushButton_load")
        self.pushButton_load.setGeometry(QRect(290, 200, 81, 21))
        self.pushButton_load.setStyleSheet(u"background-color: rgb(61, 62, 255);\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Form", None))
        self.lineEdit_id.setPlaceholderText(QCoreApplication.translate("Dialog", u"  Enter student ID", None))
        self.lineEdit_first.setText("")
        self.lineEdit_first.setPlaceholderText(QCoreApplication.translate("Dialog", u"  Enter student First Name", None))
        self.lineEdit_last.setPlaceholderText(QCoreApplication.translate("Dialog", u"  Enter student Last Name", None))
        self.pushButton_add.setText(QCoreApplication.translate("Dialog", u"ADD", None))
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("Dialog", u"  Enter student Email", None))
        self.pushButton_modify.setText(QCoreApplication.translate("Dialog", u"MODIFY", None))
        self.pushButton_delet.setText(QCoreApplication.translate("Dialog", u"DELET", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"  STUDENTS  INFORMATION", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"FIRST NAME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"LAST NAME", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"EMAIL", None));
        self.pushButton_load.setText(QCoreApplication.translate("Dialog", u"LOAD", None))
    # retranslateUi

