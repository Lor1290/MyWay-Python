class Piramidi:
    
    def __init__(self, length):
        self.len = length
    
    def ScalaSemplice(self):
        for x in range(1, self.len + 1):
            print("*" * x)
    
    def ScalaAlContrario(self):
        for x in range(self.len + 1, 1, -1):
            print("*" * x)
    
    def ScalaBuffa(self):
        for x in range(self.length + 1, 1, -1):
            print("*" * x)
        for x in range(2, self.length + 1):
            print("*" * x)
    
    def ScalaReverse(self):
        for x in range(0, self.lengh):
            print("" * x)
            print("*" * self.lenght - x)
