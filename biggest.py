# -*- coding: utf-8 -*-
"""
==================================================
BIGGEST
Exercise Lecture 6
MITx 6.00.1x
==================================================

This is a program to find the key with the
largest number of element.

Created on Tue Jun 25 14:53:00 2019

@author: Wishnuputra
==================================================
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = ''
    largest = 0
    for key in aDict:
        valLength = len(aDict[key])
        if valLength > largest:
            largest = valLength
            result = key
    return result

    
    
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))