# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
''' 1.	Take a string as an input from the user.
 Find total number of vowels in it. (Hint: take a tuple of vowels)
'''

inn = tuple(input('Enter the input '))
vowel = ('a','i','u','e')

total_number = 0

for i in vowel:
    total_number += 1
    print(i)


print(total_number,'are vowel in input ')