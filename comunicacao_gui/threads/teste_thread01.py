# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 18:45:48 2018

@author: jpela_000
"""

import threading
from time import sleep

class thdread(threading.Thread):
    def run(self):
        print('Executando thread..')
        sleep(10)
        

t = thdread()
print('Iniciando thread.. ')
t.start()

while t.is_alive():
    print('Aguardando thread..')
    sleep(2)
    
print('Thread terminada.')