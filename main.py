import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
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

        if len(username) == 0 or len(password) == 0:
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

        if len(username) == 0 or len(password) == 0:
            QMessageBox.about(self, "Warning", "Please Enter username and password")
        else:
            conn = sqlite3.connect("shop_data1.db")
            cursor = conn.cursor()
            cursor.execute('SELECT password FROM login_info1 WHERE username =\''+username+"\'")
            row = cursor.fetchall()
            if row:
                self.adminPage = AdminAcc()
                widget.addWidget(self.adminPage)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                self.adminPage.show()
            else:
                QMessageBox.about(self, "Warning", "Wrong username or password")


class AdminAcc(QDialog):
    def __init__(self):
        super(AdminAcc, self).__init__()
        loadUi("admin.ui", self)
        self.pushButton_add.clicked.connect(self.addfunc)
        self.pushButton_list.clicked.connect(self.listfunc)
        self.pushButton_modify.clicked.connect(self.modifyfunc)
        self.pushButton_delet.clicked.connect(self.delfunc)


    def listfunc(self):
        connection = sqlite3.connect("std_data.db")
        query = "SELECT * FROM student_data"
        connection.execute(query)
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

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

    def delfunc(self):
        id = self.lineEdit_id.text()
        name = self.lineEdit_first.text()
        surname = self.lineEdit_last.text()
        email = self.lineEdit_email.text()
        conn = sqlite3.connect("std_data.db")
        cur = conn.cursor()
        deleteq = "DELETE FROM student_data WHERE email = %s"
        values = (email,)
        try:
            cur.execute(deleteq, values)
            conn.commit()
            print("success")
        except:
            print("failed")

    def modifyfunc(self):
        id = self.lineEdit_id.text()
        name = self.lineEdit_first.text()
        surname = self.lineEdit_last.text()
        email = self.lineEdit_email.text()
        conn = sqlite3.connect("std_data.db")
        cur = conn.cursor()
        student_info = [id, name, surname, email]
        updateq = "UPDATE student_data SET (id, name, surname, email) VALUES (?,?,?,?)', student_info"
        values = (id, name, surname, email)
        try:
            cur.execute(updateq, values)
            cur.commit()
            print("Success")
        except:
            print("failed")


class StudentAcc(QDialog):
    def __init__(self):
        super(StudentAcc, self).__init__()
        loadUi("student.ui", self)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_done.clicked.connect(self.done)
        self.pushButton_load_add.clicked.connect(self.load_add)
        self.pushButton_load_done.clicked.connect(self.load_done)


    def add(self):
        name = self.lineEdit_task.text()
        instruction = self.lineEdit_instruction.text()
        description = self.lineEdit_description.text()
        conn = sqlite3.connect("task_data.db")
        cur = conn.cursor()
        task_info = [name, description, instruction]
        cur.execute('INSERT INTO task_data (name, description, instruction) VALUES (?,?,?)', task_info)
        conn.commit()
        conn.close()

    def load_add(self):
        connection = sqlite3.connect("task_data.db")
        query = "SELECT * FROM task_data"
        connection.execute(query)
        result = connection.execute(query)
        self.tableWidget_all.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_all.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_all.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()


    def done(self):
        name = self.lineEdit_task.text()
        instruction = self.lineEdit_instruction.text()
        description = self.lineEdit_description.text()
        conn = sqlite3.connect("doneTasks.db")
        cur = conn.cursor()
        task_info = [name, description, instruction]
        cur.execute('INSERT INTO doneTask (name, description, instruction) VALUES (?,?,?)', task_info)
        conn.commit()
        conn.close()

    def load_done(self):
        connection = sqlite3.connect("doneTasks.db")
        query = "SELECT * FROM doneTask"
        connection.execute(query)
        result = connection.execute(query)
        self.tableWidget_done.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_done.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_done.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("register.ui", self)
        self.stdreg.clicked.connect(self.createaccstudent)
        self.adreg.clicked.connect(self.createaccadmin)

    def createaccstudent(self):
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

    def createaccadmin(self):
        username = self.username.text()
        if self.password.text() == self.confirmpassword.text():
            password = self.password.text()
            confirmpassword = self.confirmpassword.text()
            if len(username) == 0 or len(password) == 0 or len(confirmpassword) == 0:
                QMessageBox.about(self, "Warning", "Please fill in all inputs.")

            elif password != confirmpassword:
                QMessageBox.about(self, "Warning", "Passwords do not match")
            else:
                conn = sqlite3.connect("shop_data1.db")
                cur = conn.cursor()
                user_info = [username, password]
                cur.execute('INSERT INTO login_info1 (username, password) VALUES (?,?)', user_info)
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