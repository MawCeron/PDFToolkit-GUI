# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PDFToolKit.ui'
#
# Created: Thu Jun  7 11:18:03 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../share/icons/PDFToolKit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(597, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tbOutput = QtGui.QLineEdit(self.groupBox_2)
        self.tbOutput.setObjectName(_fromUtf8("tbOutput"))
        self.gridLayout_2.addWidget(self.tbOutput, 0, 0, 1, 1)
        self.btSearch = QtGui.QPushButton(self.groupBox_2)
        self.btSearch.setObjectName(_fromUtf8("btSearch"))
        self.gridLayout_2.addWidget(self.btSearch, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 3)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidget = QtGui.QListWidget(self.groupBox)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btUp = QtGui.QPushButton(self.groupBox)
        self.btUp.setObjectName(_fromUtf8("btUp"))
        self.verticalLayout.addWidget(self.btUp)
        self.btDown = QtGui.QPushButton(self.groupBox)
        self.btDown.setObjectName(_fromUtf8("btDown"))
        self.verticalLayout.addWidget(self.btDown)
        spacerItem1 = QtGui.QSpacerItem(20, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btAdd = QtGui.QPushButton(self.groupBox)
        self.btAdd.setObjectName(_fromUtf8("btAdd"))
        self.verticalLayout.addWidget(self.btAdd)
        self.btQuit = QtGui.QPushButton(self.groupBox)
        self.btQuit.setObjectName(_fromUtf8("btQuit"))
        self.verticalLayout.addWidget(self.btQuit)
        self.btQuitAll = QtGui.QPushButton(self.groupBox)
        self.btQuitAll.setObjectName(_fromUtf8("btQuitAll"))
        self.verticalLayout.addWidget(self.btQuitAll)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 3)
        self.btExit = QtGui.QPushButton(self.centralwidget)
        self.btExit.setObjectName(_fromUtf8("btExit"))
        self.gridLayout_3.addWidget(self.btExit, 2, 2, 1, 1)
        self.btMerge = QtGui.QPushButton(self.centralwidget)
        self.btMerge.setObjectName(_fromUtf8("btMerge"))
        self.gridLayout_3.addWidget(self.btMerge, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionAcerca_de = QtGui.QAction(MainWindow)
        self.actionAcerca_de.setObjectName(_fromUtf8("actionAcerca_de"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PDF Tool Kit GUI - ver. 0.0.1 BETA", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Archivo de Salida", None, QtGui.QApplication.UnicodeUTF8))
        self.btSearch.setText(QtGui.QApplication.translate("MainWindow", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Archivos a unir", None, QtGui.QApplication.UnicodeUTF8))
        self.btUp.setText(QtGui.QApplication.translate("MainWindow", "Subir", None, QtGui.QApplication.UnicodeUTF8))
        self.btDown.setText(QtGui.QApplication.translate("MainWindow", "Bajar", None, QtGui.QApplication.UnicodeUTF8))
        self.btAdd.setText(QtGui.QApplication.translate("MainWindow", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.btQuit.setText(QtGui.QApplication.translate("MainWindow", "Quitar", None, QtGui.QApplication.UnicodeUTF8))
        self.btQuitAll.setText(QtGui.QApplication.translate("MainWindow", "Quitar Todo", None, QtGui.QApplication.UnicodeUTF8))
        self.btExit.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.btMerge.setText(QtGui.QApplication.translate("MainWindow", "Unir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAcerca_de.setText(QtGui.QApplication.translate("MainWindow", "Acerca de PDF Tool Kit GUI", None, QtGui.QApplication.UnicodeUTF8))

