# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_sectie.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sectie_dialog(object):
    def setupUi(self, sectie_dialog):
        sectie_dialog.setObjectName("sectie_dialog")
        sectie_dialog.resize(1400, 850)
        self.pacient_label = QtWidgets.QLabel(sectie_dialog)
        self.pacient_label.setGeometry(QtCore.QRect(630, 30, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pacient_label.setFont(font)
        self.pacient_label.setObjectName("pacient_label")
        self.sectie_next = QtWidgets.QPushButton(sectie_dialog)
        self.sectie_next.setGeometry(QtCore.QRect(1170, 730, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sectie_next.setFont(font)
        self.sectie_next.setObjectName("sectie_next")
        self.sectie_back = QtWidgets.QPushButton(sectie_dialog)
        self.sectie_back.setGeometry(QtCore.QRect(50, 730, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sectie_back.setFont(font)
        self.sectie_back.setObjectName("sectie_back")
        self.pacient_insert_label = QtWidgets.QLabel(sectie_dialog)
        self.pacient_insert_label.setGeometry(QtCore.QRect(110, 120, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pacient_insert_label.setFont(font)
        self.pacient_insert_label.setObjectName("pacient_insert_label")
        self.pacient_update_label = QtWidgets.QLabel(sectie_dialog)
        self.pacient_update_label.setGeometry(QtCore.QRect(430, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pacient_update_label.setFont(font)
        self.pacient_update_label.setObjectName("pacient_update_label")
        self.pacient_delete_label = QtWidgets.QLabel(sectie_dialog)
        self.pacient_delete_label.setGeometry(QtCore.QRect(800, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pacient_delete_label.setFont(font)
        self.pacient_delete_label.setObjectName("pacient_delete_label")
        self.sectie_denumire_lineEdit = QtWidgets.QLineEdit(sectie_dialog)
        self.sectie_denumire_lineEdit.setGeometry(QtCore.QRect(30, 200, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sectie_denumire_lineEdit.setFont(font)
        self.sectie_denumire_lineEdit.setObjectName("sectie_denumire_lineEdit")
        self.label = QtWidgets.QLabel(sectie_dialog)
        self.label.setGeometry(QtCore.QRect(30, 170, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pacient_delete_label_2 = QtWidgets.QLabel(sectie_dialog)
        self.pacient_delete_label_2.setGeometry(QtCore.QRect(1120, 120, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pacient_delete_label_2.setFont(font)
        self.pacient_delete_label_2.setObjectName("pacient_delete_label_2")
        self.sectie_visualize_textBrowser = QtWidgets.QTextBrowser(sectie_dialog)
        self.sectie_visualize_textBrowser.setGeometry(QtCore.QRect(1030, 180, 341, 451))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sectie_visualize_textBrowser.setFont(font)
        self.sectie_visualize_textBrowser.setObjectName("sectie_visualize_textBrowser")
        self.sectie_viewRecords_button = QtWidgets.QPushButton(sectie_dialog)
        self.sectie_viewRecords_button.setGeometry(QtCore.QRect(1130, 650, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sectie_viewRecords_button.setFont(font)
        self.sectie_viewRecords_button.setObjectName("sectie_viewRecords_button")
        self.label_7 = QtWidgets.QLabel(sectie_dialog)
        self.label_7.setGeometry(QtCore.QRect(800, 170, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.sectie_deleteID_lineEdit = QtWidgets.QLineEdit(sectie_dialog)
        self.sectie_deleteID_lineEdit.setGeometry(QtCore.QRect(750, 200, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sectie_deleteID_lineEdit.setFont(font)
        self.sectie_deleteID_lineEdit.setObjectName("sectie_deleteID_lineEdit")
        self.sectie_delete_button = QtWidgets.QPushButton(sectie_dialog)
        self.sectie_delete_button.setGeometry(QtCore.QRect(780, 250, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sectie_delete_button.setFont(font)
        self.sectie_delete_button.setObjectName("sectie_delete_button")
        self.sectie_updateID_lineEdit = QtWidgets.QLineEdit(sectie_dialog)
        self.sectie_updateID_lineEdit.setGeometry(QtCore.QRect(370, 200, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sectie_updateID_lineEdit.setFont(font)
        self.sectie_updateID_lineEdit.setObjectName("sectie_updateID_lineEdit")
        self.label_8 = QtWidgets.QLabel(sectie_dialog)
        self.label_8.setGeometry(QtCore.QRect(370, 170, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.sectie_update_comboBox = QtWidgets.QComboBox(sectie_dialog)
        self.sectie_update_comboBox.setGeometry(QtCore.QRect(370, 290, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sectie_update_comboBox.setFont(font)
        self.sectie_update_comboBox.setObjectName("sectie_update_comboBox")
        self.sectie_update_comboBox.addItem("")
        self.label_9 = QtWidgets.QLabel(sectie_dialog)
        self.label_9.setGeometry(QtCore.QRect(370, 260, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.sectie_update_button = QtWidgets.QPushButton(sectie_dialog)
        self.sectie_update_button.setGeometry(QtCore.QRect(440, 460, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sectie_update_button.setFont(font)
        self.sectie_update_button.setObjectName("sectie_update_button")
        self.sectie_nouaValoare_lineEdit = QtWidgets.QLineEdit(sectie_dialog)
        self.sectie_nouaValoare_lineEdit.setGeometry(QtCore.QRect(370, 400, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sectie_nouaValoare_lineEdit.setFont(font)
        self.sectie_nouaValoare_lineEdit.setPlaceholderText("")
        self.sectie_nouaValoare_lineEdit.setObjectName("sectie_nouaValoare_lineEdit")
        self.label_10 = QtWidgets.QLabel(sectie_dialog)
        self.label_10.setGeometry(QtCore.QRect(370, 360, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.sectie_feedback_textBrowser = QtWidgets.QTextBrowser(sectie_dialog)
        self.sectie_feedback_textBrowser.setGeometry(QtCore.QRect(320, 640, 681, 161))
        self.sectie_feedback_textBrowser.setObjectName("sectie_feedback_textBrowser")
        self.label_11 = QtWidgets.QLabel(sectie_dialog)
        self.label_11.setGeometry(QtCore.QRect(590, 600, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.sectie_insert_button = QtWidgets.QPushButton(sectie_dialog)
        self.sectie_insert_button.setGeometry(QtCore.QRect(90, 260, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sectie_insert_button.setFont(font)
        self.sectie_insert_button.setObjectName("sectie_insert_button")

        self.retranslateUi(sectie_dialog)
        QtCore.QMetaObject.connectSlotsByName(sectie_dialog)

    def retranslateUi(self, sectie_dialog):
        _translate = QtCore.QCoreApplication.translate
        sectie_dialog.setWindowTitle(_translate("sectie_dialog", "Dialog"))
        self.pacient_label.setText(_translate("sectie_dialog", "Sectie"))
        self.sectie_next.setText(_translate("sectie_dialog", "Next"))
        self.sectie_back.setText(_translate("sectie_dialog", "Back"))
        self.pacient_insert_label.setText(_translate("sectie_dialog", "Insert"))
        self.pacient_update_label.setText(_translate("sectie_dialog", "Update"))
        self.pacient_delete_label.setText(_translate("sectie_dialog", "Delete"))
        self.sectie_denumire_lineEdit.setPlaceholderText(_translate("sectie_dialog", "Ex: Cardiologie"))
        self.label.setText(_translate("sectie_dialog", "Denumire"))
        self.pacient_delete_label_2.setText(_translate("sectie_dialog", "Visualize Data"))
        self.sectie_viewRecords_button.setText(_translate("sectie_dialog", "View table records"))
        self.label_7.setText(_translate("sectie_dialog", "Record ID"))
        self.sectie_deleteID_lineEdit.setPlaceholderText(_translate("sectie_dialog", "Ex: 5"))
        self.sectie_delete_button.setText(_translate("sectie_dialog", "Delete"))
        self.sectie_updateID_lineEdit.setPlaceholderText(_translate("sectie_dialog", "Ex: 5"))
        self.label_8.setText(_translate("sectie_dialog", "Record ID"))
        self.sectie_update_comboBox.setItemText(0, _translate("sectie_dialog", "denumire"))
        self.label_9.setText(_translate("sectie_dialog", "Camp updatat"))
        self.sectie_update_button.setText(_translate("sectie_dialog", "Update"))
        self.label_10.setText(_translate("sectie_dialog", "Noua valoare a campului"))
        self.label_11.setText(_translate("sectie_dialog", "Feedback messages"))
        self.sectie_insert_button.setText(_translate("sectie_dialog", "Insert"))