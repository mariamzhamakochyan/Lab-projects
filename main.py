"""" This file is head file with databases"""

import sys
import sqlite3
from PyQt5.QtWidgets import (QDialog, QApplication, QMessageBox, QTableWidget, QTableWidgetItem, QStackedWidget)
from PyQt5.uic import loadUi

User_name = ''


class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.adminPage = AdminAcc()
        self.studentPage = StudentAcc()
        loadUi("ui_design/login.ui", self)
        self.pushButton_stdlogin.clicked.connect(self.loginfunc)
        self.pushButtton_register.clicked.connect(self.gotocreate)

    def loginfunc(self):
        """This function is for log in """

        username = self.username.text()
        password = self.password.text()
        if len(username) == 0 or len(password) == 0:
            QMessageBox.about(self, "Warning", "Please Enter "
                                               "username and password")
        elif username == "coderepubliclab" and password == "code1111":
            widget.addWidget(self.adminPage)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            self.adminPage.show()

        else:
            conn = sqlite3.connect("database/user_data.db")
            cursor = conn.cursor()
            cursor.execute('SELECT password FROM login_info WHERE '
                           'username =\'' + username + "\'")
            row = cursor.fetchall()
            if row:
                widget.addWidget(self.studentPage)
                widget.setCurrentIndex(widget.currentIndex() + 1)

                global User_name
                User_name = username
                self.studentPage.show()
            else:
                QMessageBox.about(self, "Warning", "Wrong username or password")

    def gotocreate(self):
        """This function is for connecting log in and register tables"""

        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class AdminAcc(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("ui_design/admin.ui", self)
        self.pushButton_add.clicked.connect(self.addfunc)
        self.pushButton_list.clicked.connect(self.listfunc)
        self.pushButton_modify.clicked.connect(self.modifyfunc)
        self.pushButton_delet.clicked.connect(self.delfunc)
        # self.tableWidget.cellDoubleClicked.connect(self.selectedCell)

        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)


    def listfunc(self):
        """This function returns students data"""

        connection = sqlite3.connect("database/std_data.db")
        query = "SELECT * FROM student_data"
        connection.execute(query)
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,
                                         QTableWidgetItem(str(data)))
        connection.close()

    def addfunc(self):
        """This function is for adding students data"""

        id = self.lineEdit_id.text()
        name = self.lineEdit_first.text()
        surname = self.lineEdit_last.text()
        email = self.lineEdit_email.text()
        conn = sqlite3.connect("database/std_data.db")
        cur = conn.cursor()
        student_info = [id, name, surname, email]
        cur.execute('INSERT INTO student_data (id, name, surname, email) '
                    'VALUES (?,?,?,?)', student_info)
        if id.isalpha():
            QMessageBox.about(self, "Warning", "id must be a number")
        elif name.isnumeric() or surname.isnumeric():
            QMessageBox.about(self, "Warning", "First and last names must be alphabetic")
        conn.commit()
        conn.close()

    def delfunc(self):
        """This function is for deleting students from data"""

        id = self.lineEdit_id.text()
        conn = sqlite3.connect("database/std_data.db")
        cur = conn.cursor()
        cur.execute("DELETE from student_data WHERE id = :id",
                    {'id': id})
        conn.commit()
        conn.close()

    def modifyfunc(self):
        """This function is deesigned to modify student data"""

        id = self.lineEdit_id.text()
        name = self.lineEdit_first.text()
        surname = self.lineEdit_last.text()
        email = self.lineEdit_email.text()
        connection = sqlite3.connect('database/std_data.db')
        cur = connection.cursor()
        with connection:
            cur.execute("""UPDATE student_data SET name = :name,
             surname = :surname, email = :email
                           WHERE id = :id""",
                        {'name': name, 'surname': surname, 'id': id,
                         'email': email})


