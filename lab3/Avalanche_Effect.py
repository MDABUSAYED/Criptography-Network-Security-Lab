# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 11:39:27 2016

@author: SAYED
"""

import random, string

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))


def WHA( str ):
    mask=0x3fffffff
    
    outhash=0
    for byte in str:
        intermediate_value= (((ord(byte) ^ int('0xcc',16))<<24) |
                            ((ord(byte) ^ int('0x33',16))<<16) |
                            ((ord(byte) ^ int('0xaa',16))<<8) |
                            (ord(byte) ^ int('0x55',16)))
        outhash=(outhash & mask) +(intermediate_value & mask)
    #print outhash
    return hex(outhash)[0:10];
    
    
infile=open('3.2_input_string.txt', 'r')
input_string=infile.read()
infile.close()
print len(input_string)
another_string=input_string

str1=another_string[0:1]
str2=another_string[1:2]
str3=another_string[2:]

str4=str2+str1+str3
print str4
print WHA(input_string)
print WHA(str4)

infile=open('solution32.txt', 'w')
infile.write("Given string   : "+input_string+"\n\n")
infile.write("Another string : "+str4+"\n\n")
infile.close()