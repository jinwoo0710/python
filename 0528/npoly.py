# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:41:27 2021

@author: Mac_1
"""

import turtle as t 

s = t.textinput("","몇 각형을 원하세요? :")
n = int(s)

for i in range(n):
    t.forward(100)
    t.left(360/n)
    
t.done()
