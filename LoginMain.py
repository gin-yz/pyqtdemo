# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginMain.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from LoginPrivate import Ui_Private
from LoginFilekey import Ui_Filekey

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Ui_LoginMain")
        MainWindow.resize(301, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 150, 158, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 301, 141))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        # self.frame_2 = QtWidgets.QFrame(self.splitter)
        # self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_2.setObjectName("frame_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.filekey = KEYFILE()
        self.private = PRIVATE()
        self.splitter.addWidget(self.filekey)
        self.pushButton_2.clicked.connect(lambda :self.change(self.pushButton_2.objectName()))
        self.pushButton.clicked.connect(lambda :self.change(self.pushButton.objectName()))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "区块链音乐版权系统登录"))
        self.pushButton_3.setText(_translate("MainWindow", "登录"))
        self.pushButton_4.setText(_translate("MainWindow", "关闭"))
        self.pushButton_2.setText(_translate("MainWindow", "KEYFILE登录"))
        self.pushButton.setText(_translate("MainWindow", "PRIVATE登录"))

    def change(self, name):
        if name == "pushButton_2":
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.filekey)

        if name == "pushButton":
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.private)


class KEYFILE(QtWidgets.QWidget, Ui_Filekey):
    def __init__(self):
        super(KEYFILE, self).__init__()
        self.setupUi(self)
        self.setMinimumWidth(301)
        self.setMinimumHeight(109)
        self.setMaximumWidth(301)
        self.setMaximumHeight(109)

class PRIVATE(QtWidgets.QWidget, Ui_Private):
    def __init__(self):
        super(PRIVATE, self).__init__()
        self.setupUi(self)
        self.setMinimumWidth(301)
        self.setMinimumHeight(109)
        self.setMaximumWidth(301)
        self.setMaximumHeight(109)

# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
