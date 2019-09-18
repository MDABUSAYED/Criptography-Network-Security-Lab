from Crypto.PublicKey import RSA

f = open('key','r')
private_key = RSA.importKey(f.read(),passphrase='')

f = open('key.pub','r')
public_key = RSA.importKey(f.read(),passphrase='')

print private_key
print public_key

input_string = raw_input("Input : ")
enc_data = public_key.encrypt(input_string, 32)
print enc_data

print private_key.decrypt(enc_data)

#public_key = key.publickey()
