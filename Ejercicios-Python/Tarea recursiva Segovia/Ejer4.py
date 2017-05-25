from random import *

def ma(lista,maximo):
    
    #print("1",maximo,"  ",lista)
    if len(lista)==1:
        return maximo
    if lista[1]>maximo:
        maximo=lista[1]
    else:
        lista.pop(1)
    #print ("2",maximo,"  ",lista)
    return ma(lista,maximo)
l=[]
for i in range(5):
    l.append(randrange(0,50))
maximo=l[0]
print(l)
print ("El maximo es: ",ma(l,maximo))
