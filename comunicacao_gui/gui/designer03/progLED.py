# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 11:57:48 2016

@author: carlos
"""

import sys

import serial
from PyQt4.QtGui import QApplication, QMainWindow
from leds import Ui_MainWindow



class JanelaLED (QMainWindow, Ui_MainWindow):
    
    def __init__(self):        
        super(JanelaLED, self).__init__()       
        self.setupUi(self)
        
        self.porta = serial.Serial ('/dev/ttyACM3',9600,timeout=1)
        

    def on_LigaLED_clicked(self):
        self.porta.write ('L')
        msg = self.porta.readline()
        print msg

    def on_DesligaLED_clicked(self):
        self.porta.write ('D')
        msg = self.porta.readline()
        print msg

if __name__ == '__main__':
    app = QApplication(sys.argv)    
    
    jan = JanelaLED()   
    jan.show()        
    
    sys.exit(app.exec_())

