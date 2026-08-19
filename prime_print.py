# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:21:44 2026

@author: ex409_5
"""

start = int(input("Enter The Number 1 : "))
stop = int(input("Enter The Number 2 : "))

for n in range(start,stop+1):
    for i in range(2,n):
        if n%2 == 0:
            flage = False
            break

if flage == True:
     print(n)

            
             




