# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movies.ui'
#
# Created: Thu Jun 19 14:31:16 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 614)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Movies-Oscar-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(522, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.subir = QtGui.QPushButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("hand-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subir.setIcon(icon1)
        self.subir.setObjectName("subir")
        self.horizontalLayout.addWidget(self.subir)
        self.bajar = QtGui.QPushButton(self.widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("hand-icon_unlike.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bajar.setIcon(icon2)
        self.bajar.setObjectName("bajar")
        self.horizontalLayout.addWidget(self.bajar)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 2)
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image = QtGui.QLabel(self.widget_2)
        self.image.setText("")
        self.image.setObjectName("image")
        self.verticalLayout.addWidget(self.image)
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.titulo = QtGui.QLabel(self.widget_2)
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo)
        self.label_3 = QtGui.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.descripcion = QtGui.QLabel(self.widget_2)
        self.descripcion.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.descripcion.setText("")
        self.descripcion.setWordWrap(True)
        self.descripcion.setObjectName("descripcion")
        self.verticalLayout.addWidget(self.descripcion)
        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setImageLabel(self, direccion):
        """Funcion que asigna una imagen
        @param direccion"""
        self.image.setPixmap(QtGui.QPixmap(direccion))


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Movies", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Ranking:", None, QtGui.QApplication.UnicodeUTF8))
        self.subir.setText(QtGui.QApplication.translate("MainWindow", "Subir", None, QtGui.QApplication.UnicodeUTF8))
        self.bajar.setText(QtGui.QApplication.translate("MainWindow", "Bajar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Titulo:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.titulo.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Descripcion:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

