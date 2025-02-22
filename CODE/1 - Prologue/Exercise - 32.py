import time

def matrice_ad_aspirale(num):
    lista_numeri = []
    lista_matrice = []
    num_alla_seconda = num**2
    
    contatore_1 = 0
    contatore_2 = 1
    
    
    for i in range(num_alla_seconda):
        lista_numeri.append(num_alla_seconda)
        num_alla_seconda -= 1

    lista_numeri.sort()
    
    for i in range(num):
        lista_matrice.append([])
    
    for i in lista_numeri:
        contatore_2 = 0
        if contatore_2 == 5:
                contatore_2 = 0
                contatore_1 -= 1
                lista_matrice[contatore_1].insert(1, i)
                
                while contatore_2 != 5
                if contatore_1 == 0:
                    lista_matrice[contatore_1].insert(1, i)
                    contatore_2 += 1
        try:         
            lista_matrice[contatore_1].append(i)
            contatore_1 += 1
        except IndexError:
            lista_matrice[contatore_1].insert(1, i)
            contatore_2 +=1



            

        
    print(*lista_matrice)

matrice_ad_aspirale(9)