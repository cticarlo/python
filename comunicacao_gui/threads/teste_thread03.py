#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 17:55:44 2018

@author: julia
"""

import threading, random 
from time import sleep

def espera():
    pausa = random.randint(1, 10)
    sleep(pausa)
    
t = threading.Thread(target=espera)
t.daemon = True
t.start()

t.join(timeout=5)

if t.is_alive():
    print('Thread passou do tempo limite')
else:
    print('Thread terminada')
    
print('Finalizando o programa')