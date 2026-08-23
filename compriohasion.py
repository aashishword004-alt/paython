# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:56:13 2026

@author: ex409_27
"""

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


number = [x  for x in num if x%2 == 0 and x%3 == 0]

print(number)