import random

def isPrime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def Keypair(fi):
    e = random.randrange(1, fi)
    g = gcd(e, fi)
    while g != 1:
        e = random.randrange(1, fi)
        g = gcd(e, fi)

    d = e + 1
    while d*e % fi != 1:
        d+=1

    return e, d

def encrypt(plaintext, private_key, n):
    cipher = [(ord(char) ** private_key) % n for char in plaintext]
    return cipher

def decrypt(ciphertext, public_key, n):
    plain = [chr((char ** public_key) % n) for char in ciphertext]
    return ''.join(plain)

p = 0
q = 0

while p==0 or q==0:
    x = random.randrange(1, 1000)
    if isPrime(x):
        if p==0:
            p = x
        else :
            q = x

n = p * q
fi = (p-1) * (q-1)

e, d = Keypair(fi)

print "Public Key : ", e
print "Private Key :", d

plain_text = raw_input("Input : ")

cipher = encrypt(plain_text, e, n)
plain = decrypt(cipher, d, n)

print "Ciper Text : ",cipher
print "Plain Text : ",plain
