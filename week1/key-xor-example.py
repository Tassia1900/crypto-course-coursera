# Programa que resuelve el caso propuesto en el test
import operator, binascii

c=bin(int('6c73d5240a948c86981bc294814d', 16))
m=bin(int(binascii.hexlify('attack at dawn'), 16))
newm = bin(int(binascii.hexlify('attack at dusk'),16))


def binary_xor(c,m):
    k = '0b'
    if not(len(m) == len(c)):
        raise Exception('Longitudes no coinciden')
    for i in range(2,len(m)):
        k+=str(int(m[i]) ^ int(c[i]))
    #print k
    return k

k = binary_xor(c,m)
nencryption = binary_xor(k,newm)
# el resultado final en hexadecimal:
print hex(int(nencryption,2))[2:-1]

# el resultado es:
# 0b000110100000111101000010100010101101001111111111010110011100111111011000011101110100110111101011111011000100011
