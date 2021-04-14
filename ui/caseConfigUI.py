# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caseConfigUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class TabBar(QtWidgets.QTabBar):
    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt);
            painter.restore()

class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
        self.setTabBar(TabBar(self))
        self.setTabPosition(QtWidgets.QTabWidget.West)

class ProxyStyle(QtWidgets.QProxyStyle):
    def drawControl(self, element, opt, painter, widget):
        if element == QtWidgets.QStyle.CE_TabBarTabLabel:
            ic = self.pixelMetric(QtWidgets.QStyle.PM_TabBarIconSize)
            r = QtCore.QRect(opt.rect)
            w =  0 if opt.icon.isNull() else opt.rect.width() + self.pixelMetric(QtWidgets.QStyle.PM_TabBarIconSize)
            r.setHeight(opt.fontMetrics.width(opt.text) + w)
            r.moveBottom(opt.rect.bottom())
            opt.rect = r
        QtWidgets.QProxyStyle.drawControl(self, element, opt, painter, widget)


class Ui_Case_config(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(592, 567)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)

        QtWidgets.QApplication.setStyle(ProxyStyle())

        # 调用重绘的TabWidget使Tab变成文字水平显示  -_- but目前无法显示tab名称
        # self.tabWidget = TabWidget(self.centralwidget)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)

        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 571, 491))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        # self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Tab_call_set = QtWidgets.QWidget()
        self.Tab_call_set.setMinimumSize(QtCore.QSize(0, 0))
        self.Tab_call_set.setObjectName("Tab_call_set")
        self.Label_call_number = QtWidgets.QLabel(self.Tab_call_set)
        self.Label_call_number.setGeometry(QtCore.QRect(80, 60, 109, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setWeight(50)
        self.Label_call_number.setFont(font)
        self.Label_call_number.setObjectName("Label_call_number")
        self.Ledit_call_number = QtWidgets.QLineEdit(self.Tab_call_set)
        self.Ledit_call_number.setGeometry(QtCore.QRect(214, 48, 266, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setWeight(50)
        self.Ledit_call_number.setFont(font)
        self.Ledit_call_number.setObjectName("Ledit_call_number")
        self.Ledit_call_interval = QtWidgets.QLineEdit(self.Tab_call_set)
        self.Ledit_call_interval.setGeometry(QtCore.QRect(214, 130, 266, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setWeight(50)
        self.Ledit_call_interval.setFont(font)
        self.Ledit_call_interval.setObjectName("Ledit_call_interval")
        self.Ledit_call_hold = QtWidgets.QLineEdit(self.Tab_call_set)
        self.Ledit_call_hold.setGeometry(QtCore.QRect(214, 210, 266, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setWeight(50)
        self.Ledit_call_hold.setFont(font)
        self.Ledit_call_hold.setObjectName("Ledit_call_hold")
        self.Label_call_interval = QtWidgets.QLabel(self.Tab_call_set)
        self.Label_call_interval.setGeometry(QtCore.QRect(80, 140, 121, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setWeight(50)
        self.Label_call_interval.setFont(font)
        self.Label_call_interval.setObjectName("Label_call_interval")
        self.Label_call_hold = QtWidgets.QLabel(self.Tab_call_set)
        self.Label_call_hold.setGeometry(QtCore.QRect(80, 220, 121, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setWeight(50)
        self.Label_call_hold.setFont(font)
        self.Label_call_hold.setObjectName("Label_call_hold")
        self.tabWidget.addTab(self.Tab_call_set, "通话")

        self.Tab_WIFI_set = QtWidgets.QWidget()
        self.Tab_WIFI_set.setObjectName("Tab_WIFI_set")
        self.Label_WIFI_SSID = QtWidgets.QLabel(self.Tab_WIFI_set)
        self.Label_WIFI_SSID.setGeometry(QtCore.QRect(80, 60, 109, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setWeight(50)
        self.Label_WIFI_SSID.setFont(font)
        self.Label_WIFI_SSID.setObjectName("Label_WIFI_SSID")
        self.Ledit_WIFI_SSID = QtWidgets.QLineEdit(self.Tab_WIFI_set)
        self.Ledit_WIFI_SSID.setGeometry(QtCore.QRect(214, 48, 266, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setWeight(50)
        self.Ledit_WIFI_SSID.setFont(font)
        self.Ledit_WIFI_SSID.setObjectName("Ledit_WIFI_SSID")
        self.Ledit_WIFI_PWD = QtWidgets.QLineEdit(self.Tab_WIFI_set)
        self.Ledit_WIFI_PWD.setGeometry(QtCore.QRect(214, 130, 266, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setWeight(50)
        self.Ledit_WIFI_PWD.setFont(font)
        self.Ledit_WIFI_PWD.setObjectName("Ledit_WIFI_PWD")
        self.Label_WIFI_PWD = QtWidgets.QLabel(self.Tab_WIFI_set)
        self.Label_WIFI_PWD.setGeometry(QtCore.QRect(80, 142, 109, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setWeight(50)
        self.Label_WIFI_PWD.setFont(font)
        self.Label_WIFI_PWD.setObjectName("Label_WIFI_PWD")
        self.Ledit_WIFI_interval = QtWidgets.QLineEdit(self.Tab_WIFI_set)
        self.Ledit_WIFI_interval.setGeometry(QtCore.QRect(214, 210, 266, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setWeight(50)
        self.Ledit_WIFI_interval.setFont(font)
        self.Ledit_WIFI_interval.setObjectName("Ledit_WIFI_interval")
        self.Label_WIFI_interval = QtWidgets.QLabel(self.Tab_WIFI_set)
        self.Label_WIFI_interval.setGeometry(QtCore.QRect(80, 222, 121, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setWeight(50)
        self.Label_WIFI_interval.setFont(font)
        self.Label_WIFI_interval.setObjectName("Label_WIFI_interval")
        self.tabWidget.addTab(self.Tab_WIFI_set, "WIFI")

        self.Tab_BT_set = QtWidgets.QWidget()
        self.Tab_BT_set.setObjectName("Tab_BT_set")
        self.Ledit_BT_name = QtWidgets.QLineEdit(self.Tab_BT_set)
        self.Ledit_BT_name.setGeometry(QtCore.QRect(214, 48, 266, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setWeight(50)
        self.Ledit_BT_name.setFont(font)
        self.Ledit_BT_name.setObjectName("Ledit_BT_name")
        self.Label_BT_name = QtWidgets.QLabel(self.Tab_BT_set)
        self.Label_BT_name.setGeometry(QtCore.QRect(80, 60, 109, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setWeight(50)
        self.Label_BT_name.setFont(font)
        self.Label_BT_name.setObjectName("Label_BT_name")
        self.tabWidget.addTab(self.Tab_BT_set, "蓝牙")

        self.Btn_config_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_config_cancel.setGeometry(QtCore.QRect(460, 520, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Btn_config_cancel.setFont(font)
        self.Btn_config_cancel.setObjectName("Btn_config_cancel")
        self.Btn_config_ok = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_config_ok.setGeometry(QtCore.QRect(350, 520, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Btn_config_ok.setFont(font)
        self.Btn_config_ok.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        # self.Btn_config_ok.setCheckable(False)
        # self.Btn_config_ok.setChecked(False)
        # self.Btn_config_ok.setAutoExclusive(False)
        # self.Btn_config_ok.setAutoDefault(True)
        self.Btn_config_ok.setObjectName("Btn_config_ok")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "配置"))
        self.Label_call_number.setText(_translate("MainWindow", "对端电话"))
        self.Label_call_interval.setText(_translate("MainWindow", "通话间隔(秒)"))
        self.Label_call_hold.setText(_translate("MainWindow", "驻留时长(秒)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_call_set), _translate("MainWindow", "通话"))
        self.Label_WIFI_SSID.setText(_translate("MainWindow", "SSID"))
        self.Label_WIFI_PWD.setText(_translate("MainWindow", "密码"))
        self.Label_WIFI_interval.setText(_translate("MainWindow", "测试间隔(秒)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_WIFI_set), _translate("MainWindow", "WIFI"))
        self.Label_BT_name.setText(_translate("MainWindow", "蓝牙名"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_BT_set), _translate("MainWindow", "蓝牙"))
        self.Btn_config_cancel.setText(_translate("MainWindow", "取消"))
        self.Btn_config_ok.setText(_translate("MainWindow", "确定"))