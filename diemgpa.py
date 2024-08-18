# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:25:42 2024

@author: LINHNE
"""
GPA = float(input("Nhập điểm trung bình (GPA):"))

if GPA < 3.5:
    print("Học Lực Kém")
elif GPA >= 3.5 and GPA <5.0:
    print("Học lực Yếu")
elif GPA >= 5.0 and GPA < 7.0:
    print("Học lực Trung bình")
elif GPA >= 7.0 and GPA < 8.0:
    print("Học lực Khá")
elif GPA >= 8.0 and GPA < 9.0:
    print("Học lực Giỏi")
else:
    print("Học lực xuất sắc")

