
def Matrice_Triangolare(matrix):
    length, count, = len(matrix), 1
    for x in range(1, length):
        for y in range(count):
            if matrix[x][y] != 0:
                return False           
        count += 1
        
    return True

def Matrice_Diagonale(matrix):
    length = len(matrix)
    cell = 0
    for x in range(length):
        if matrix[x] == 0 and x == cell:
            return False
        
        for y in range(length): 
            if matrix[x][y] != 0 and y != cell:
                return False
        cell += 1

    return True

def Matrice_Trasporta(matrix):
    colonne = len(matrix)
    righe = len(matrix[0])
    tmp_matrix = []
    new_matrix = []

    for x in matrix:
        for y in x:
            tmp_matrix.append(y)

    print()
    new_matrix = [tmp_matrix[x: x+colonne] for x in range(0, (colonne*righe), colonne)]
    for x in new_matrix:
        print(x)

def Matrice_identità(length: int):
    new_matrix = [[] for x in range(length)]
    count = 0
    print(new_matrix)
    for x in range(length):
        for y in range(length):
            if y == count:
                new_matrix[x].append(1)
            else:
                new_matrix[x].append(0)
        count += 1
        
    print()
    for x in new_matrix:
        print(x)
       
Matrice_1 = [[5, 2, 7, 0, 3, 5],
             [0, 4, 7, 0, 2, 2],
             [0, 0, 6, 8, 4, 2],
             [0, 0, 0, 4, 3, 1],
             [0, 0, 0, 0, 7, 3],
             [0, 0, 0, 0, 0, 1]]

Matrice_2 = [[6, 0, 0, 0],
             [0, 4, 0, 0],
             [0, 0, 7, 0],
             [0, 0, 0, 1]]

Matrice_3 = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1],
             [1, 1, 1],
             [1, 1, 1],
             [1, 1, 1],
             [1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]

print(Matrice_Triangolare(Matrice_1))
print(Matrice_Diagonale(Matrice_2))
Matrice_Trasporta(Matrice_3)
Matrice_identità(10)
print()

def EliminaDuplicati():
    print("[s] Inserisci dei numeri nella lista, per ricorda...")
    print("[!] devi inserire dai 5 ai 30 numeri")
    print("[!] i numeri inseriti devo essere compresi tra -1000 e 1000")
    
    print("\n[+] Se tutto è chiaro, cominciamo!")
    
    cicle = True
    while cicle:
        print("[=] Inserisci i numeri nella lista: ")
        Array = list(map(int, input().split()))
        Array.sort()
        if len(Array) < 5 or len(Array) > 30:
            print("[!] Grandezza lista invalida")            
        elif Array[0] < -1001 or Array[len(Array)-1] > 1001:
            print("[!] Numeri inseriti invalidi")
        else:
            cicle = False

    print("\n", list(set(Array)))

EliminaDuplicati()

def Sequenza_di_fibonacci(num: int):
    def fibonacci(num: int):
        num_1, num_2, tmp = 0, 1, 1
        List = [num_1, num_2]

        for x in range(num):
            tmp += num_1 + num_2
            List.append(tmp)
            num_1 = tmp + num_2
            num_2 = tmp

        return List
        
    with open("Fibonacci Sequenze.txt", "a+") as file:
        List_W = fibonacci(num)
        file.write("\nSequenza generata: ")
        file.write("".join(str(x)+" " for x in List_W))

Sequenza_di_fibonacci(10)        
