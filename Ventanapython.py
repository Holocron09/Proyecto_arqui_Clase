# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InterfazProyec.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 857)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 200, 291, 241))
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 30, 301, 141))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(170, 110, 81, 21))
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(170, 20, 111, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(170, 50, 91, 20))
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 91, 20))
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(170, 80, 91, 20))
        self.label_7.setObjectName("label_7")
        self.graphicsView_2 = PlotWidget(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(330, 200, 281, 241))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(440, 30, 511, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(380, 20, 81, 20))
        self.label_12.setObjectName("label_12")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 101, 20))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(260, 20, 81, 20))
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(140, 20, 81, 20))
        self.label_10.setObjectName("label_10")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(380, 90, 91, 20))
        self.label_16.setObjectName("label_16")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(260, 90, 91, 20))
        self.label_15.setObjectName("label_15")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(10, 90, 101, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(140, 90, 91, 20))
        self.label_14.setObjectName("label_14")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 50, 101, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber_2.setGeometry(QtCore.QRect(143, 50, 91, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber_3.setGeometry(QtCore.QRect(260, 50, 91, 23))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber_4.setGeometry(QtCore.QRect(383, 50, 91, 23))
        self.lcdNumber_4.setSmallDecimalPoint(True)
        self.lcdNumber_4.setDigitCount(5)
        self.lcdNumber_4.setProperty("value", 2.5)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.graphicsView_3 = PlotWidget(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(330, 440, 281, 241))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = PlotWidget(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(40, 440, 291, 241))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.graphicsView_5 = PlotWidget(self.centralwidget)
        self.graphicsView_5.setGeometry(QtCore.QRect(610, 200, 451, 481))
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(720, 170, 231, 22))
        self.spinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox.setProperty("value", 30)
        self.spinBox.setObjectName("spinBox")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(470, 170, 231, 16))
        self.label_17.setObjectName("label_17")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 21))
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
        self.groupBox.setTitle(_translate("MainWindow", "Valores"))
        self.label_2.setText(_translate("MainWindow", "Humedad"))
        self.label.setText(_translate("MainWindow", "Temperatura"))
        self.label_4.setText(_translate("MainWindow", "Altitud"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Presión"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Diales"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "Altitud"))
        self.label_15.setText(_translate("MainWindow", "Presión"))
        self.label_13.setText(_translate("MainWindow", "Temperatura"))
        self.label_14.setText(_translate("MainWindow", "Humedad"))
        self.label_17.setText(_translate("MainWindow", "Numero de Datos a Graficar"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

