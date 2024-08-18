# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:43:02 2024

@author: LINHMUONVELAM
"""
from random import randint
print("Chọn 'bao', 'búa', 'kéo': "); chon = input(); rdom = randint(0,2)
if rdom == 0:
    rdom = 'bao'
elif rdom == 1:
    rdom = 'búa'
else:
    rdom = 'kéo'
print('Bạn chọn: '+chon); print('Hệ thống chọn: '+rdom); print('Kết quả: ')
if chon == rdom:
    print('Hòa')
elif chon == 'bao':
    if rdom == 'kéo':
        print('Hệ thống thắng')
    else:
        print('Bạn thắng')
elif chon == "búa":
      if rdom == "kéo":
        print('Bạn thắng')
      else:
        print('Hệ thống thắng')
elif chon == "kéo":
    if rdom == "bao":
        print("Bạn thắng")
    else:
        print("Hệ thống thắng")