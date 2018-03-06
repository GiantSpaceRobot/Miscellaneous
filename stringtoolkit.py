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
        """ Return the number of characters in the input string """
        self.StringLength = len(self.InputString)
        return self.StringLength

    def UniqueChars(self):
        """ Returns information about characters in input string """
        UniqueCharsSet = set(self.InputString)                      #Store the unique characters as a set
        UniqueCharsString = ''.join(UniqueCharsSet)                 #Store the unique characters as a string
        return (UniqueCharsSet, UniqueCharsString)

    def CharacterFrequency(self):
        """ Return the frequency of each character in input string """
        CharDict = dict()
        for char in self.InputString:                               #Add all characters from the input string to dict, counting as we go
            if str(char) in CharDict:										
                CharDict[char] = (int(CharDict[char]) + 1)	        #If the character is already in the dict, add 1 to the value
            else:															
                CharDict[char] = 1                                  #If the character is not in the dict, add it as a key
        return CharDict

    def findmean(self):
        """ Find mean value of characters """
        StringLength = self.StringCount()
        if int(StringLength) == 0:                                  #If a string of length 0 is passed to this function, return a Mean value of 0
            Mean = int(0)
        else:
            NumberOfChars = len((self.UniqueChars())[1])            #Calculate the number of unique characters in the input string
            Mean = float(StringLength)/float(NumberOfChars)         #Calculate mean
        return Mean

    def standarddeviation(self):
        """ Calculate standard deviation of character frequency """
        CharFreqList = (self.CharacterFrequency()).values()         #Gather all of the frequencies of the characters
        SD = numpy.std(CharFreqList)                                #Use numpy to calculate the standard deviation 
        return SD

    @staticmethod                                                   #Method is not callable outside of this class
    def frequencyabovemean(InputString, FlankingChars):
        """ Return "True" boolean flag if the current cubstring 
        has flanking regions with no character represented more
        times than the mean. Otherwise return "False" """
        Flag = False
        InputMean = StringToolkit(InputString).findmean()           #Calculate mean of the original input string
        FlankFreq = StringToolkit(FlankingChars).CharacterFrequency()   #Calculate the character frequency of the regions flanking the substring
        FreqAboveMean = {k:v for (k,v) in FlankFreq.items() if v > InputMean}   #If any characters are present in the flanking region more often than the mean, add these to a new dict
        if bool(FreqAboveMean) == False:                            #If this new dict is empty, change the flag to "True"
            Flag = True
        return Flag

    def getsubstrings(self):
        """ Get all possible substrings of inut string
        provided the flanking regions of the substring 
        has all characters represented less than the mean """
        length = len(self.InputString)                              #Find the length of the original input string
        substrings = list()
        Start = 0
        Stop = 1
        while Start < (length - 1):
            """ Walk along the input string and generate
            every possible substring. If the inverse of 
            the substring (i.e. the flanking regions) 
            contains characters present more often than 
            the mean, dump these substrings """
            SubString = self.InputString[Start:Stop]
            Flanks = self.InputString[:Start] + self.InputString[Stop:]
            if StringToolkit.frequencyabovemean(self.InputString, Flanks) == True:  #Test concatenated flanking regions of the substring
                substrings.append(SubString)                        #Add viable subtrings to a list
            if Stop == (length):
                Start = Start + 1
                Stop = Start + 1
            else:
                Stop = Stop + 1
        return substrings