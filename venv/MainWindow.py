# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(607, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 611, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 607, 23))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
        self.menu_CLOSE = QtWidgets.QMenu(self.menubar)
        self.menu_CLOSE.setObjectName("menu_CLOSE")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action123 = QtWidgets.QAction(MainWindow)
        self.action123.setObjectName("action123")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.addWinAction = QtWidgets.QAction(MainWindow)
        self.addWinAction.setCheckable(False)
        self.addWinAction.setShortcutVisibleInContextMenu(False)
        self.addWinAction.setObjectName("addWinAction")
        self.menu_F.addAction(self.action)
        self.menu_E.addAction(self.action123)
        self.menu_CLOSE.addSeparator()
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.menubar.addAction(self.menu_CLOSE.menuAction())
        self.toolBar.addAction(self.addWinAction)

        self.retranslateUi(MainWindow)
        self.action123.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_F.setTitle(_translate("MainWindow", "文件&F"))
        self.menu_E.setTitle(_translate("MainWindow", "编辑&E"))
        self.menu_CLOSE.setTitle(_translate("MainWindow", "关闭"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action123.setText(_translate("MainWindow", "123"))
        self.action123.setShortcut(_translate("MainWindow", "Ctrl+F4"))
        self.action.setText(_translate("MainWindow", "打开"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.addWinAction.setText(_translate("MainWindow", "添加窗体"))
        self.addWinAction.setToolTip(_translate("MainWindow", "添加窗体"))

