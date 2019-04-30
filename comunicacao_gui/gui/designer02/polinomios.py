# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:58:14 2015

@author: carlos
"""

import sys

import numpy as np

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QApplication, QMainWindow
from telagrafico import Ui_MainWindow

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FC


class JanelaPolinomio (QMainWindow, Ui_MainWindow):
    
    def __init__(self):        
        super(JanelaPolinomio, self).__init__()       
        self.setupUi(self)
        
        # Adicionando a área de desenho da figura
        self.grafico = Figure()
        self.canvasFC = FC(self.grafico)
        self.canvasFC.sizePolicy().setVerticalStretch(10)
        
        self.verticalLayout.addWidget(self.canvasFC)
        
      #  self.actionTracar.triggered.connect(self.apertouBotaoPlota)
        self.frLimites.setVisible(False)
        
        c = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        self.calculaPontos(c)
        self.btFaca.clicked.emit(True)


    def calculaPontos(self, coefs):
        u"""
        Calcula os pontos a serem traçados para o polinômio em questão
        """       
        eq = np.poly1d(coefs)
        
        x = np.linspace (-10.0,10.0,101)
        y = eq(x)
        
        self.grafico.clear()
        self.graf = self.grafico.add_subplot(111)       
        self.graf.plot(x,y,'b') 
        self.canvasFC.draw()
        # Obrigado ao StackOverflow
        # http://stackoverflow.com/questions/30880358/matplotlib-figure-not-updating-on-data-change
        

#    @pyqtSlot()
#    def apertouBotaoPlota(self):
#        # conseguir os coeficientes  
#        c = np.array([float(self.edX5.text()),
#                      float(self.edX4.text()),
#                      float(self.edX3.text()),
#                      float(self.edX2.text()),
#                      float(self.edX1.text()),
#                      float(self.edX0.text())])
#        self.calculaPontos(c)


    def on_actionTracar_triggered(self):
        # conseguir os coeficientes  
        c = np.array([float(self.edX5.text()),
                      float(self.edX4.text()),
                      float(self.edX3.text()),
                      float(self.edX2.text()),
                      float(self.edX1.text()),
                      float(self.edX0.text())])
        self.calculaPontos(c)

    def on_actionLimites_triggered(self):        
        self.frLimites.setVisible(True)

    def on_btFaca_clicked(self):
        self.graf.set_xlim(float(self.edXmin.text()),float(self.edXmax.text()))
        self.graf.set_ylim(float(self.edYmin.text()),float(self.edYmax.text()))
        self.frLimites.setVisible(False)
        self.canvasFC.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)    
    
    jan = JanelaPolinomio()   
    jan.show()        
    
    sys.exit(app.exec_())

