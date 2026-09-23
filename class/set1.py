# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

l = [12,7,18,5,22,9]
count = 0
for i in l :
    if i % 2 == 0:
        print(i)
    else:
        count+=1

#print(count , 'odd')
        
print('**********************')
sm = []
nw = {}
for k in l :
  n = i
  total = 0
  while i > 0:
    digit = i % 10 
    total += digit
    i = i // 10
    
mx = 0
sl = 0
for k in l:
   if k > mx:
       sl = mx
       mx = k
print(mx,sl,)

print("*************")
lar = []
for v in l:
    if v > 10:
        lar.append(v)
print(lar)
