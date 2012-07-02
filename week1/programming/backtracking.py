# -*- coding: utf-8 -*-
import copy
import time

# Algoritmo de backtracking

lista = [[1,2,3],[4,5],[7,8,9,10],[],[11]]
lista_sol = []

def backtracking(i, key, lista, lista_sol):
    if(i == (len(lista) -1)):              
        for j in range(len(lista[i])):
            c_key = copy.deepcopy(key)
            c_key.append(lista[i][j])
            print 'imprimiendo clave: '+str(c_key)
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
                #print 'i='+str(i)+', j='+str(j)+'key: '+str(c_key)
                backtracking(i+1,c_key, lista, lista_sol)
                time.sleep(2)


#backtracking(0,[],lista, lista_sol)
#print len(lista_sol)

'''
Notese que al generar la lista aquellas sublistas con cero elemento contendran un -1
'''
lista_index = []
for i in range(len(lista)): 
    lista_index.append(len(lista[i]) - 1)

lista_index_init = copy.deepcopy(lista_index)

'''
Algoritmo para recorrer todas las posibilidades
'''
def generar_posibilidades(lista_index, i, lista_index_init):
    # IMPRESION SOLUCION
    #   (si hubiera indices con -1 denota que hay que introducir un caracter 'tonto')
    solucion = []
    for j in range(len(lista_index)):
        if lista_index[j] == -1:
            solucion.append(-2)
        else:
            solucion.append(lista_index[j])
    #print ''.join([str(c) for c in solucion])
    print lista_index

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



