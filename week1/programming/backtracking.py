import copy

# Algoritmo de backtracking

lista = [[1,2,3],[4,5],[7,8,9,10],[],[11]]
lista_sol = []

def backtracking(i, key, lista, lista_sol):
    if(i == (len(lista) -1)):              
        for j in range(len(lista[i])):
            c_key = copy.deepcopy(key)
            c_key.append(lista[i][j])
            #print 'imprimiendo clave: '+str(c_key)
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

backtracking(0,[],lista, lista_sol)
print len(lista_sol)
