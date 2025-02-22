class MatriceAdAspirale():
    def __init__(self, num: int, new_array = [], count1 = 0, count2 = 0):
        self.nm = new_array
        self.n2 = num**2
        self.c1 = count1
        self.c2 = count2
        self.n = num

    
    def array(self) -> list:
        
        for x in range(self.n):
            self.nm.append([])
        
        for y in self.nm:
            for z in range(self.n):
                y.append([])
    
        for i in range(1, self.n2 +1):
            self.nm[]

        return self.nm

print(MatriceAdAspirale(5).matrice()) 