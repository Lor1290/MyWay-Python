#Application to compleate a 'Magic Cube'

import random as rm

#MagicCube
class MagicCube:
    def __init__(self, num):
        self.num = num
        self.nums = num**2
        self.K = num*(num**2 +1)/2
    def square(self):
        
        c = 0 #Counter
        matrix = [] 
        matrix_ext = []
        
        for x in range(1, self.nums + 1): #Creating the first list
            matrix.append(x)
        
        for y in range(self.num): #Dividing the element inthe list
            matrix_ind = []
            
            for z in range(self.num):
                matrix_ind.append(matrix[c])
                c += 1 #Increasing the counter
            
            matrix_ext.append(matrix_ind)
        
        row, colum, diagonal1, diagonal2 = self.K, self.K, self.K, self.K

        for i in matrix_ext:
            for j in i:
                
    
MC = MagicCube(5)
print(MC.square())
        