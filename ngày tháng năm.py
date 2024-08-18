# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:28:28 2024

@author: LINHĐIVE
"""
time = input("Nhập ngày tháng năm theo dd/mm/yyyy hoặc dd-mm-yyyy là: ")
try:
    ngay, thang, nam =map(int, time.split('/'))
except ValueError:
    print("Không đúng, nhập lại đi")
else:
    if nam % 400 ==0 or (nam % 4 ==0 and nam % 100 !=0):
        namnhuan = True
    else:
        namnhuan = False
    ngaytrongthang = [31, 28, 31,30,31,30,31,30,31,30,31,30]
    if namnhuan:
        ngaytrongthang[1]=29
    if nam<1:
        print("Năm không đúng")
    elif thang<1 or thang>12:
        print("Tháng không đúng")
    elif ngay<1 or ngay > ngaytrongthang[thang-1]:
        print("Ngày không đúng")
    else:
        print("ngày tháng đúng")