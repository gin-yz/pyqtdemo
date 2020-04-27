import json
import sys
from PyQt5 import QtWidgets
from eth_account import Account
from PyQt5.QtWidgets import QMessageBox
from LoginMain import Ui_MainWindow  # 由.UI文件生成.py文件后，导入创建的GUI类
from MainOP import Mainwindow

# QtWidgets.QMainWindow：继承该类方法
class Login_window(QtWidgets.QMainWindow, Ui_MainWindow):

    # __init__: 析构函数，也就是类被创建后就会预先加载的项目。
    # 马上运行，这个方法可以用来对你的对象做一些你希望的初始化。
    def __init__(self):
        # 这里需要重载一下Login_window，同时也包含了QtWidgets.QMainWindow的预加载项。
        super(Login_window, self).__init__()
        self.setupUi(self)

        # 将点击事件与槽函数进行连接
        self.pushButton_3.clicked.connect(self.btn_login_fuc)

    def keyPressEvent(self, event):
        if (event.key() == 16777220):
            self.btn_login_fuc()

    def btn_login_fuc(self):
        if self.splitter.widget(1).objectName() == 'Ui_Filekey':
            if self.splitter.widget(1).lineEdit.text().endswith(".json") ==False:
                reply = QMessageBox.warning(self, "警告", "请选择KEYFILE文件！")
                return
            if self.splitter.widget(1).lineEdit_2.text() == '':
                reply = QMessageBox.warning(self, "警告", "KEYFILE密码不能为空，请输入！")
                return
            with open(self.splitter.widget(1).lineEdit.text().replace("/", "\\"), 'r') as f:
                wallet = json.load(f)
            try:
                priv_key = Account.decrypt(wallet, self.splitter.widget(1).lineEdit_2.text()).hex()
                account = Account.privateKeyToAccount(priv_key)
            except Exception as e:
                reply = QMessageBox.warning(self, "警告", str(e))
                return
        if self.splitter.widget(1).objectName() == 'Ui_Private':
            if self.splitter.widget(1).lineEdit_2.text() =='':
                reply = QMessageBox.warning(self, "警告", "private不能为空，请输入！")
                return
            try:
                account = Account.from_key(self.splitter.widget(1).lineEdit_2.text())
            except Exception as e:
                reply = QMessageBox.warning(self, "警告", str(e))
                return
        mainwindow.address = account.address
        mainwindow.private = account._key_obj
        mainwindow.public = account._key_obj.public_key
        # print(account.address,account._key_obj,account._key_obj.public_key)
        mainwindow.lineEdit_2.setText(str(account.address))
        mainwindow.show()
        self.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Login_window()
    mainwindow = Mainwindow()
    window.show()
    sys.exit(app.exec_())
