# -*- coding: utf-8 -*-
import sys
import string
import binascii

MSGS_E = ['315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a19b159610b11ef3e', '234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8356f','32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb','32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d835402bca670bda8eb775200b8dabbba246b130f040d8ec6447e2c767f3d30ed81ea2e4c1404e1315a1010e7229be6636aaa','3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b40aaa065f2a5e33a5a0bb5dcaba43722130f042f8ec85b7c2070','32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d11902aebc66f2b2e436434eacc0aba938220b084800c2ca4e693522643573b2c4ce35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983122b11be87a59c355d25f8e4','32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f83414aaaf261bda2e97b170fb5cce2a53e675c154c0d9681596934777e2275b381ce2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894473c1bbeb6b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce','315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c5474da2f276baa3ac325918b2daada43d6712150441c2e04f6565517f317da9d3','271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f1543efa270bda5e933421cbe88a4a52222190f471e9bd15f652b653b7071aec59a2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027','466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83', '32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904']

target = '32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904'


'''
    Returns the xor of two binary numbers given as a parameter
        with size the least of the given parameters
'''
def binary_xor(c,m):
    k = '0b'
    if len(c) > len(m):
        for i in range(2,len(m)):
            k+=str(int(m[i]) ^ int(c[i]))   
    else:
        for i in range(2,len(c)):
            k+=str(int(m[i]) ^ int(c[i]))   
    #print k
    return k

'''
    xor of two binary parameters. When the parameters are not 8 bit binary numbers
        they are expanded so that they have 9 bits
'''
def binary_xor_8bit(c,m):
    k = '0b'
    #f Erase the '0b' at the beggining
    c=c[2:]
    m=m[2:]
    # Fill with 0s until length equals 8
    while len(c) < 8:
        c='0'+c
    while len(m) < 8:
        m='0'+m
    for i in range(8):
        k+=str(int(m[i]) ^ int(c[i]))   
    return k

'''
    Returns the xor of the two parameters given in hexadecimal format
        NOTE: returns the xor in hexadecimal with size the least of the two parameters
'''
def hex_xor(m1, m2):
    m1_bin = bin(int(m1,16))
    m2_bin = bin(int(m2,16))
    res = binary_xor(m1_bin, m2_bin)
    hex_res =  hex(int(res,2))
    if 'L'== hex_res[-1]:
        return hex_res[2:-1]
    else:
        return hex_res[2:]

'''
    Similar to hex_xor but using the 8 bit xor operation
'''
def hex_xor_8bit(m1, m2):
    m1_bin = bin(int(m1,16))
    m2_bin = bin(int(m2,16))
    res = binary_xor_8bit(m1_bin, m2_bin)
    hex_res =  hex(int(res,2))
    if 'L'== hex_res[-1]:
        hex_res=hex_res[2:-1]
    else:
        hex_res=hex_res[2:]
    while len(hex_res) < 2:
        hex_res='0'+hex_res
    return hex_res

def calc_positivos(subkey, pos, c_set):
    count = 0
    for m in MSGS_E:
        if pos + 2 < len(m):
            subciph = m[pos:pos + 2]
            submess = hex_xor_8bit(subkey, subciph)
            #print 'xor de key='+subkey+' y ciphertext='+subciph+' ---> '+submess+' ('+chr(int(submess,16))+')'
            if (chr(int(submess,16)) in c_set):
                count = count + 1
        #print count
    return count

# Just interested in the size of the target (since the key k is the same)
longitud = len(target)

'''
# String with the caracters of interest
caracteres = ''
caracteres+=string.lowercase[:30]
caracteres+=string.uppercase[:30]
'''

# Other charset
caracteres = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM .,-1234567890'"
c_set = set(caracteres)
c_set_lectura = set("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ")
xor_table = []

'''
# Fill the xor_table (no tengo claro si este paso hay que hacerlo o no con 8bit)
for i in range(len(MSGS_E)-1):
    aux = []
    for j in range(i+1, len(MSGS_E)):
        r_hex = hex_xor(MSGS_E[i],MSGS_E[j])[:longitud]
        if len(r_hex) % 2 != 0:
            r_hex = '0'+r_hex    
        aux.append(r_hex)
    xor_table.append(aux)
'''

