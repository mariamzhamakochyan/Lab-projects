"""This file create db and table and is connected with sql"""

import sqlite3


conn = sqlite3.connect('database/std_data.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS student_data (
            id INTEGER,
            name TEXT,
            surname TEXT
            email 
)""")


def delfunc(self):
    """This function delete contact"""

    name = self.lineedit_name.text()
    student_data = listfunc()
    lst = []
    for cont in student_data:
        lst.append(list(cont))

    lst_name_surname = []  # the same name's list
    count = 0  # names count
    for element in lst:
        if element[0] == name:
            count += 1
            phone_number = element[2]
            lst_name_surname.append([name, element[1], element[2]])

    if count == 0:
        self.label_txt.setText("There is no such contact")
        self.label_txt.setStyleSheet("color: red")
        self.label_txt.setFont(QFont("Arial", 11))
        self.label_txt.move(5, 0)
        self.label_txt.resize(240, 20)
    elif count == 1:
        # delete automatically
        delete_contact(phone_number)
        self.close()
        obj = contact_view.CreateTable()
        obj.close_table()
    else:
        # ask which contact delete
        self.combo_box = QComboBox(self)
        self.combo_box.resize(200, 25)
        self.combo_box.move(50, 120)
        self.combo_box.show()
        for element in lst_name_surname:
            self.combo_box.addItem(f"{element[0]} {element[1]}")
        self.combo_box.activated.connect(partial(self.check_index, lst_name_surname))








#
# def all_contacts():
#     """This function return all contacts with list"""
#
#     connection = sqlite3.connect('database/contacts.db')
#     cur = connection.cursor()
#     with connection:
#         cur.execute("SELECT * FROM contacts")
#         contact = cur.fetchall()
#         lst = []
#         for cont in contact:
#             lst.append(cont)
#         return lst

#
# def insert_contact(contact):
#     """This function insert a contact in table"""
#
#     connection = sqlite3.connect('database/contacts.db')
#     cur = connection.cursor()
#     with connection:
#         cur.execute("INSERT INTO contacts VALUES (:name, :surname, :phone_number, :address)",
#                     {'name': contact.name, 'surname': contact.surname,
#                      'phone_number': contact.phone_number, 'address': contact.address})
#

def modifyfunc(student_data, name, surname, email):
    """This function update the contact"""

    connection = sqlite3.connect('database/std_data.db')
    cur = connection.cursor()
    with connection:
        cur.execute("""UPDATE student_data SET name = :name, surname = :surname, email = :email
                    WHERE id = :id""",
                    {'name': name, 'surname': surname, 'id': student_data.id,
                     'email': email})


def delfunc(id):
    """This function delete the contact"""

    conn = sqlite3.connect('database/std_data.db')
    cur = conn.cursor()
    with conn:
        cur.execute("DELETE from student_data WHERE id = :id",
                    {'id': id})

conn.commit()
conn.close()



import mysql.connector
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import DBGUI

class MainClass(QDialog, DBGUI.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_load.clicked.connect(self.loadDB)
        self.pushButton_add.clicked.connect(self.addData)
        self.pushButton_delete.clicked.connect(self.DeleteData)
        self.pushButton_update.clicked.connect(self.updateData)
        self.tableWidget.cellDoubleClicked.connect(self.selectedCell)

        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)


    def loadDB(self):
        connection = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "Usopen97!",
            database="Employees"
        )

        query = "SELECT ID, empF, empL, email FROM account"
        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        cur.close()

    def addData(self):
        connection = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "Usopen97!",
            database="Employees"
        )

        ID = self.lineEdit_id.text()
        firstN = self.lineEdit_first.text()
        lastN = self.lineEdit_last.text()
        email = self.lineEdit_email.text()

        cur = connection.cursor()

        insertq = "INSERT INTO account (id, empF, empL, email) VALUES (%s, %s, %s, %s)"
        values = (ID, firstN, lastN, email,)

        try:
            cur.execute(insertq, values)
            connection.commit()
            print("Success")
        except:
            print("failed")

    def DeleteData(self):
        connection = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "Usopen97!",
            database="Employees"
        )

        cur = connection.cursor()
        email = self.lineEdit_email.text()
        deleteq = "DELETE FROM account WHERE email = %s"
        values = (email,)

        try:
            cur.execute(deleteq, values)
            connection.commit()
            print("success")
        except:
            print("failed")

    def updateData(self):
        connection = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "Usopen97!",
            database="Employees"
        )

        cur = connection.cursor()
        firstN = self.lineEdit_first.text()
        lastN = self.lineEdit_last.text()
        email = self.lineEdit_email.text()
        updateq = "UPDATE account SET empF = %s, empL = %s WHERE email = %s"
        values = (firstN, lastN, email,)

        try:
            cur.execute(updateq, values)
            connection.commit()
            print("Success")
        except:
            print("failed")

    def selectedCell(self):
        connection = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "Usopen97!",
            database="Employees"
        )

        cur = connection.cursor()

        self.index = self.tableWidget.selectedItems()

        query = "SELECT ID, empF, empL, email FROM account WHERE ID = %s"
        value = (self.index[0].text(),)

        try:
            cur.execute(query, value)
            row = cur.fetchone()

            if row:
                self.lineEdit_id.setText(row[0])
                self.lineEdit_first.setText(row[1])
                self.lineEdit_last.setText(row[2])
                self.lineEdit_email.setText(row[3])
        except:
            print("Fill Failed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ims = MainClass()
    ims.show()
    app.exec_()


















import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Usopen97!",
    database="Employee"
)


c = connection.cursor()
#Create db
query = "CREATE DATABASE Employee;"
c.execute(query)

#table
query = "CREATE TABLE account (id VARCHAR(100), empF VARCHAR(100), empL VARCHAR(100), email VARCHAR(200))"
c.execute(query)


#insert
query = "INSERT INTO account (id, empF, empL, email) VALUES (%s, %s, %s, %s)"
value = ('1', 'Matt', 'Lee', 'mattlee@email.com')
c.execute(query, value)
connection.commit()



#Update
query = "UPDATE account SET empF= 'Matthew' WHERE email = %s"
value = ('mattlee@email.com',)
c.execute(query, value)
connection.commit()


#Delete
query = "DELETE FROM account WHERE email = %s"
value = ('mattlee@email.com',)
c.execute(query, value)
connection.commit()



##Select
query = "SELECT * FROM account"
c.execute(query)
result = c.fetchall()
print(result)