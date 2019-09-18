# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 11:39:55 2016

@author: SAYED
"""

import hashlib


infile=open('3.1_input_string.txt', 'r')
input_string=infile.read()
infile.close()

infile=open('3.1_perturbed_string.txt', 'r')
perturbed_string=infile.read()
infile.close()

hash_object = hashlib.sha256(input_string)
hex_dig = hash_object.hexdigest()
print hex_dig


hash_object = hashlib.sha256(perturbed_string)
hex_dig1 = hash_object.hexdigest()
print hex_dig1

binary=bin(int(hex_dig, 16))[2:]

binary1=bin(int(hex_dig1, 16))[2:]

y = int(binary,2) ^ int(binary1,2)

print format(y,'0256b')
print format(y,'0256b').count('1')

infile=open('solution31.txt', 'w')
infile.write("SHA256 for given string     : "+hex_dig+"\n\n")
infile.write("SHA256 for perturbed string : "+hex_dig1+"\n\n")
infile.write("Number Of bit Difference   : "+str(format(y,'0256b').count('1'))+"\n\n")
infile.close()

