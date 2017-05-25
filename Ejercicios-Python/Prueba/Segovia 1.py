n=input("Como te llamas?= ")

try:
    assert n.isalpha()
except:
    print("El nombre contiene cifras") 


try:
   e=int(input("Cual es tu edad?= "))
   assert e>0 and e<130
except AssertionError:
    print("Error al ingresar edad")
except ValueError:
    print("La edad tiene letras")   

