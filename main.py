import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi



def gotocreate():
    createacc = CreateAcc()
    widget.addWidget(createacc)
    widget.setCurrentIndex(widget.currentIndex() + 1)


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        self.adminPage = AdminAcc()
        self.studentPage = StudentAcc()
        loadUi("ui_design/login.ui", self)
        self.pushButton_stdlogin.clicked.connect(self.studentfunc)
        self.pushButton_adminlogin.clicked.connect(self.adminfunc)
        self.pushButtton_register.clicked.connect(gotocreate)

    def studentfunc(self):
        username = self.username.text()
        password = self.password.text()

        if len(username) == 0 or len(password) == 0:
            QMessageBox.about(self, "Warning", "Please Enter "
                                               "username and password")
        else:
            conn = sqlite3.connect("database/shop_data.db")
            cursor = conn.cursor()
            cursor.execute('SELECT password FROM login_info WHERE '
                           'username =\'' + username + "\'")
            row = cursor.fetchall()
            if row:
                widget.addWidget(self.studentPage)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                self.studentPage.show()
            else:
                QMessageBox.about(self, "Warning", "Wrong username or password")

    def adminfunc(self):
        username = self.username.text()
        password = self.password.text()

        if len(username) == 0 or len(password) == 0:
            QMessageBox.about(self, "Warning", "Please Enter username and password")
        else:
            conn = sqlite3.connect("database/shop_data1.db")
            cursor = conn.cursor()
            cursor.execute('SELECT password FROM login_info1 WHERE '
                           'username =\'' + username + "\'")
            row = cursor.fetchall()
            if row:
                widget.addWidget(self.adminPage)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                self.adminPage.show()
            else:
                QMessageBox.about(self, "Warning", "Wrong username or password")


class AdminAcc(QDialog):
    def __init__(self):
        super(AdminAcc, self).__init__()
        loadUi("ui_design/admin.ui", self)
        self.pushButton_add.clicked.connect(self.addfunc)
        self.pushButton_list.clicked.connect(self.listfunc)
        self.pushButton_modify.clicked.connect(self.modifyfunc)
        self.pushButton_delet.clicked.connect(self.delfunc)
        # self.tableWidget.cellDoubleClicked.connect(self.selectedCell)

        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)


    # def selectedCell(self):
    #     conn = sqlite3.connect("database/std_data.db")
    #
    #     cur = conn.cursor()
    #
    #     cur.execute("SELECT * FROM student_data WHERE id = :id",
    #                 {'id': id})
    #     try:
    #
    #         row = cur.fetchone()
    #         if row:
    #             self.lineEdit_id.setText(row[0])
    #             self.lineEdit_first.setText(row[1])
    #             self.lineEdit_last.setText(row[2])
    #             self.lineEdit_email.setText(row[3])
    #     except:
    #         print("Fill Failed")




    def listfunc(self):
        connection = sqlite3.connect("database/std_data.db")
        query = "SELECT * FROM student_data"
        connection.execute(query)
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,
                                         QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

    def addfunc(self):
        id = self.lineEdit_id.text()
        name = self.lineEdit_first.text()
        surname = self.lineEdit_last.text()
        email = self.lineEdit_email.text()
        conn = sqlite3.connect("database/std_data.db")
        cur = conn.cursor()
        student_info = [id, name, surname, email]
        cur.execute('INSERT INTO student_data (id, name, surname, email) '
                    'VALUES (?,?,?,?)', student_info)
        conn.commit()
        conn.close()

    def delfunc(self):
        id = self.lineEdit_id.text()
        conn = sqlite3.connect("database/std_data.db")
        cur = conn.cursor()
        cur.execute("DELETE from student_data WHERE id = :id",
                    {'id': id})
        conn.commit()
        conn.close()

    def modifyfunc(self):
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
        super(StudentAcc, self).__init__()
        loadUi("ui_design/student.ui", self)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_done.clicked.connect(self.done)
        self.pushButton_load_add.clicked.connect(self.load_add)
        self.pushButton_load_done.clicked.connect(self.load_done)


    def add(self):
        name = self.lineEdit_task.text()
        instruction = self.lineEdit_instruction.text()
        description = self.lineEdit_description.text()
        conn = sqlite3.connect("database/task_data.db")
        cur = conn.cursor()
        task_info = [name, description, instruction]
        cur.execute('INSERT INTO task_data (name, description, instruction)'
                    ' VALUES (?,?,?)', task_info)
        conn.commit()
        conn.close()

    def load_add(self):
        connection = sqlite3.connect("database/task_data.db")
        query = "SELECT * FROM task_data"
        connection.execute(query)
        result = connection.execute(query)
        self.tableWidget_all.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_all.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_all.setItem(row_number, column_number,
                                             QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

    def done(self):
        name = self.lineEdit_task.text()
        instruction = self.lineEdit_instruction.text()
        description = self.lineEdit_description.text()
        conn = sqlite3.connect("database/doneTasks.db")
        cur = conn.cursor()
        task_info = [name, description, instruction]
        cur.execute('INSERT INTO doneTask (name, description, instruction) '
                    'VALUES (?,?,?)', task_info)
        conn.commit()
        conn.close()

    def load_done(self):
        connection = sqlite3.connect("database/doneTasks.db")
        query = "SELECT * FROM doneTask"
        connection.execute(query)
        result = connection.execute(query)
        self.tableWidget_done.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_done.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_done.setItem(row_number,
                                              column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        self.registerPage = Login()
        loadUi("ui_design/register.ui", self)
        self.stdreg.clicked.connect(self.createaccstudent)
        self.adreg.clicked.connect(self.createaccadmin)
        self.pushButton_cancel.clicked.connect(self.close)

    def close(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

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
                conn = sqlite3.connect("database/shop_data1.db")
                cur = conn.cursor()
                user_info = [username, password]
                cur.execute('INSERT INTO login_info1 (username, password) '
                            'VALUES (?,?)', user_info)
                conn.commit()
                conn.close()
                widget.addWidget(self.registerPage)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                self.registerPage.show()


app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(700)
widget.setFixedHeight(600)
widget.show()
app.exec_()
