# Programa que resuelve el caso propuesto en el test
import operator, binascii

c=bin(int('6c73d5240a948c86981bc294814d', 16))
m=bin(int(binascii.hexlify('attack at dawn'), 16))
k = [0, 'b']
for i in range(2,len(m)):
    k.append(int(m[i]) ^ int(c[i]))

print m
print c
print k
