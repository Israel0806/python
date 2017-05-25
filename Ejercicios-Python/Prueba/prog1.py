def ingresar_lista(n, nombre):
    lista = []
    print 'Ingresar elementos de la Lista ' + nombre + ':'
    for c in range(0,n):
        num = input('Ingrese un numero: ')
        lista.append(num)
    print ''
    return lista

def sumar_elementos_lista(lista):
    suma = 0
    for c in range(0,len(lista)):
        suma += lista[c]
    return suma

def sumar_listas(lista1, lista2):
    lista3 = []
    if len(lista1)==len(lista2):
        for c in range(0,len(lista1)):
            num = lista1[c] + lista2[c]
            lista3.append(num)
    else:
        print 'No se puede sumar listas de diferentes tamanios'
    return lista3
        

num_a = input('Ingres la cantidad de elementos de A: ')
num_b = input('Ingres la cantidad de elementos de B: ')

A = ingresar_lista(num_a, 'A')
B = ingresar_lista(num_b, 'B')

print 'Lista A: ', A
print 'Lista B: ', B

print 'La suma de los elementos de A es: ', sumar_elementos_lista(A)
print 'La suma de los elementos de B es: ', sumar_elementos_lista(B)

C = sumar_listas(A,B)
print 'La suma de las listas A y B es: ', C

