# -*- coding: utf-8 -*-
import sys
import string
import binascii
import copy
import time

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

def backtracking(i, key, lista, lista_sol):
    if(i == (len(lista) -1)):              
        for j in range(len(lista[i])):
            c_key = copy.deepcopy(key)
            c_key.append(lista[i][j])
            lista_sol.append(c_key)
    else:                                 
        if(len(lista[i]) == 0):
            c_key = copy.deepcopy(key)
            c_key.append('00')
            backtracking(i+1,c_key, lista, lista_sol)
        else:
            for j in range(len(lista[i])):
                c_key = copy.deepcopy(key)
                c_key.append(lista[i][j])
                backtracking(i+1,c_key,lista, lista_sol)

def backtracking_xor_hex(i, key, lista, lista_sol):
    if(i == (len(lista) -1)):              
        for j in range(len(lista[i])):
            c_key = copy.copy(key)
            c_key.append(lista[i][j])
            lista_sol.append(c_key)
            key_candidate = ''.join([c for c in c_key])
            message = ''.join([chr(int(hex_xor_8bit(key_candidate[z:z+2],target[z:z+2]),16)) for z in range(0,min(len(key_candidate),len(target)),2)])
            print message
    else:                                 
        if(len(lista[i]) == 0):
            c_key = copy.copy(key)
            c_key.append('00')
            print '     key candidate for now: '+str(c_key)
            backtracking(i+1,c_key, lista, lista_sol)
        else:
            for j in range(len(lista[i])):
                c_key = copy.copy(key)
                c_key.append(lista[i][j])
                print '     key candidate for now: '+str(c_key)
                backtracking(i+1,c_key,lista, lista_sol)


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

'''
# Fill the xor_table
for i in range(len(MSGS_E)-1):
    aux = []
    for j in range(i+1, len(MSGS_E)):
        r_hex = ''.join([hex_xor_8bit(MSGS_E[i][z:z+2],MSGS_E[j][z:z+2]) for z in range(0,min(len(MSGS_E[i]),len(MSGS_E[j])),2)])
        r_hex = r_hex[:longitud]
        aux.append(r_hex)
    xor_table.append(aux)


start = time.time()

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
                        ''''''si c_hex xor (m[v] xor m[j]) == caracter valido, se supone que c_hex corresponde a m[v] o a m[z] y por tanto
                            se acaba teniendo (no se sabe cual de ellas asi que hay que valorar las dos posibilidades):
                                - m[z] o
                                - m[v] 
                            con esto, y dados los ciphertexts (c) en el enunciado:
                                - k = m xor c
                        ''''''    
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
'''
'''
# Selección delos mejores positivos por cada posición y formación de la clave (k)
for i in range(len(positivos)):
    if len(positivos[i]) > 0:
        c_max = max(positivos[i])
        for j in range(len(positivos[i])):
            #print 'i='+str(i)
            #print 'j='+str(j)
            if positivos[i][j] == c_max:
                keys.append(posibilidades[i][j])
                break
        
        '''
