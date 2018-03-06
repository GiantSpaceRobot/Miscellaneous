#!/usr/bin/env python

"""
Determine the shortest possible subsequence that needs to be replaced 
to have equal representation of all characters from the input string
"""

__author__ = "Paul Donovan" 
__maintainer__ = "Paul Donovan"
__email__ = "pauldonovandonegal@gmail.com"

import sys
import argparse
from stringtoolkit import StringToolkit

""" Display help and usage """
parser = argparse.ArgumentParser(description="Incorrect number of command line arguments")
parser.add_argument('Input_String.txt')
if len(sys.argv[1:]) == 0:
    parser.print_help()
    parser.exit()
args = parser.parse_args()

with open(sys.argv[1]) as f:                                    #Read file containing string into variable f
    InputString = (f.readlines())[0].strip()   

Substrings = StringToolkit(InputString).getsubstrings()         #Generate list of all viable substrings
ShortestSubsequence = min(Substrings, key=len)                  #Find the shortest subsequence
print "Number of viable substrings: %s\nShortest subsequence that can be replaced to get equal character representation: %s\nThe length of this subsequence: %s" % (len(Substrings), ShortestSubsequence, len(ShortestSubsequence))
