# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:25:57 2026

@author: ex409_27
"""

alp = [ 'a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

vowel  = ['a','i' ,'o','u','e' ]

voice = [ x for x in alp  if x not in vowel]

print(voice)