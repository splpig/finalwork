# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_stu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_stu(object):
    def setupUi(self, MainWindow_stu):
        MainWindow_stu.setObjectName("MainWindow_stu")
        MainWindow_stu.resize(800, 600)
        MainWindow_stu.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow_stu.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        MainWindow_stu.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow_stu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 121, 30))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 500, 93, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 500, 93, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 500, 93, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 20, 141, 26))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 500, 93, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(30, 60, 341, 411))
        self.tableView.setObjectName("tableView")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(445, 60, 331, 411))
        self.tableView_2.setObjectName("tableView_2")
        MainWindow_stu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_stu)
        self.statusbar.setObjectName("statusbar")
        MainWindow_stu.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow_stu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        MainWindow_stu.setMenuBar(self.menubar)
        self.action1_1 = QtWidgets.QAction(MainWindow_stu)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(11)
        self.action1_1.setFont(font)
        self.action1_1.setObjectName("action1_1")
        self.action2_1 = QtWidgets.QAction(MainWindow_stu)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(11)
        self.action2_1.setFont(font)
        self.action2_1.setObjectName("action2_1")
        self.action3_1 = QtWidgets.QAction(MainWindow_stu)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(11)
        self.action3_1.setFont(font)
        self.action3_1.setObjectName("action3_1")
        self.action1 = QtWidgets.QAction(MainWindow_stu)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(11)
        self.action1.setFont(font)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow_stu)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(11)
        self.action2.setFont(font)
        self.action2.setObjectName("action2")
        self.action = QtWidgets.QAction(MainWindow_stu)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(11)
        self.action.setFont(font)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow_stu)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(11)
        self.action_2.setFont(font)
        self.action_2.setObjectName("action_2")
        self.menu.addSeparator()
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow_stu)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_stu)

    def retranslateUi(self, MainWindow_stu):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_stu.setWindowTitle(_translate("MainWindow_stu", "MainWindow"))
        self.label.setText(_translate("MainWindow_stu", "新书推荐"))
        self.pushButton.setText(_translate("MainWindow_stu", "借阅查询"))
        self.pushButton_2.setText(_translate("MainWindow_stu", "图书借阅"))
        self.pushButton_3.setText(_translate("MainWindow_stu", "图书归还"))
        self.label_2.setText(_translate("MainWindow_stu", "借阅排行榜"))
        self.pushButton_4.setText(_translate("MainWindow_stu", "图书查询"))
        self.menu.setTitle(_translate("MainWindow_stu", "设置"))
        self.action1_1.setText(_translate("MainWindow_stu", "个人借阅查询"))
        self.action2_1.setText(_translate("MainWindow_stu", "图书借阅"))
        self.action3_1.setText(_translate("MainWindow_stu", "图书归还"))
        self.action1.setText(_translate("MainWindow_stu", "借阅排行"))
        self.action2.setText(_translate("MainWindow_stu", "图书搜索"))
        self.action.setText(_translate("MainWindow_stu", "密码更改"))
        self.action_2.setText(_translate("MainWindow_stu", "注销"))