class StudentAcc(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("ui_design/student.ui", self)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_done.clicked.connect(self.done)
        self.pushButton_load_add.clicked.connect(self.load_add)
        self.pushButton_load_done.clicked.connect(self.load_done)

    def add(self):
        """This function is for adding tasks"""

        name = self.lineEdit_task.text()
        instruction = self.lineEdit_instruction.text()
        description = self.lineEdit_description.text()
        conn = sqlite3.connect("database/task_data.db")
        if name.isnumeric():
            QMessageBox.about(self, "Warning", "Task name can not contain numbers!")
        elif len(name) == 0 or len(instruction) == 0 or len(description) == 0:
            QMessageBox.about(self, "Warning", "Please fill in all inputs before adding.")
        else:
            cur = conn.cursor()
            task_info = [User_name, name, description, instruction]
            cur.execute('INSERT INTO task_data (username, name, desription, instruction)'
                    ' VALUES (?,?,?,?)', task_info)
            conn.commit()
            conn.close()

    def load_add(self):
        """This function returns added tasks"""

        connection = sqlite3.connect("database/task_data.db")
        print(User_name)
        query = f"SELECT name, desription, instruction FROM task_data WHERE username = '{User_name}'"
        connection.execute(query)
        result = connection.execute(query)
        self.tableWidget_all.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_all.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_all.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))
        connection.close()


    def done(self):
        """This function is for adding tasks that students done"""

        name = self.lineEdit_task.text()
        instruction = self.lineEdit_instruction.text()
        description = self.lineEdit_description.text()
        conn = sqlite3.connect("database/done_task.db")
        if name.isnumeric():
            QMessageBox.about(self, "Warning", "Task name can not contain numbers!")
        elif len(name) == 0 or len(instruction) == 0 or len(description) == 0:
            QMessageBox.about(self, "Warning", "Please fill in all inputs before adding.")
        else:
            cur = conn.cursor()
            task_info = [User_name, name, description, instruction]
            cur.execute('INSERT INTO done_task (username, name, description, instruction)'
                    ' VALUES (?,?,?,?)', task_info)
            conn.commit()
            conn.close()

    def load_done(self):
        """This function returns done tasks"""

        connection = sqlite3.connect("database/done_task.db")
        print(User_name)
        query = f"SELECT name, description, instruction FROM done_task WHERE username = '{User_name}'"
        connection.execute(query)
        result = connection.execute(query)
        self.tableWidget_done.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_done.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_done.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))
        connection.close()



class CreateAcc(QDialog):
    def __init__(self):
        super().__init__()
        self.registerPage = Login()
        loadUi("ui_design/register.ui", self)
        self.stdreg.clicked.connect(self.createaccstudent)
        self.pushButton_cancel.clicked.connect(self.close)

    def close(self):
        """This function returns log in page"""

        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def createaccstudent(self):
        """This function is creates users"""

        username = self.username.text()
        if self.password.text() == self.confirmpassword.text():
            password = self.password.text()
            confirmpassword = self.confirmpassword.text()
            if len(username) == 0 or len(password) == 0 or len(confirmpassword) == 0:
                QMessageBox.about(self, "Warning", "Please fill in all inputs.")
            elif username.isnumeric():
                QMessageBox.about(self, "Warning", "The username is unavailable, please do not use numbers!")
            elif len(username) < 3:
                QMessageBox.about(self, "Warning", "Username was too short.")
            elif len(password) < 8:
                QMessageBox.about(self, "Warning", "Minimum password length is 8")
            elif password != confirmpassword:
                QMessageBox.about(self, "Warning", "Passwords do not match")
            else:
                conn = sqlite3.connect("database/shop_data.db")
                cur = conn.cursor()
                user_info = [username, password]
                cur.execute('INSERT INTO login_info (username, password) '
                            'VALUES (?,?)', user_info)
                conn.commit()
                conn.close()
                self.registerPage = Login()
                widget.addWidget(self.registerPage)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                self.registerPage.show()


app = QApplication(sys.argv)
mainwindow = Login()
widget = QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(700)
widget.setFixedHeight(600)
widget.show()
app.exec_()
