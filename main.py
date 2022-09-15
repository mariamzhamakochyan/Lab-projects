import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QPushButton
from PyQt5.uic import loadUi
import sqlite3


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.b2.clicked.connect(self.studentfunc)
        self.b3.clicked.connect(self.adminfunc)
        self.b1.clicked.connect(self.gotocreate)

    def studentfunc(self):
        username = self.username.text()
        password = self.password.text()

        if len(username)==0 or len(password)==0:
            QMessageBox.about(self, "Warning", "Please Enter username and password")
        else:
            conn = sqlite3.connect("shop_data.db")
            cursor = conn.cursor()
            cursor.execute('SELECT password FROM login_info WHERE username =\''+username+"\'")
            row = cursor.fetchall()
            if row:
                self.studentPage = StudentAcc()
                widget.addWidget(self.studentPage)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                self.studentPage.show()
            else:
                QMessageBox.about(self, "Warning", "Wrong username or password")

    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def adminfunc(self):
        username = self.username.text()
        password = self.password.text()
        if username != "":
            if password != "":
                self.adminPage = AdminAcc()
                widget.addWidget(self.adminPage)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                self.adminPage.show()
            else:
                QMessageBox.about(self, "Warning", "Please Enter Password")
        else:
            QMessageBox.about(self, "Warning", "Please Enter username")


class AdminAcc(QDialog):
    def __init__(self):
        super(AdminAcc, self).__init__()
        loadUi("admin.ui", self)
        self.pushButton_add.clicked.connect(self.addfunc)


    def addfunc(self):
        id = self.lineEdit_id.text()
        name = self.lineEdit_first.text()
        surname = self.lineEdit_last.text()
        email = self.lineEdit_email.text()

        conn = sqlite3.connect("std_data.db")
        cur = conn.cursor()
        student_info = [id, name, surname, email]
        cur.execute('INSERT INTO student_data (id, name, surname, email) VALUES (?,?,?,?)', student_info)
        conn.commit()
        conn.close()





class StudentAcc(QDialog):
    def __init__(self):
        super(StudentAcc, self).__init__()
        loadUi("student.ui", self)


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("register.ui", self)
        self.stdreg.clicked.connect(self.createaccfunction)
        self.adreg.clicked.connect(self.createaccfunction)

    def createaccfunction(self):
        username = self.username.text()
        if self.password.text() == self.confirmpassword.text():
            password = self.password.text()
            confirmpassword = self.confirmpassword.text()

            if len(username) == 0 or len(password) == 0 or len(confirmpassword) == 0:
                QMessageBox.about(self, "Warning", "Please fill in all inputs.")

            elif password != confirmpassword:
                QMessageBox.about(self, "Warning", "Passwords do not match")
            else:
                conn = sqlite3.connect("shop_data.db")
                cur = conn.cursor()
                user_info = [username, password]
                cur.execute('INSERT INTO login_info (username, password) VALUES (?,?)', user_info)
                conn.commit()
                conn.close()
                self.registerPage = Login()
                widget.addWidget(self.registerPage)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                self.registerPage.show()



app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(500)
widget.show()
app.exec_()