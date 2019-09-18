# -*- coding: utf-8 -*-
"""
Created on Thu Aug 04 06:48:32 2016

@author: SAYED
"""
import re
from math import log10
wordarray={}
#open file to read count and calculate fitness for each keyword og length 3
with open('english.txt') as f:
    content = f.read().splitlines()
    print(len(content))
for i in range(0,len(content)):
    key,value=content[i].split(' ')
    wordarray[key]=log10(float(int(value))/len(content))
    
cypher_text = 'YMJHFJXFWHNUMJWNXTSJTKYMJJFWQNJXYPSTBSFSIXNRUQJXYHNUMJWX'
cypher_text = re.sub('[^A-Z]','',cypher_text.upper())
decypher_text=''
plain_text=''
score=[-10000,0]
#decription
for i in range(26):
    fitness_calculation=0
    b=''
    k=0;
    #shift cypher_text a fixed amount
    for j in range(0,len(cypher_text)):
        if (ord(cypher_text[j])-i)<65:
            b+=chr(ord(cypher_text[j])-65+91-i)
        else:
            b+=chr(ord(cypher_text[j])-i)
    #calculate fitness
    for j in range(0,len(b)):
        if b[j:j+3] in wordarray: 
                fitness_calculation += wordarray[b[j:j+3]]
    if(fitness_calculation>score[0]):
        score[0]=fitness_calculation
        score[1]=i
        plain_text=b

print "ceaser cyper key for above cypher text : "+str(score[1])
print "plaintext :\n"+plain_text
    
    
    

    
    