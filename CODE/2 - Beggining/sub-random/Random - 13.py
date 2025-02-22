import time

def matrice_ad_aspirale():
    decision = True

    while decision:
        try:
            num = int(input("Inderisci un numero di cui vuoi sapere la sua matrice a forma aspirale: "))
            decision = False
        except ValueError:
            print("hai sbagliato a digitare, riprova")
        
        lista_num = []
        lista_num_matrice = []
        num_elevato = num ** 2

        
        for i in range(1, num_elevato + 1):
            lista_num.append(i)
        
        for i in range(num):
            lista_num_matrice.append([])
        
        lista_num.sort()
        print(lista_num)

        J = -1 #Index_1
        K = 0 #Position
        L = 0 #Pattern
        M = 0 #index_2

        while (num - L) > 0:

            for i in lista_num:
                
                for A in range(num - L):
                    J += 1
                    lista_num_matrice[J].insert(K, lista_num[M])
                    M += 1
                
                L += 1

                for B in range(num - L):
                    K += 1
                    lista_num_matrice[J].insert(K, lista_num[M])
                    M += 1
                
                for C in range(num - L):
                    J -= 1
                    K = 1
                    lista_num_matrice[J].insert(K, lista_num[M])
                    M += 1
                
                L += 1

                for D in range(num - L):
                    J -= 1
                    lista_num_matrice[J].insert(K, lista_num[M])
                    M += 1
        
        for i in lista_num_matrice:
            print(*i)
            time.sleep(0.5)

matrice_ad_aspirale()