# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 15:51:14 2016

@author: SAYED
"""

from Crypto.Cipher import AES

infile=open('aes_weak_ciphertext.hex', 'r')
cipher_text=infile.read().decode("hex")
infile.close()
iv=format(0,'032x').decode("hex")
infile=open('solution03.txt', 'w')

for x in range(0,32) :      
    k=format(x,'064x').decode("hex")
    decryption_suite = AES.new(k, AES.MODE_CBC, iv)
    plain_text = decryption_suite.decrypt(cipher_text)
    infile.write(plain_text+"\n\n\n")
    print plain_text
infile.close()
    
    
    
