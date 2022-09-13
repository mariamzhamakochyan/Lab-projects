import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi



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

        if username != "":
            if password != "":
                print("connect bdi enenq heto student i acci het")
            else:
                QMessageBox.about(self, "Warning", "Please Enter Password")
        else:
            QMessageBox.about(self, "Warning", "Please Enter username")

    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)



    def adminfunc(self):
        username = self.username.text()
        password = self.password.text()
        info = AdminAcc()
        widget.addWidget(info)
        widget.setCurrentIndex(widget.currentIndex()+1)


class AdminAcc(QDialog):
    def __init__(self):
        super(AdminAcc, self).__init__()
        loadUi("admin.ui", self)


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
            print("Successfully created acc with username: ", username, "and password: ", password)
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)
            if username != "":
                if password != "":
                    if confirmpassword != "":
                        QMessageBox.about(self, "Warning", "you successfully registered")
                    else:
                        QMessageBox.about(self, "Warning", "Please confirm the password")
                else:
                    QMessageBox.about(self, "Warning", "Please Enter your Password")
            else:
                QMessageBox.about(self, "Warning", "Please Enter your Username")


app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(500)
widget.show()
app.exec_()