'''        
# Seleccion de un c onjunto de mejores positivos para cada opcion        
for i in range(len(positivos)):
    if len(positivos[i]) > 0:
        aux = []
        for j in range(len(positivos[i])):
            if positivos[i][j] > 8:
                aux.append(posibilidades[i][j])
        keys.append(aux)        

elapsed = (time.time() - start)
print str(elapsed)+' segundos en generar las posibilidades (selección de mejores positivos incluída)'
print keys

'''
# The following keys generate 9830999239967990119213554050935081910326249610271258957368524800000000L combinations
keys = [['5e', '5d', '5a', '5b', '59', '55', '54', '57', '56', '50', '53', '60', '61', '62', '64', '65', '66', '67', '68', '6b', '7e', '7d', '7b', '7a', '48', '46', '47', '44', '45', '42', '40', '41', '77', '76', '75', '74', '73', '70', '79', '4b'], ['51', '46'], ['24', '25', '26', '28', '29', '2b', '06', '04', '05', '08', '09', '3b', '3a', '3f', '3e', '3d', '39', '38', '37', '35', '34', '0b', '1a', '1b', '1e', '1d', '1f', '15', '14', '17', '19', '18'], [], ['6e'], [], ['89'], ['d8', 'd9', 'd2', 'd3', 'd0', 'cc', 'df', 'dd', 'de', 'dc', 'ee', 'ed', 'ef', 'ec', 'eb', 'e9', 'e8', 'e3', 'e2', 'fd', 'f0', 'ff', 'cb', 'cf', 'ce', 'cd', 'c9', 'c8', 'c3', 'c2', 'f2', 'f3', 'f8', 'f9', 'fc', 'fe'], ['d8', 'd9', 'df', 'dd', 'de', 'dc', 'ee', 'ed', 'ef', 'ea', 'eb', 'e9', 'e1', 'e3', 'e2', 'cb', 'ca', 'cf', 'ce', 'cd', 'c9', 'c3', 'c2', 'c1', 'f8', 'f9', 'fc', 'fd', 'fe', 'ff'], ['ef'], ['db'], [], ['c3', 'd8', 'df', 'dd', 'de', 'dc', 'da', 'e1', 'e3', 'c1', 'f8', 'fa', 'fc', 'fd', 'fe', 'ff'], [], ['d3', 'd0', 'db', 'da', 'ee', 'ed', 'ef', 'ea', 'ec', 'eb', 'e9', 'e8', 'e7', 'e6', 'cc', 'cb', 'ca', 'cf', 'ce', 'cd', 'c9', 'c8', 'c7', 'c6', 'f0', 'f3', 'fa', 'fb'], [], ['b4', 'b5', '88', '89', 'be', 'bf', 'ba', 'bb', 'bc', '8b', '8a', '8f', '8d', '8e', '9a', '9c', '9b', '9e', '9f', '99', '98', '95', '94', '96', 'b6', 'aa', 'ab', 'ae', 'ad', 'af', 'b8', 'b9', 'a9', 'a8'], ['a0'], ['74'], [], ['35'], [], ['24', '27', '28', '29', '2d', '2e', '2a', '2b', '2c', '07', '04', '08', '09', '37', '36', '35', '0b', '0c', '0a', '0d', '0e', '15', '17', '16'], [], ['d2', 'd0', 'd1', 'c7', 'c5', 'db', 'ee', 'ed', 'ef', 'ea', 'ec', 'eb', 'e9', 'e5', 'e4', 'e7', 'e6', 'cc', 'cb', 'ca', 'cf', 'ce', 'cd', 'c9', 'c6', 'c4', 'f0', 'f1', 'f2', 'fa', 'fb', 'da'], [], ['63'], [], ['95'], [], ['25', '26', '27', '21', '22', '23', '28', '2b', '02', '03', '01', '06', '07', '05', '08', '3a', '39', '33', '30', '0b', '1a', '10', '13', '19'], [], ['24', '26', '27', '28', '29', '2d', '2e', '2f', '2a', '2b', '2c', '06', '07', '04', '08', '09', '3b', '39', '38', '0b', '0c', '0a', '0f', '0d', '0e', '1b', '19', '18'], [], ['84', '85', '8b', '8c', '8f', '8e', 'a5', 'a4', '88', '89', 'ac', 'ab', 'ae', 'af', '87', 'a7', 'a9', 'a8'], [], ['d8', 'd9', 'd2', 'd3', 'd0', 'c5', 'c4', 'ee', 'ed', 'ef', 'ec', 'eb', 'e9', 'e8', 'e5', 'e4', 'e7', 'cc', 'cb', 'cf', 'ce', 'cd', 'c9', 'c8', 'c7', 'f0', 'f2', 'f3', 'f8', 'f9', 'fa', 'da'], [], ['59', '58', '55', '54', '68', '69', '6b', '48', '49', '75', '74', '79', '78', '4b'], [], ['aa'], [], ['5e', '5f', '51', '50', '52', '6c', '6d', '6e', '7f', '7e', '72', '71', '70', '4d', '4e', '4c'], [], ['ed'], [], ['28', '29', '2e', '2f', '2a', '2c', '08', '09', '3b', '38', '0c', '0a', '0f', '0e', '1b', '18'], [], ['9d', '83', '80', '81', 'b8', 'bd', 'be', 'bf', 'ba', 'bb', 'bc', '8b', '8a', 'a0', '9a', '9c', '9b', '9e', '9f', '98', 'aa', 'ab', 'a1', 'a3'], [], ['5e', '5f', '5c', '55', '54', '57', '56', '52', '60', '62', '63', '68', '69', '6a', '6b', '7f', '7e', '7c', '48', '49', '42', '43', '40', '77', '76', '75', '74', '72', '4b', '4a'], [], ['6b'], [], ['c9'], ['fe'], ['92', 'b0', 'b2', 'b3', '8c', '8d', '8e', '90', '93', 'ac', 'ae', 'ad'], [], ['22', '23', '28', '29', '2d', '2e', '2f', '2a', '2b', '2c', '02', '03', '08', '09', '3a', '39', '38', '0b', '0c', '0a', '0f', '0d', '0e', '1a', '19', '18'], [], ['c5'], [], ['0b'], [], ['60', '63', '69', '6a', '6b', '6c', '6d', '6f', '49', '43', '40', '4f', '4d', '4b', '4c', '4a'], [], ['b0'], [], ['33'], [], ['9a'], [], ['3b', '3f', '3e', '3d', '39', '38', '1b', '1e', '1d', '1f', '14', '19', '18'], [], ['d8', 'd9', 'df', 'de', 'db', 'da', 'cf', 'ee', 'ef', 'e9', 'e8', 'e5', 'e4', 'ce', 'c9', 'c8', 'c5', 'c4', 'f8', 'f9', 'fa', 'fb', 'fe', 'ff'], [], ['9d', 'b5', 'b6', '89', 'bd', 'ba', 'bb', 'bc', '8b', '8a', '9a', '9c', '9b', '95', '97', '96', 'b7', 'aa', 'ab', 'a9'], [], ['40'], [], ['2d', '2c', '3a', '3f', '3e', '3d', '39', '38', '0c', '0d', '1a', '1e', '1d', '1f', '19', '18'], [], ['86', '87', 'bd', 'bc', '9c', '9d', 'a7', 'a6'], [], ['6d'], [], ['55', '54', '57', '56', '51', '50', '53', '52', '65', '67', '69', '6a', '6b', '6c', '6d', '6f', '49', '47', '45', '77', '76', '75', '74', '73', '72', '71', '70', '4f', '4d', '4b', '4c', '4a'], [], ['8f'], [], ['96', 'b4', '88', 'b1', 'b3', '82', '83', '80', '84', '8a', '8f', '8d', '91', '93', '94', 'b6', 'aa', 'ad', 'af', '86', 'a0', 'a3', 'a2', 'a4', 'a6', 'a8'], [], ['c0', 'c6', 'c4', 'e5', 'e4', 'e6', 'e1', 'e0', 'e2', 'c2', 'c1', 'c5'], [], ['5b', '59', '60', '62', '64', '65', '66', '67', '68', '6b', '6c', '6d', '6e', '7b', '48', '46', '47', '44', '45', '42', '40', '79', '4d', '4e', '4b', '4c'], [], ['c3', 'd8', 'd9', 'd2', 'd0', 'd1', 'c0', 'c4', 'df', 'dd', 'db', 'dc', 'ed', 'ef', 'e4', 'e7', 'e6', 'e0', 'e3', 'e2', 'cf', 'cd', 'c7', 'c6', 'f0', 'f1', 'f2', 'f8', 'f9', 'fb', 'fc', 'fd', 'ff', 'c2'], [], ['5e', '5f', '5c', '52', '60', '62', '63', '7f', '7e', '7c', '42', '43', '40', '72'], [], ['fe'], [], ['f0'], [], ['28', '29', '2d', '2e', '2f', '2a', '2b', '2c', '08', '09', '3c', '33', '32', '31', '30', '37', '36', '35', '34', '0b', '0c', '0a', '0f', '0d', '0e', '1c', '11', '10', '13', '12', '15', '14', '17', '16'], [], ['33', '32', '31', '37', '36', '35', '11', '13', '12', '15', '17', '16'], [], ['48'], [], ['cd'], [], ['d8', 'd4', 'd5', 'd2', 'd0', 'd1', 'dd', 'de', 'db', 'dc', 'da', 'cf', 'ee', 'ef', 'ce', 'f0', 'f1', 'f2', 'f4', 'f5', 'f8', 'fa', 'fb', 'fc', 'fd', 'fe'], [], ['e8'], [], ['24', '25', '22', '23', '02', '03', '04', '05'], [], ['d6', 'd7', 'd4', 'd2', 'd3', 'd0', 'd1', 'c0', 'db', 'ed', 'ef', 'ec', 'e1', 'e0', 'cc', 'cf', 'cd', 'c1', 'f0', 'f1', 'f2', 'f3', 'f4', 'f6', 'f7', 'fa', 'fb', 'da'], [], ['5d', '5f', '5c', '5b', '59', '58', '7f', '7d', '7c', '7b', '79', '78'], [], ['b0', 'b1', 'b2', 'b3', 'bd', 'be', 'bf', '8b', '8c', '8a', '8f', '8d', '8e', '9e', '9d', '9f', '91', '90', '93', '92', '88', '89', 'aa', 'ac', 'ab', 'ae', 'ad', 'af', 'a9', 'a8'], [], ['83', '80', '81', '86', '87', '84', '85', 'ba', 'bb', '8c', '8d', '9a', '9b', '98', 'ac', 'ad', 'b8', 'a1', 'a0', 'a3', 'a5', 'a4', 'a7', 'a6'], [], ['77'], [], ['33'], [], ['5e', '5d', '5f', '5a', '5c', '5b', '59', '58', '54', '57', '61', '62', '63', '64', '65', '66', '68', '6a', '6b', '6c', '6f', '7f', '7e', '7d', '7c', '7b', '7a', '48', '46', '44', '45', '42', '43', '41', '77', '74', '79', '78', '4f', '4b', '4c', '4a'], [], ['ae'], [], ['d9', 'd0', 'd1', 'df', 'dd', 'de', 'db', 'dc', 'da', 'ea', 'eb', 'e4', 'e7', 'e6', 'e1', 'e0', 'e3', 'e2', 'cb', 'ca', 'c3', 'c2', 'c1', 'c0', 'c7', 'c6', 'c4', 'f0', 'f1', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff'], [], ['d7', 'd5', 'ee', 'ea', 'ec', 'eb', 'e9', 'e8', 'e1', 'cc', 'cb', 'ca', 'ce', 'c9', 'c8', 'c1', 'f5', 'f7', 'fa', 'da'], [], ['d5'], [], ['9f', 'be', 'bf', 'ba', 'bb', 'bc', '9a', '9c', '9b', '9e'], [], ['5d', '5f', '5c', '55', '54', '60', '61', '62', '63', '64', '66', '67', '7f', '7d', '7c', '46', '47', '44', '42', '43', '40', '41', '75', '74'], [], ['26', '29', '2a', '2b', '06', '09', '3b', '3a', '3e', '3d', '39', '38', '32', '31', '30', '37', '36', '35', '34', '0b', '0a', '1a', '1b', '1e', '1d', '11', '10', '12', '15', '14', '17', '16', '19', '18'], [], ['6b'], [], ['26', '20', '22', '23', '02', '03', '00', '06', '33', '30', '10', '13'], [], ['91', '92', '94', '97', '96', 'b4', 'b5', '88', '89', 'b0', 'b1', 'b2', 'b3', '80', '81', '8b', '8c', '8a', '8f', '8d', '8e', '90', '93', '95', 'b6', 'b7', 'aa', 'ac', 'ab', 'ae', 'ad', 'af', 'a1', 'a0', 'a9', 'a8'], [], ['5b', '57', '56', '60', '61', '62', '63', '64', '66', '67', '6c', '6d', '7b', '46', '47', '44', '42', '43', '40', '41', '77', '76', '4d', '4c'], [], ['b5', '82', '83', '80', '81', '84', '85', 'be', 'bf', 'bc', '8b', '8a', 'a0', 'a2', '9c', '9e', '9f', '95', '88', '89', 'aa', 'ab', '87', 'a1', 'a3', 'a5', 'a4', 'a7', 'a9', 'a8'], [], ['4e'], [], ['d6', 'd4', 'd2', 'd0', 'd1', 'c7', 'dc', 'e7', 'fc', 'f0', 'f1', 'f2', 'f4', 'f6'], [], ['28', '29', '2d', '2a', '2b', '2c', '08', '09', '3c', '3b', '3f', '3e', '38', '37', '36', '34', '0b', '0c', '0a', '0d', '1c', '1b', '1e', '1f', '14', '17', '16', '18'], [], ['9a'], [], ['61']]

# A PARTIR DE ESTE PUNTO SE PRESENTAN DIFERENTES TÉCNICAS PARA INTENTAR CALCULAR TODAS LAS DIFERENTES POSIBILIDADES DADO EL CONJUNTO DE CLAVES,
# NO OBSTANTE, DEBIDO AL NÚMERO TAN ELEVADO DE POSIBILIDADES, NO RESULTA POSIBLE GENERAR TODAS ELLAS


'''
# Backtracking y generar todas las posibles combinaciones de claves. Utilizar un diccionario para detectar qué combinaciones son mejores y cuales peores.
start = time.time()
key_candidates = []
backtracking_xor_hex(0, [], keys, key_candidates)
elapsed = (time.time() - start)
print str(elapsed)+' segundos en generar las claves candidatas con backtracking'
print '----------------'
print key_candidates

# Método alternativo utilizando una lista de índices:
lista_almacen = []
lista = keys
#Notese que al generar la lista aquellas sublistas con cero elemento contendran un -1
lista_index = []
for i in range(len(lista)): 
    lista_index.append(len(lista[i]) - 1)

lista_index_init = copy.deepcopy(lista_index)

Algoritmo para recorrer todas las posibilidades
def generar_posibilidades(lista_index, i, lista_index_init):
    # IMPRESION SOLUCION
    #   (si hubiera indices con -1 denota que hay que introducir un caracter 'tonto')
    solucion = []
    for j in range(len(lista_index)):
        if lista_index[j] == -1:
            solucion.append('00')
        else:
            solucion.append(lista[j][lista_index[j]])
    lista_almacen.append(lista_index)
    #print lista_index
    #print len(lista_almacen)
    key_candidate = ''.join([c for c in solucion])
    message = ''.join([chr(int(hex_xor_8bit(key_candidate[z:z+2],target[z:z+2]),16)) for z in range(0,min(len(key_candidate),len(target)),2)])
    print message

    # CONTNUAR SOLO SI NO SE HA LLEGADO AL FINAL
    continue_flag = False
    for m in range(len(lista_index)):
        if(lista_index[m] > 0):
            continue_flag = True 
            break
    
    if(continue_flag):
        # SIGUIENTE ITERACION
        #print 'i='+str(i)+', lista_index[i]='+str(lista_index[i])
        flag = True
        flag_init = False           # Este flag se activa cuando se detecta que se llega a 0. Hace que se empiece a descender desde la ultima posicion de nuevo
        while flag:
            if lista_index[i] == -1:
                i= i-1
            elif lista_index[i] == 0:     # si se ha llegado al principio de uno de los indices, se resta uno al anterior y se vuelve a su valor maximo
                lista_index[i] = lista_index_init[i]
                i = i-1
                flag_init = True
            else:
                lista_index[i] = lista_index[i] - 1
                flag = False            # salir del bucle
        if flag_init:
            generar_posibilidades(lista_index,len(lista_index) -1, lista_index_init)
        else:
            generar_posibilidades(lista_index,i, lista_index_init)
        
generar_posibilidades(lista_index, len(lista_index) - 1, lista_index_init)



# Método sin utilizar recursividad. Se genera el array directamente y se van imprimiendo las soluciones según se generan
def generar_posibilidades(lista_index, i, lista_index_init):

    # IMPRESION SOLUCION
    #   (si hubiera indices con -1 denota que hay que introducir un caracter 'tonto')
    solucion = []
    for j in range(len(lista_index)):
        if lista_index[j] == -1:
            solucion.append('00')
        else:
            solucion.append(lista[j][lista_index[j]])
    lista_almacen.append(lista_index)
    #print lista_index
    #print len(lista_almacen)
    key_candidate = ''.join([c for c in solucion])
    message = ''.join([chr(int(hex_xor_8bit(key_candidate[z:z+2],target[z:z+2]),16)) for z in range(0,min(len(key_candidate),len(target)),2)])
    print message

    continue_flag = True
    while(continue_flag):

        # SIGUIENTE ITERACION
        flag = True
        flag_init = False           # Este flag se activa cuando se detecta que se llega a 0. Hace que se empiece a descender desde la ultima posicion de nuevo
        while flag:
            if lista_index[i] == -1:
                i= i-1
            elif lista_index[i] == 0:     # si se ha llegado al principio de uno de los indices, se resta uno al anterior y se vuelve a su valor maximo
                lista_index[i] = lista_index_init[i]
                i = i-1
                flag_init = True
            else:
                lista_index[i] = lista_index[i] - 1
                flag = False            # salir del bucle
        if flag_init:
            #generar_posibilidades(lista_index,len(lista_index) -1, lista_index_init)
            i = len(lista_index) - 1

            # IMPRESION SOLUCION
            #   (si hubiera indices con -1 denota que hay que introducir un caracter 'tonto')
            solucion = []
            for j in range(len(lista_index)):
                if lista_index[j] == -1:
                    solucion.append('00')
                else:
                    solucion.append(lista[j][lista_index[j]])
            lista_almacen.append(lista_index)
            #print lista_index
            #print len(lista_almacen)
            key_candidate = ''.join([c for c in solucion])
            message = ''.join([chr(int(hex_xor_8bit(key_candidate[z:z+2],target[z:z+2]),16)) for z in range(0,min(len(key_candidate),len(target)),2)])
            print message

        else:
            #generar_posibilidades(lista_index,i, lista_index_init)

            # IMPRESION SOLUCION
            #   (si hubiera indices con -1 denota que hay que introducir un caracter 'tonto')
            solucion = []
            for j in range(len(lista_index)):
                if lista_index[j] == -1:
                    solucion.append('00')
                else:
                    solucion.append(lista[j][lista_index[j]])
            lista_almacen.append(lista_index)
            #print lista_index
            #print len(lista_almacen)
            key_candidate = ''.join([c for c in solucion])
            message = ''.join([chr(int(hex_xor_8bit(key_candidate[z:z+2],target[z:z+2]),16)) for z in range(0,min(len(key_candidate),len(target)),2)])
            print message
            

        # CONTNUAR SOLO SI NO SE HA LLEGADO AL FINAL
        continue_flag = False
        for m in range(len(lista_index)):
            if(lista_index[m] > 0):
                continue_flag = True 
                break


start = time.time()
generar_posibilidades(lista_index, len(lista_index) - 1, lista_index_init)
elapsed = (time.time() - start)
print str(elapsed)+' segundos en terminar'
'''




