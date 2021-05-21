# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:40:01 2021

@author: Mac_1
"""

import turtle as t 
 
t.width(3)
t.shape('turtle')
t.shapesize(3, 3)

while True:
    command = t.textinput("방향 결정", "L 이나 R 입니다.")
    if command == "L":
        t.left(90)
        t.forward(100)
    if command == "R":
        t.right(90)
        t.forward(100)
t.exitonclick(0)