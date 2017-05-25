def palindrome(a):
    if len(a)==0:
        if l2==l1:
            print ("La palabra ingresada es palindrome")
        else:
            print ("La palabra ingresada no es palindrome")
    l2=l2+a[-1]
    a.pop(a[-1])
    print (l2)
    return palindrome(l)
a=input("Ingrese una palabra: ")
print(palindrome(a)
