"""
# -*- coding: utf-8 -*-
Spyder Editor

This is a temporary script file.                                                                      
p = int(input('ennter the numbe')
"""


l = [1,2,3,4,5,6,7,8,9]

even = []
odd = []

even , odd = [ i*i for i in l if i%2 == 1 ] ,[i*i for i in l if i%2 == 0] 
print(even)
print(odd)