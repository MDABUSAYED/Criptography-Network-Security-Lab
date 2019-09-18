# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 10:56:22 2016

@author: SAYED
"""

from Crypto.Cipher import AES
# Encryption
BLOCK_SIZE = 16
infile=open('aes_iv.hex', 'r')
iv=infile.read().decode("hex")
infile.close()

infile=open('aes_key.hex', 'r')
key=infile.read().decode("hex")
infile.close()

infile=open('aes_ciphertext.hex', 'r')
cipher_text=infile.read().decode("hex")
infile.close()

PADDING = '{'
#iv="3811de72a2adff99aff81a59c02ec0b3".decode("hex")
#key="2438be10190e7a4a6d17341c02c7afc6486405afd7b734e114b14f90ed75bba7".decode("hex")
# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
#encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
#cipher_text = encryption_suite.encrypt(pad("A really secret message."))
#print cipher_text
# Decryption

decryption_suite = AES.new(key, AES.MODE_CBC, iv)
plain_text = decryption_suite.decrypt(cipher_text)

print plain_text

infile=open('solution02.txt', 'w')
infile.write(plain_text)
infile.close()
