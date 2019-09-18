# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 16:15:25 2016

@author: SAYED
"""
global str
import re
import hashlib
i=700000000L
a=1195819262116515719124667416518786849282L
while True:
    i=i+1
    if(i>a) :break
    
    line =hashlib.md5(str(i)).digest()
    #print line
    if re.match( r"'or'", line, re.M|re.I):
        print line
    #if re.match( r"'or[1-9]#", line, re.M|re.I): print line
        