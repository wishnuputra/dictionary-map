# -*- coding: utf-8 -*-
"""
==================================================
BIGGEST
==================================================

This is a program to find the key with the
largest number of element.

Created on Tue Jun 25 15:15:27 2019

@author: Wishnuputra
==================================================
"""

def biggest(aDict):
    result = ''
    best = len(max(aDict.values()))
    for key in aDict:
        if len(aDict[key]) == best:
            result = key
    return result

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))