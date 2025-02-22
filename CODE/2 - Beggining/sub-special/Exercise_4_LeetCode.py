class Pattern1:
    
    def _init_(self, base):
        self.B = base
    
    def ScalaBaseDestra(self):
        for x in range(self.B + 1):
            print("*"*x)
    
    def ScalaBaseDestraContrario(self):
            for x in range(self.B, 1, -1):
                print("*"*x)
   
    def ScalaBaseSinistra(self):
        stelline = 1
        for x in range(self.B, 0, -1):
            print(" "*x)
            print("*" * stelline)
            stelline += 1
     
    def ScalaBaseSinistraContrario(self):
        spazi = 0
        for x in range(self.B-1, 1, -1):
            print("*"*x)
            print(" " * spazi)
            spazi += 1
    
    def ScalaBaseSuEGiu(self):
        for x in range(-self.B, self.B + 1):
            if x == 0 or x == 1:
                pass
            elif x < 0:
                print("*" * -(x))
            else:
                print("*" * x)

class Pattern2:
    
    def Triangolo(n):
        for x in range(1, n+1):
            print(" " * (n - x) + " *" * x)
    
    def Rombo(n):
        for x in range(1, n):
            print(" " * (n - x) + " *" * x)
        for x in range(n, 0, -1):
            print(" " * (n - x) + " *" * x)
    
    def Clessidra(n):
        for x in range(n, 0, -1):
            print(" " * (n - x) + " *" * x)
        for x in range(1, n+1):
            print(" " * (n - x) + " *" * x)
    
    def Farfalla(n):
        for x in range(1, n):
            print("*" * x + " " * (n*2 - x*2) + "*" * x)
        for x in range(n, 0, -1):
            print("*" * x + " " * (n*2 - x*2) + "*" * x)

    def Parallelogramma(n):
        for x in range(1, n):
            print(" " * (n - x)+ " *" * n)    