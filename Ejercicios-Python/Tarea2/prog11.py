num_f = input('Ingrese la cantidad de filas: ')
num_c = input('Ingrese la cantidad de columnas: ')

m = []

print ''
print 'Ingresar los elementos de la matriz:'
print ''

for f in range(0,num_f):
    lista_aux = []
    for c in range(0,num_c):
        num = input('Ingrese un elemento: ')
        lista_aux.append(num)
    print 'lista_aux: ', lista_aux
    m.append(lista_aux)

print ''
print 'Los elementos ingresados a la matriz son:'
print ''

for f in range(0,num_f):
    print m[f]

print ''
print 'La suma de todos los elementos de la matriz es:'

suma = 0
for f in range(0,len(m)):
    for c in range(0,len(m[0])):
        suma += m[f][c]

print suma
print ''

print 'La suma los elementos de cada fila de la matriz es:'

for c in range(0,len(m[0])):
    suma = 0
    for f in range(0,len(m)):
        suma += m[f][c]
    print 'Columna ' + str(c) + ': ' + str(suma)

