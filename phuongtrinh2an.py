# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:01:17 2024

@author: VANLALINH
"""
import math
a = float(input("Nhập số thực (a): "))
b = float(input("Nhập số thực (b): "))
c = float(input("Nhập số thực (c): "))
delta = float(b**2-4*a*c)
if delta == 0:
    x = -b/(2*a)
    print("Vậy phương trình có nghiệm kép là: ", x)
elif delta > 0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("Vậy phương trình có 2 nghiệm phân biệt là: ", x1,"và ", (x2))
else:
    print("Vậy phương trình vô nghiệm")