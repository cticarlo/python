#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:20:02 2018

@author: julia
"""
"""
  Este exemplo integra os conceitos de GUIs, gráficos matplotlib, comunicação
serial, threads e etc. trata-se de uma aplicação gráfica que mostra dados
recebidos do Arduino em um gráfico matplotlib atualizaqdo em tempo real.

  Para isso serão novamente utilizadas as APIs PyQt5 (para a parte gráfica),
pyserial (serial) para comunicação serial, matplotlib, para a construção
do gráfico, threading, para trabalhar com processamento assíncrono, etc.
  Considerando a matplotlib: será utlizado o backend Qt5Agg. O backend é a
parte da API que faz a construção da figura a partir do 'frontend' (código 
escrito pelo programador) o que pode ocorrer de formas diferentes dependendo
do caso de aplicação do gráfico. Neste exemplo o gráfico será usado em uma
aplicação PyQt5, de forma que será usado o backend 'Qt5Agg' para possibilitar
essa compatibilidade.

  Serão utilizados métodos semelhantes aos já discutidos nos exemplos 
anteriores para a utilização de telas criadas no QtDesigner através do pyuic.


"""
import matplotlib
matplotlib.use('Qt5Agg')

import serial
from PyQt5 import QtWidgets, QtCore
import sys, threading
from collections import deque
import time

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure 

from forma import Ui_Forma

class CanvasDinamico(FigureCanvas):
    """
    Esta classe cria um gráfico matplotlib que pode ser usado como um widget
    Qt5, herdando da classe FigureCanvasQTAgg (FigureCanvas) do backend 
    Qt5Agg.
    """        
    def __init__(self):
        """
        Inicia a figura como gráfico matplotlib e widget Qt.
        """
        fig = Figure(figsize=(5,4), dpi=100)
        self.axes = fig.add_subplot(111)
                
        FigureCanvas.__init__(self, fig)
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self) 
        self.reinicia()                   
        
    def atualiza(self, x, y):
        """
        Função que atualiza o gráfico, que será chamada a cada novo dado
        obtido.
        """
        self.x.append(x)
        self.y.append(y)
        self.axes.cla()
        self.axes.plot(self.x, self.y)
        self.draw()  
        
    def reinicia(self):
        """
        Inicializa (ou reseta) as variáveis x e y, que são do tipo deque,
        do módulo collections. Essas são usadas de forma semelhante a listas,
        porém têm um número máximo de elementos. Uma vez atingido esse limite
        e feito um novo append o primeiro item será excluído e todos os ele-
        mentos avançarão uma posição.
          Ex.: d = deque([1,2,3], maxlen = 3)
               d.append(4)
               d ---> [2,3,4]
        Dessa forma as variáveis x e y corresponderão ao pontos a serem 
        plotados no gráfico, atualizados dinamicamente.
        """
        self.x = deque([0.0]*100, maxlen=100)
        self.y = deque([0.0]*100, maxlen=100)
        
        
class Janela(QtWidgets.QWidget, Ui_Forma):
    """
    Esta classe é referente à GUI em si, de forma semelhante aos outros 
    exemplos.
    A maior diferença é que ela herdará da classe QWidget, de forma que a
    própria instância da classe (self) será o Widget, enquanto nos exemplos
    anteriores uma instância de QWidget era criada externamente e passada
    como parâmetro na inicialização da classe. Isto faz com que seja 
    necessário invocar o método show() na inicialização e torna possível 
    acessar eventos como o closeEvent, que é emitido cada vez que é dado
    o comando para que a aplicação feche, permitindo que as ações tomadas 
    ao fechar sejam customizadas. 
    """
    falha_conexao = QtCore.pyqtSignal()  #definição dos sinais falha_conexao
    conectado = QtCore.pyqtSignal()      # e conectado
    
    def __init__(self):
        """
        Inicia a aplicação como um QWidget e configura a GUI conforme o 
        design feito no Designer.
        Também inicia o widget CanvasDinamico (gráfico matplotlib) posicionado
        na esturtura layout_vertical (QVBoxLayout), determina as conexões
        de alguns sinais e inicia as listas xl e xy.
        """
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
              
        self.cd = CanvasDinamico()
        self.layout_vertical.addWidget(self.cd)
        
        self.falha_conexao.connect(self.falha)
        self.conectado.connect(self.envia)
        self.reconectar.clicked.connect(self.conectar) #coloca atalho         
        
        self.xl = []
        self.yl = []
        
#        self.show()
        
    def conectar(self):
        """
        Slot do sinal clicked do botão reconectar.
        Define a porta e a taxa de transmissão referentes à comunicação 
        serial canforme o escrito na GUI. Torna o botão reconectar 
        indisponível, reinicia o gráfico, define o tempo inicial a ser
        plotado como o tempo atual de execução do programa e inicia uma
        thread daemon tendo como alvo a função recebe().
        """
        self.port = self.set_port.text()
        self.baudrate = self.set_baudrate.text()
        self.reconectar.setEnabled(False)
        self.controle = False
        self.cd.reinicia()
        t = threading.Thread(target=self.recebe, daemon=True)
        self.t0 = time.time()
        t.start()    
        
    def recebe(self):
        """
        Tenta estabelecer uma conexão serial. 
        Feito isso, entra no loop de coleta de dados. A cada dado recebido
        é atualizado o gráfico e emitido o sinal conectado.
        O loop é interrompido quando a variável controle (definida na função
        conectar() como True) for falsa. Quando isso ocorre é fechada a 
        conexão serial e chamado o método close() (que dispara o evento 
        closeEvent)
        Caso ocorra alguma excessão é emitido o sinal falha_conexao.
        """
        try:
            self.ser = serial.Serial(self.port, self.baudrate)
            time.sleep(3)
            while(not self.controle):
                    num = self.ser.readline();
                    num = num.decode()
                    num.strip('\rn')
                    self.yl.append(float(num))
                    self.xl.append(time.time() - self.t0)
                    self.cd.atualiza(self.xl.pop(), self.yl.pop())
                    self.conectado.emit()    
            self.falha_conexao.emit()
            self.ser.close()                 
            self.close()
        except:
            self.falha_conexao.emit()
            
    def envia(self):
        """
        Slot do sinal conectado. Caso o botão reconectar esteja desabilitado
        escreve o texto 'Conectado' na label estado_conexao
        """
        if (not self.reconectar.isEnabled()):
            self.estado_conexao.setText('Conectado')
                           
    def falha(self):
        """
        Slot do sinal falha_conexao.
        Escreve o texto 'Falha na conexão' na label estado_conexao e
        habilita o botão reconectar.
        """
        self.estado_conexao.setText('Falha na conexão')
        self.reconectar.setEnabled(True)
    
    def closeEvent(self, event):
        """
        Evento acionado tada vez que é emitido um comando para fechar a 
        aplicação.
        Aqui ele é sobreescrito para que se o texto na label estado_conexao
        for 'Conectado' a variável controle será True (o que causará a
        interrupção do loop de aquisição de dados na thread daemon) e o 
        evento será ignorado (a aplicação não fechará).
        Caso contrário o evento será aceito e a apĺicação fechará. 
        """
        if (self.estado_conexao.text() == 'Conectado'):
            self.controle = True
            event.ignore()
        else:
            event.accept()
    
   
app = QtWidgets.QApplication(sys.argv)
 
prog = Janela()
prog.show()

sys.exit(app.exec_())











