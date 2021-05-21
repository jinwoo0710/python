# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:31:33 2021

@author: Mac_1
"""

import turtle as t
t.shape('turtle')
t.clear()
s = t.textinput("", "이름을 입력하세요, ")
t.write("안녕하세요"+s+"님 멍청합니다.")

for i in range(4):
    t.forward(100)
    t.left(90)
    t.penup()
    t.left(90)
    t.forward(120)
    t.pendown()
    t.left(90)
    t.forward(100)