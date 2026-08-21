# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:39:13 2026

@author: ex409_27
 
"""

list_1 = ['ashish' , 'jay','harsh' , 'madam']

polindrom = [x for x in list_1 if  x == x[::-1]]

print(polindrom)