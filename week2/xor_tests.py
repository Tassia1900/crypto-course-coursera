# Programa que resuelve el caso propuesto en el test
import operator, binascii

c1 = "290b6e3a39155d6f"
c2 = "d6f491c5b645c008"


def binary_xor(c,m):
    k = '0b'
    c = c[2:]
    m = m[2:]
    if not(len(m) == len(c)):
        # got to insert zeros until they're fine
        while len(m) < len(c):
            m='0'+m
        while len(c) < len(m):
            c = '0'+c    
    for i in range(len(m)):
        k+=str(int(m[i]) ^ int(c[i]))
    #print k
    return k

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

print binary_xor(bin(int(c1,16)),bin(int(c2,16)))
print bin(int(strxor(c1.decode('hex'), c2.decode('hex')).encode('hex'),16))

# La solucion contiene todo 1s en donde corresponde (parte inferior o superior)
