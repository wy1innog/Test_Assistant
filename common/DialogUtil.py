from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QPushButton



def showEmptyMessageBox(msg):
    dialog = QDialog()
    dialog.setMinimumSize(311, 140)
    dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    icon = 'D:\\ihblu\\wyrepo\\Test_Assistant\\img\\icon.ico'
    dialog.setWindowIcon(QIcon(icon))
    font1 = QtGui.QFont()
    font1.setPointSize(10)
    btn = QPushButton("ok", dialog)
    btn.setGeometry(QtCore.QRect(110, 100, 91, 40))
    btn.setFont(font1)
    btn.clicked.connect(dialog.close)

    label_mes = QtWidgets.QLabel(dialog)
    label_mes.setGeometry(QtCore.QRect(80, 40, 151, 41))
    font = QtGui.QFont()
    font.setFamily("微软雅黑")
    font.setPointSize(12)
    label_mes.setFont(font)
    label_mes.setText(msg)

    dialog.setWindowTitle("提示")
    dialog.exec_()