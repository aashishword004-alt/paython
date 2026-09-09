# -*- coding: utf-8 -*-
"""
1.	Display the youngest student from the above dictionary.
2.	Create a dictionary of students having rollno of the student 
is as key and value is a list of marks obtained by that student in 5 subjects
3.	Create a dictionary from the above one, where key is rollno and 
value is (total of all subjects, percentage and grade ) a tuple of his result
4.	Display the rollno who has scored highest marks (total)

@author: ex409_29
"""

std = {101 : [70,65,76,65] , 102 : [98.76,54,78] , 103 : [54,44,89,87] , 104 : [54,87,78,45,54]
       ,105 : [45,54,87,45]}
d = {}
for k,v in std.items():
   t = 0
   for mark in v:
       t = t+mark
       p = t / 5
   print(p)
   if p > 90:
       grad ='A++'
   elif p > 80:
        grad ='A+'
   elif p > 70:
       grad ='B+'
   elif p > 60:
        grad ='B'
   else:
        grad = 'fail'
   d[k] =(t,p,grad)
   
print(d)
     
        
       
