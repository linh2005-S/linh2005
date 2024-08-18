# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:17:34 2024

@author: LINHSAPVE
"""
a = float(input("a là: "))
b = float(input("b là: "))
c = float(input("c là: "))
if a+b>c and a+c>b and b+c>a:
    if a == b == c:
        print("tam giác đều")
    elif a==b or b==c or a==c:
        print("tam giác cân")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("tam giác vuông")
    else:
        print("3 cạnh của tam giác")
else:
    print("không phải là 3 cạnh của tam giác")