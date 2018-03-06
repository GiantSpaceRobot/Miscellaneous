#!/usr/bin/env python

"""
String manipulation toolkit
"""

__author__ = "Paul Donovan" 
__maintainer__ = "Paul Donovan"
__email__ = "pauldonovandonegal@gmail.com"

import random
import numpy

class StringToolkit(object):
    """
    A number of useful string-manipulation tools
    """
    def __init__(self, InputString):
        """ Store string in self.InputString """
        self.InputString = InputString

    def StringCount(self):
        """ Return the number of characters in input string """
        self.StringLength = len(self.InputString)
        return self.StringLength

    def UniqueChars(self):
        """ Returns information about characters in input string """
        UniqueCharsSet = set(self.InputString)
        UniqueCharsString = ''.join(UniqueCharsSet)                                #Return the unique characters as a string
        return (UniqueCharsSet, UniqueCharsString)

    #def RandomGapGenerator(self): 
    #    """ Generate two random numbers between 0 and max string length 
    #    using returned values of member function (same class) StringCount """
    #    RandomNumbers = sorted(random.sample(range(0,self.StringCount()), 2))   #Generate random numbers and sort numberically
    #    return (RandomNumbers[0], RandomNumbers[1])
    #    GapLength = RandomNumbers[1] - RandomNumbers[0]                         #Store distance between start and stop coordinates in variable
    #    UniqueCharsString = (self.UniqueChars())[1]
    #    ReplacementChunk = ''.join(random.choice(UniqueCharsString) for i in range(GapLength))
    #    return (RandomNumbers[0], RandomNumbers[1], GapLength, ReplacementChunk)

    def CharacterFrequency(self):
        """ Return the frequency of each character in input string """
        CharDict = dict()
        for char in self.InputString:
            if str(char) in CharDict:										
                CharDict[char] = (int(CharDict[char]) + 1)	
            else:															
                CharDict[char] = 1
        return CharDict

    def findmean(self):
        """ Find mean value of characters """
        StringLength = self.StringCount()  
        NumberOfChars = len((self.UniqueChars())[1])
        Mean = float(StringLength)/float(NumberOfChars)
        return Mean
    
    def standarddeviation(self):
        """ Calculate standard deviation of character frequency """
        CharFreqList = (self.CharacterFrequency()).values()
        SD = numpy.std(CharFreqList)
        return SD