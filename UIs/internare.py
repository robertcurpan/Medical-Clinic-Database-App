# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_internare.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_internare_dialog(object):
    def setupUi(self, internare_dialog):
        internare_dialog.setObjectName("internare_dialog")
        internare_dialog.resize(1400, 850)
        self.pacient_label = QtWidgets.QLabel(internare_dialog)
        self.pacient_label.setGeometry(QtCore.QRect(630, 30, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pacient_label.setFont(font)
        self.pacient_label.setObjectName("pacient_label")
        self.internare_next = QtWidgets.QPushButton(internare_dialog)
        self.internare_next.setGeometry(QtCore.QRect(1170, 730, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.internare_next.setFont(font)
        self.internare_next.setObjectName("internare_next")
        self.internare_back = QtWidgets.QPushButton(internare_dialog)
        self.internare_back.setGeometry(QtCore.QRect(50, 730, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.internare_back.setFont(font)
        self.internare_back.setObjectName("internare_back")
        self.pacient_insert_label = QtWidgets.QLabel(internare_dialog)
        self.pacient_insert_label.setGeometry(QtCore.QRect(110, 120, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pacient_insert_label.setFont(font)
        self.pacient_insert_label.setObjectName("pacient_insert_label")
        self.pacient_update_label = QtWidgets.QLabel(internare_dialog)
        self.pacient_update_label.setGeometry(QtCore.QRect(430, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pacient_update_label.setFont(font)
        self.pacient_update_label.setObjectName("pacient_update_label")
        self.pacient_delete_label = QtWidgets.QLabel(internare_dialog)
        self.pacient_delete_label.setGeometry(QtCore.QRect(800, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pacient_delete_label.setFont(font)
        self.pacient_delete_label.setObjectName("pacient_delete_label")
        self.internare_dataInternare_lineEdit = QtWidgets.QLineEdit(internare_dialog)
        self.internare_dataInternare_lineEdit.setGeometry(QtCore.QRect(30, 200, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.internare_dataInternare_lineEdit.setFont(font)
        self.internare_dataInternare_lineEdit.setObjectName("internare_dataInternare_lineEdit")
        self.internare_IDpacient_lineEdit = QtWidgets.QLineEdit(internare_dialog)
        self.internare_IDpacient_lineEdit.setGeometry(QtCore.QRect(30, 280, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.internare_IDpacient_lineEdit.setFont(font)
        self.internare_IDpacient_lineEdit.setObjectName("internare_IDpacient_lineEdit")
        self.internare_IDsectie_lineEdit = QtWidgets.QLineEdit(internare_dialog)
        self.internare_IDsectie_lineEdit.setGeometry(QtCore.QRect(30, 360, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.internare_IDsectie_lineEdit.setFont(font)
        self.internare_IDsectie_lineEdit.setObjectName("internare_IDsectie_lineEdit")
        self.label = QtWidgets.QLabel(internare_dialog)
        self.label.setGeometry(QtCore.QRect(30, 170, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(internare_dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 250, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(internare_dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 330, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.internare_IDboala_lineEdit = QtWidgets.QLineEdit(internare_dialog)
        self.internare_IDboala_lineEdit.setGeometry(QtCore.QRect(30, 440, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.internare_IDboala_lineEdit.setFont(font)
        self.internare_IDboala_lineEdit.setObjectName("internare_IDboala_lineEdit")
        self.label_4 = QtWidgets.QLabel(internare_dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 410, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.internare_IDmanopera_lineEdit = QtWidgets.QLineEdit(internare_dialog)
        self.internare_IDmanopera_lineEdit.setGeometry(QtCore.QRect(30, 520, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.internare_IDmanopera_lineEdit.setFont(font)
        self.internare_IDmanopera_lineEdit.setObjectName("internare_IDmanopera_lineEdit")
        self.label_5 = QtWidgets.QLabel(internare_dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 490, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pacient_delete_label_2 = QtWidgets.QLabel(internare_dialog)
        self.pacient_delete_label_2.setGeometry(QtCore.QRect(1120, 120, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pacient_delete_label_2.setFont(font)
        self.pacient_delete_label_2.setObjectName("pacient_delete_label_2")
        self.internare_visualize_textBrowser = QtWidgets.QTextBrowser(internare_dialog)
        self.internare_visualize_textBrowser.setGeometry(QtCore.QRect(1030, 180, 341, 451))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.internare_visualize_textBrowser.setFont(font)
        self.internare_visualize_textBrowser.setObjectName("internare_visualize_textBrowser")
        self.internare_insert_button = QtWidgets.QPushButton(internare_dialog)
        self.internare_insert_button.setGeometry(QtCore.QRect(80, 570, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.internare_insert_button.setFont(font)
        self.internare_insert_button.setObjectName("internare_insert_button")
        self.internare_viewRecords_button = QtWidgets.QPushButton(internare_dialog)
        self.internare_viewRecords_button.setGeometry(QtCore.QRect(1130, 650, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.internare_viewRecords_button.setFont(font)
        self.internare_viewRecords_button.setObjectName("internare_viewRecords_button")
        self.label_7 = QtWidgets.QLabel(internare_dialog)
        self.label_7.setGeometry(QtCore.QRect(800, 170, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.internare_deleteID_lineEdit = QtWidgets.QLineEdit(internare_dialog)
        self.internare_deleteID_lineEdit.setGeometry(QtCore.QRect(750, 200, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.internare_deleteID_lineEdit.setFont(font)
        self.internare_deleteID_lineEdit.setObjectName("internare_deleteID_lineEdit")
        self.internare_delete_button = QtWidgets.QPushButton(internare_dialog)
        self.internare_delete_button.setGeometry(QtCore.QRect(780, 250, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.internare_delete_button.setFont(font)
        self.internare_delete_button.setObjectName("internare_delete_button")
        self.internare_updateID_lineEdit = QtWidgets.QLineEdit(internare_dialog)
        self.internare_updateID_lineEdit.setGeometry(QtCore.QRect(370, 200, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.internare_updateID_lineEdit.setFont(font)
        self.internare_updateID_lineEdit.setObjectName("internare_updateID_lineEdit")
        self.label_8 = QtWidgets.QLabel(internare_dialog)
        self.label_8.setGeometry(QtCore.QRect(370, 170, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.internare_update_comboBox = QtWidgets.QComboBox(internare_dialog)
        self.internare_update_comboBox.setGeometry(QtCore.QRect(370, 290, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.internare_update_comboBox.setFont(font)
        self.internare_update_comboBox.setObjectName("internare_update_comboBox")
        self.internare_update_comboBox.addItem("")
        self.internare_update_comboBox.addItem("")
        self.internare_update_comboBox.addItem("")
        self.internare_update_comboBox.addItem("")
        self.internare_update_comboBox.addItem("")
        self.label_9 = QtWidgets.QLabel(internare_dialog)
        self.label_9.setGeometry(QtCore.QRect(370, 260, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.internare_update_button = QtWidgets.QPushButton(internare_dialog)
        self.internare_update_button.setGeometry(QtCore.QRect(440, 460, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.internare_update_button.setFont(font)
        self.internare_update_button.setObjectName("internare_update_button")
        self.internare_nouaValoare_lineEdit = QtWidgets.QLineEdit(internare_dialog)
        self.internare_nouaValoare_lineEdit.setGeometry(QtCore.QRect(370, 400, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.internare_nouaValoare_lineEdit.setFont(font)
        self.internare_nouaValoare_lineEdit.setPlaceholderText("")
        self.internare_nouaValoare_lineEdit.setObjectName("internare_nouaValoare_lineEdit")
        self.label_10 = QtWidgets.QLabel(internare_dialog)
        self.label_10.setGeometry(QtCore.QRect(370, 360, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.internare_feedback_textBrowser = QtWidgets.QTextBrowser(internare_dialog)
        self.internare_feedback_textBrowser.setGeometry(QtCore.QRect(320, 640, 681, 161))
        self.internare_feedback_textBrowser.setObjectName("internare_feedback_textBrowser")
        self.label_11 = QtWidgets.QLabel(internare_dialog)
        self.label_11.setGeometry(QtCore.QRect(590, 600, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.retranslateUi(internare_dialog)
        QtCore.QMetaObject.connectSlotsByName(internare_dialog)

    def retranslateUi(self, internare_dialog):
        _translate = QtCore.QCoreApplication.translate
        internare_dialog.setWindowTitle(_translate("internare_dialog", "Dialog"))
        self.pacient_label.setText(_translate("internare_dialog", "Internare"))
        self.internare_next.setText(_translate("internare_dialog", "Next"))
        self.internare_back.setText(_translate("internare_dialog", "Back"))
        self.pacient_insert_label.setText(_translate("internare_dialog", "Insert"))
        self.pacient_update_label.setText(_translate("internare_dialog", "Update"))
        self.pacient_delete_label.setText(_translate("internare_dialog", "Delete"))
        self.internare_dataInternare_lineEdit.setPlaceholderText(_translate("internare_dialog", "Ex: 10-MAR-2000"))
        self.internare_IDpacient_lineEdit.setPlaceholderText(_translate("internare_dialog", "Ex: 15"))
        self.internare_IDsectie_lineEdit.setPlaceholderText(_translate("internare_dialog", "Ex: 3"))
        self.label.setText(_translate("internare_dialog", "Data internare"))
        self.label_2.setText(_translate("internare_dialog", "ID Pacient"))
        self.label_3.setText(_translate("internare_dialog", "ID Sectie"))
        self.internare_IDboala_lineEdit.setPlaceholderText(_translate("internare_dialog", "Ex: 5"))
        self.label_4.setText(_translate("internare_dialog", "ID Boala"))
        self.internare_IDmanopera_lineEdit.setPlaceholderText(_translate("internare_dialog", "Ex: 5"))
        self.label_5.setText(_translate("internare_dialog", "ID Manopera"))
        self.pacient_delete_label_2.setText(_translate("internare_dialog", "Visualize Data"))
        self.internare_insert_button.setText(_translate("internare_dialog", "Insert"))
        self.internare_viewRecords_button.setText(_translate("internare_dialog", "View table records"))
        self.label_7.setText(_translate("internare_dialog", "Record ID"))
        self.internare_deleteID_lineEdit.setPlaceholderText(_translate("internare_dialog", "Ex: 10"))
        self.internare_delete_button.setText(_translate("internare_dialog", "Delete"))
        self.internare_updateID_lineEdit.setPlaceholderText(_translate("internare_dialog", "Ex: 10"))
        self.label_8.setText(_translate("internare_dialog", "Record ID"))
        self.internare_update_comboBox.setItemText(0, _translate("internare_dialog", "data_internare"))
        self.internare_update_comboBox.setItemText(1, _translate("internare_dialog", "Pacient_ID_pacient"))
        self.internare_update_comboBox.setItemText(2, _translate("internare_dialog", "Sectie_ID_sectie"))
        self.internare_update_comboBox.setItemText(3, _translate("internare_dialog", "Boala_ID_boala"))
        self.internare_update_comboBox.setItemText(4, _translate("internare_dialog", "Manopera_ID_manopera"))
        self.label_9.setText(_translate("internare_dialog", "Camp updatat"))
        self.internare_update_button.setText(_translate("internare_dialog", "Update"))
        self.label_10.setText(_translate("internare_dialog", "Noua valoare a campului"))
        self.label_11.setText(_translate("internare_dialog", "Feedback messages"))
