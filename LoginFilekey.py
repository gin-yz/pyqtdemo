# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginFilekey.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_Filekey(object):
    def setupUi(self, Ui_Filekey):
        Ui_Filekey.setObjectName("Ui_Filekey")
        Ui_Filekey.resize(300, 179)
        # self.centralwidget = QtWidgets.QWidget(Ui_Filekey)
        # self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(Ui_Filekey)
        # self.frame.setGeometry(QtCore.QRect(0, 32, 301, 109))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 278, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('请输入文件路径')
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("请输入KEYFILE密码")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        # Ui_Filekey.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.openfile)

        self.retranslateUi(Ui_Filekey)
        QtCore.QMetaObject.connectSlotsByName(Ui_Filekey)

    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'JSON files(*.json)')
        self.lineEdit.setText(openfile_name[0])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "KEYFILE："))
        self.pushButton.setText(_translate("MainWindow", "选择文件"))
        self.label_2.setText(_translate("MainWindow", "KEYFILE密码："))

