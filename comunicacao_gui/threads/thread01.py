#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 11:24:25 2019

@author: carlos
"""

import threading as linha

from time import sleep


def testeLinha ():
    print ("Esta eh uma thread")
    sleep(5)
    print ("Saindo da thread")


t = linha.Thread (target=testeLinha)
t.start()
print ("Vou dormir")
sleep(10)
print ("Acordei")








