# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:59:24 2015

@author: carlos
"""

import sys
from PyQt4 import QtGui
from segunda import Ui_MainWindow

class Prim (QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Prim, self).__init__(parent)        
        self.setupUi(self)

app = QtGui.QApplication(sys.argv)

w = Prim()
w.show()

sys.exit(app.exec_())


