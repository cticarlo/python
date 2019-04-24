# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forma.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Forma(object):
    def setupUi(self, Forma):
        Forma.setObjectName("Forma")
        Forma.resize(456, 368)
        self.verticalLayoutWidget = QtWidgets.QWidget(Forma)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 431, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_vertical = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_vertical.setContentsMargins(0, 0, 0, 0)
        self.layout_vertical.setObjectName("layout_vertical")
        self.estado_conexao = QtWidgets.QLabel(Forma)
        self.estado_conexao.setGeometry(QtCore.QRect(10, 330, 121, 18))
        self.estado_conexao.setObjectName("estado_conexao")
        self.splitter = QtWidgets.QSplitter(Forma)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 435, 32))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.set_port = QtWidgets.QLineEdit(self.splitter)
        self.set_port.setObjectName("set_port")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.set_baudrate = QtWidgets.QLineEdit(self.splitter)
        self.set_baudrate.setObjectName("set_baudrate")
        self.reconectar = QtWidgets.QPushButton(Forma)
        self.reconectar.setEnabled(True)
        self.reconectar.setGeometry(QtCore.QRect(370, 330, 71, 31))
        self.reconectar.setFlat(False)
        self.reconectar.setObjectName("reconectar")
        self.label.setBuddy(self.set_port)
        self.label_2.setBuddy(self.set_baudrate)

        self.retranslateUi(Forma)
        QtCore.QMetaObject.connectSlotsByName(Forma)

    def retranslateUi(self, Forma):
        _translate = QtCore.QCoreApplication.translate
        Forma.setWindowTitle(_translate("Forma", "Plotter Arduino"))
        self.estado_conexao.setText(_translate("Forma", "Iniciando.."))
        self.label.setText(_translate("Forma", "Porta:"))
        self.set_port.setText(_translate("Forma", "/dev/ttyACM0"))
        self.label_2.setText(_translate("Forma", "&Taxa de transmissão:"))
        self.set_baudrate.setText(_translate("Forma", "9600"))
        self.reconectar.setText(_translate("Forma", "Conectar"))
        self.reconectar.setShortcut(_translate("Forma", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Forma = QtWidgets.QWidget()
    ui = Ui_Forma()
    ui.setupUi(Forma)
    Forma.show()
    sys.exit(app.exec_())

