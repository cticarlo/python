#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 08:33:27 2019

@author: carlos
"""
import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

w = QtGui.QWidget()
w.resize(640, 480)
w.move(300, 300)
w.setWindowTitle('Hi, mundo!!!')
w.show()


sys.exit(app.exec_())
