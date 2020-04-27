from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from Main_window import Ui_MainWindow
from encryptmodule import encrypt_run
from decryptmodule import decrypt_run

class EncryptThread(QThread):
    update_date = pyqtSignal(str)
    message_date = pyqtSignal(int, str)

    def __init__(self, path):
        super(EncryptThread, self).__init__()
        self.path = path

    def run(self):
        self.update_date.emit(str('开始加密，请稍等片刻'))
        try:
            msg, name = encrypt_run(self.path)
            # print(msg, name)
        except Exception as e:
            self.message_date.emit(1, str(e))
            return
        if msg:
            self.update_date.emit(str('加密完成，原目录下生成.copyright .key文件'))
            self.message_date.emit(2, str('加密完成，加密后的文件在%s，加密后的密钥在%s' % (name + '.copyright', name + '.key')))
            return


class DecryptThread(QThread):
    update_date = pyqtSignal(str)
    message_date = pyqtSignal(int, str)

    def __init__(self, copyright, key,private):
        super(DecryptThread, self).__init__()
        self.copyright = copyright
        self.key = key
        self.private = private

    def run(self):
        self.update_date.emit(str('开始解密，请稍等片刻'))
        try:
            msg, path = decrypt_run(self.copyright,self.key,self.private)
            # print(msg, path)
        except Exception as e:
            self.message_date.emit(1, str(e))
            return
        if msg:
            self.update_date.emit(str('解密完成，原加密文件目录下生成版权文件'))
            self.message_date.emit(2, str('解密完成，解密后的文件在%s' % path))
            return


class Mainwindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self.statusBar.showMessage('欢迎使用本系统！')

        # 将点击事件与槽函数进行连接
        self.pushButton.clicked.connect(lambda: self.openfile(1, 'music copyright files(*)'))
        self.pushButton_3.clicked.connect(lambda: self.openfile(2, 'encrypt copyright files(*)'))
        self.pushButton_5.clicked.connect(lambda: self.openfile(3, 'encrypt key files(*)'))

        self.pushButton_2.clicked.connect(lambda: self.encryptwork(self.lineEdit.text().replace("/", "\\")))
        self.pushButton_6.clicked.connect(lambda: self.decryptwork(self.lineEdit_3.text().replace("/", "\\"),
                                                                   self.lineEdit_4.text().replace("/", "\\")))

    def handleDisplay(self, data):
        self.statusBar.showMessage(data)

    def encryptwork(self, data):
        if data == '':
            reply = QMessageBox.warning(self, "警告", '请选择加密文件！')
            return
        self.encryptthread = EncryptThread(data)
        self.encryptthread.update_date.connect(self.handleDisplay)
        self.encryptthread.message_date.connect(self.messageBox)
        self.encryptthread.start()

    def decryptwork(self, copyright, key):
        if (copyright == '') | (key == ''):
            reply = QMessageBox.warning(self, "警告", '请选择对应解密的文件！')
            return
        self.decryptthread = DecryptThread(copyright, key, self.private)
        self.decryptthread.update_date.connect(self.handleDisplay)
        self.decryptthread.message_date.connect(self.messageBox)
        self.decryptthread.start()

    def messageBox(self, type, data):
        if type == 1:
            reply = QMessageBox.warning(self, "警告", data)
        if type == 2:
            reply = QMessageBox.information(self, "完成", str(data), QMessageBox.Yes)
            self.lineEdit.setText('')
            self.lineEdit_3.setText('')
            self.lineEdit_4.setText('')



    def openfile(self, line, suffix):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', suffix)
        if (line == 1): self.lineEdit.setText(openfile_name[0])
        if (line == 2): self.lineEdit_3.setText(openfile_name[0])
        if (line == 3): self.lineEdit_4.setText(openfile_name[0])
