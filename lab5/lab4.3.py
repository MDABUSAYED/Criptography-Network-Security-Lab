import decimal
def modular_exponent(X, E, m):
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E /= 2
        else:
            Y = (X * Y) % m
            E -= 1

    return Y
def sqrt(n):
    assert n > 0
    with decimal.localcontext() as ctx:
        ctx.prec += 2 
        x, prior = decimal.Decimal(n), None
        while x != prior: 
            prior = x
            x = (x + n/x) / 2 
    return +x 
def continued_function(a):
    arr=list(a)
    arr.reverse()
    k=1
    d=arr[0]    
    for i in range(len(arr)-1):
        b=d*arr[i+1]+k
        k=d
        d=b
    return list([d,k])
    
infile=open('4.3_ciphertext.hex', 'r')
ciphertext=int(infile.read(),16)
infile.close()

infile=open('4.4_public_key.hex', 'r')
e=int(infile.read(),16)
infile.close()
print e
infile=open('4.5_modulo.hex', 'r')
n=int(infile.read(),16)
infile.close()

a=list([(int)(e/n)])
b=n
c=e%n
while(True):
    a.append((int)(b/c))
    m=b%c
    b=c
    c=m
    d=continued_function(a)
    if d[1]==1 or d[1]%2==0 : continue       
    N=(((e*d[1])-1)/d[0])
    J=(int)(N)
    if N-J==0:
        decimal.getcontext().prec = 500
        var=n-(int)(N)+1
        v=(var*var)-(4*n)
        if (sqrt(v)-int(sqrt(v)))==0:
           break;
        else : 
            continue
    else : continue

plaintext=modular_exponent(ciphertext, d[1], n)
print plaintext
