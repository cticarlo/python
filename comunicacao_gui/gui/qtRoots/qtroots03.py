#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 09:52:19 2019

@author: carlos
"""

import sys
from PyQt4 import QtGui,QtCore

class HiButton(QtGui.QWidget):
    
    def __init__(self):
        super(HiButton, self).__init__()        
        self.initUI()

    def initUI(self):        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        self.setToolTip('Esta é uma janela personalizada de <b>QWidget</b>')
        
        btn = QtGui.QPushButton(u'Botão', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)       
        
        btn.setToolTip(u'Este é um botão do tipo <b>QPushButton</b>')
        
        btn.clicked.connect(self.minhaAcao)            
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Hi, Mundo com botão e dicas')
    

    def minhaAcao(self):        
        QtGui.QMessageBox.critical (self, "Importante",
             u"Uhu!!! Estou executando minhas ações!!!")
        
        print (u"Uhu!!! Estou executando minhas ações!!!")
        QtCore.QCoreApplication.instance().quit()




def main():    
    app = QtGui.QApplication(sys.argv)
    hmb = HiButton()
    hmb.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()












