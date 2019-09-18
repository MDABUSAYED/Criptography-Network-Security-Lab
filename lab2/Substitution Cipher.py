# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 18:16:55 2016

@author: SAYED
"""

#from Crypto.Cipher import AES
# Encryption

infile=open('sub_ciphertext.txt', 'r')
cipher_text=infile.read()
infile.close()

infile=open('sub_key.txt', 'r')
key=infile.read()
infile.close()
plain_text=""
for x in range(0,len(cipher_text)) :
    if cipher_text[x]!=' ' :
        plain_text=plain_text+key[ord(cipher_text[x])-65]
    else :
        plain_text=plain_text+' '
        
print plain_text

infile=open('solution01.txt', 'w')
infile.write(plain_text)
infile.close()