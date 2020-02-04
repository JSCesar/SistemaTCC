# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JanelaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ListaAct = QtWidgets.QListWidget(self.centralwidget)
        self.ListaAct.setGeometry(QtCore.QRect(250, 410, 521, 111))
        self.ListaAct.setObjectName("ListaAct")
        self.btn_carregar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carregar.setGeometry(QtCore.QRect(10, 480, 101, 31))
        self.btn_carregar.setObjectName("btn_carregar")
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(250, 10, 521, 341))
        self.Image.setFrameShape(QtWidgets.QFrame.Box)
        self.Image.setLineWidth(3)
        self.Image.setText("")
        self.Image.setScaledContents(False)
        self.Image.setAlignment(QtCore.Qt.AlignCenter)
        self.Image.setObjectName("Image")
        self.btn_aplicar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_aplicar.setGeometry(QtCore.QRect(0, 420, 121, 41))
        self.btn_aplicar.setObjectName("btn_aplicar")
        self.btn_remover = QtWidgets.QPushButton(self.centralwidget)
        self.btn_remover.setGeometry(QtCore.QRect(130, 420, 111, 41))
        self.btn_remover.setObjectName("btn_remover")
        self.btn_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_salvar.setGeometry(QtCore.QRect(130, 480, 101, 31))
        self.btn_salvar.setObjectName("btn_salvar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 786, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_carregar.setText(_translate("MainWindow", "Carregar"))
        self.btn_aplicar.setText(_translate("MainWindow", "Aplicar"))
        self.btn_remover.setText(_translate("MainWindow", "Remover"))
        self.btn_salvar.setText(_translate("MainWindow", "Salvar"))

