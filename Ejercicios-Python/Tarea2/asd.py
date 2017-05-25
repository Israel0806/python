##matriz multi

def multiplicacion(A,B):
    C=[]
##m=filas de A, p=filas de B n=co
    m=3
    n=2
    p=2
    q=3
    for k in range(m):
        C.append([0]*q)
        for i in range(q):
            C[k][i]=0
            
    for i in range(m):
        for j in range(n):
            for k in range(q):
                C[i][k]+=A[i][j]*B[j][k]
    for k in range(m):
        print C[k]



A=[[2, 6],[1, 5],[1, 3]]
B=[[9, 7, 8],[4, 6, 8]]

print multiplicacion(A,B)
