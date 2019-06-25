# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:32:22 2019

@author: Wishnuputra
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    result = 0
    for key in aDict:
        val = aDict[key]
        result += len(val)
    return result

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals)
print("Sum of element in each value:", how_many(animals))

