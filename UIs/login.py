# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(1400, 850)
        self.login_console_textBrowser = QtWidgets.QTextBrowser(Login)
        self.login_console_textBrowser.setGeometry(QtCore.QRect(40, 480, 1321, 321))
        self.login_console_textBrowser.setObjectName("login_console_textBrowser")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(630, 40, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(90, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(90, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.login_username_lineEdit = QtWidgets.QLineEdit(Login)
        self.login_username_lineEdit.setGeometry(QtCore.QRect(220, 170, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_username_lineEdit.setFont(font)
        self.login_username_lineEdit.setObjectName("login_username_lineEdit")
        self.login_password_lineEdit = QtWidgets.QLineEdit(Login)
        self.login_password_lineEdit.setGeometry(QtCore.QRect(222, 230, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_password_lineEdit.setFont(font)
        self.login_password_lineEdit.setObjectName("login_password_lineEdit")
        self.login_login_button = QtWidgets.QPushButton(Login)
        self.login_login_button.setGeometry(QtCore.QRect(290, 290, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_login_button.setFont(font)
        self.login_login_button.setObjectName("login_login_button")
        self.label_4 = QtWidgets.QLabel(Login)
        self.label_4.setGeometry(QtCore.QRect(50, 430, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.label.setText(_translate("Login", "Login Screen"))
        self.label_2.setText(_translate("Login", "Username:"))
        self.label_3.setText(_translate("Login", "Password:"))
        self.login_login_button.setText(_translate("Login", "Login"))
        self.label_4.setText(_translate("Login", "Console"))
