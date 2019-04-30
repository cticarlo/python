# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 19:21:37 2018

@author: jpela_000
"""

import threading
from time import sleep

        
class thrd_sec(threading.Thread):
    def __init__(self, thread_primaria):
        threading.Thread.__init__(self)
        self.t_prim = thread_primaria
    def run(self):
        print('Executando {}..'.format(self.name))
        self.t_prim.join()
        print('Terminando ', self.name)
    
    
def espera(tempo):
    print('Esperando {} segundos'.format(str(tempo)))
    for t in range(1, tempo+1):
        print(t)
        sleep(1)
        
    
t0 = threading.Thread(target=espera, args=(5,))    
t1 = thrd_sec(t0)

t0.start()
t1.start()

