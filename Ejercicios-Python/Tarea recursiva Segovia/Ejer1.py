def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)
n=int(input("Ingrese un numero: "))
print (fac(n))
