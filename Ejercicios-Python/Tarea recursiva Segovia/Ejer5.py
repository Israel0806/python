def serie(n):
    if n==0:
        return 3
    return 3*serie(n-1)+4
n=int(input("Ingrese numero: "))
print (serie(n))
