#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 09:42:06 2019

@author: carlos
"""

import sys
from PyQt4 import QtGui


class HiMundoWindow(QtGui.QWidget):
    
    def __init__(self):
        super(HiMundoWindow, self).__init__()        
        self.personalizaUI()
        
        
    def personalizaUI(self):        
        self.setGeometry(100, 100, 640, 480)
        self.setWindowTitle('Hi, mundo!!!')
        
        self.setWindowIcon(QtGui.QIcon('automacao.png'))            
        
        #self.show()





app = QtGui.QApplication(sys.argv)
hiMundo = HiMundoWindow()
hiMundo.show()
sys.exit(app.exec_())
