class a:
    def __init__(self):
        self.num=0

    def agre(self):
        self.num+=1

    def imprimir2(self):
        print self.num
    
class b(a):
    def __init__(self):
        a.__init__()
        self.num2=32

    def imprimir(self):
        print self.num2
##        print self.num
        a.imprimir2()
        
a=a()
a.agre()
##asd.agre()
##aa.imprimir2()
##asd.imprimir2()
aa=b()
##aa.agre()
aa.imprimir()