# Fill the xor_table
for i in range(len(MSGS_E)-1):
    aux = []
    for j in range(i+1, len(MSGS_E)):
        r_hex = ''.join([hex_xor_8bit(MSGS_E[i][z:z+2],MSGS_E[j][z:z+2]) for z in range(0,min(len(MSGS_E[i]),len(MSGS_E[j])),2)])
        r_hex = r_hex[:longitud]
        aux.append(r_hex)
    xor_table.append(aux)


#print [[t for t in c] for c in xor_table]

posibilidades = []  # posibilidades para cada una de los 83 caracteres (166 posiciones)
positivos = []      # positivos de cada uno de las 166 posiciones dadas las opciones en 'posibilidades'
keys = []            # clave final compuesta por las posibilidades con más positivos
for m in range(longitud):
    km_set = set()         # var auxiliar para almacenar las posibilidades en cada posicion k[m]. Es un conjunto porque puede haber repetidos (optimizacion)
    # Calculo de las posibilidades
    for c in caracteres:
        #print c
        c_hex = hex(ord(c))        # valor en hexadecimal del caracter con el cual se hace el xor
        for i in range(len(xor_table)):
            for j in range(len(xor_table[i])):
                #print 'Iteracion i='+str(i)+', j='+str(j)+', m='+str(m)
                if m + 2 <= len(xor_table[i][j]):        # necesario indexar el elemento m+2 en la tabla xor_table
                    #c_xor_hex = ''.join([hex_xor_8bit(xor_table[i][j][z]+xor_table[i][j][z+1],c_hex) for z in range(0,len(xor_table[i][j]),2)])
                    c_xor_hex = hex_xor_8bit(c_hex, xor_table[i][j][m:m+2])        # xor de (c_hex xor (m[v] xor m[z]))
                    #print 'resultado de '+c+' xor '+xor_table[i][j][m:m+2]+' = '+chr(int(c_xor_hex,16))
                    if chr(int(c_xor_hex,16)) in c_set_lectura:     
                        '''si c_hex xor (m[v] xor m[j]) == caracter valido, se supone que c_hex corresponde a m[v] o a m[z] y por tanto
                            se acaba teniendo (no se sabe cual de ellas asi que hay que valorar las dos posibilidades):
                                - m[z] o
                                - m[v] 
                            con esto, y dados los ciphertexts (c) en el enunciado:
                                - k = m xor c
                        '''    
                        km_set.add(hex_xor_8bit(c_xor_hex, MSGS_E[i][m:m+2])) 
                        km_set.add(hex_xor_8bit(c_xor_hex, MSGS_E[i+(j + 1)][m:m+2]))                     
                        #print '          key1: '+c_xor_hex+' xor '+MSGS_E[i][m:m+2]+' = ' +hex_xor_8bit(c_xor_hex, MSGS_E[i][m:m+2])
                        #print '          key2: '+c_xor_hex+' xor '+MSGS_E[i+(j + 1)][m:m+2]+' = ' +hex_xor_8bit(c_xor_hex, MSGS_E[i+(j + 1)][m:m+2])
                       
    posibilidades.append(list(km_set))

# Computo de los 'positivos' de cada posibidad
for i in range(len(posibilidades)):
    aux = []
    for j in range(len(posibilidades[i])):
        aux.append(calc_positivos(posibilidades[i][j],i, c_set_lectura))
    positivos.append(aux)

# Selección de el mejor positivo por cada posición y formación de la clave (k)
for i in range(len(positivos)):
    if len(positivos[i]) > 0:
        c_max = max(positivos[i])
        for j in range(len(positivos[i])):
            #print 'i='+str(i)
            #print 'j='+str(j)
            if positivos[i][j] == c_max:
                keys.append(posibilidades[i][j])
                break
        
key = ''.join([c for c in keys])

#key = '665139306ece89eec9efdb0ad8c3cbbb98a07431355e2a8bcda1635b952410552e98afdace8378acaac27fd8edb028dca0765e446bdec9fe8d0429eec5260bd869c9b071331e9ad41928f8ecaad240771acf9c346da1702f8f88805bc05a666bc7016368fe98f0571285317548fbcd88d8f9e8f7025fd0725bd8a9d88751770433635db8ae99fc7cecafd52f9c9543253a806bc0263a8b10609fbf924e9df0743c8f9ac461'

message = ''.join([chr(int(hex_xor_8bit(key[z:z+2],target[z:z+2]),16)) for z in range(0,min(len(key),len(target)),2)])
#message_ASCII = binascii.unhexlify(message)
#print message_ASCII
print message

#print [[t for t in c] for c in posibilidades]
#print [[t for t in c] for c in positivos]
#print key
