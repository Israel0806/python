def potencia(a,b):
    if b==1:
        return a
    return a*potencia(a,b-1)
print("Ingrese dos numeros\n")
a=int(input())
b=int(input())
print (potencia(a,b))
