import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.b2.clicked.connect(self.loginfunction)
        self.b3.clicked.connect(self.loginfunction)
        self.b1.clicked.connect(self.gotocreate)


    def loginfunction(self):
        username=self.username.text()
        password=self.password.text()
        print("Successfully logged in with username: ", username, "and password:", password)

    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("register.ui",self)
        self.stdreg.clicked.connect(self.createaccfunction)
        self.adreg.clicked.connect(self.createaccfunction)



    def createaccfunction(self):
        username = self.username.text()
        if self.password.text()==self.confirmpassword.text():
            password=self.password.text()
            print("Successfully created acc with username: ", username, "and password: ", password)
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)



app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(500)
widget.show()
app.exec_()
