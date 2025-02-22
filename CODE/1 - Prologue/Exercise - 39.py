#Esercitazione sulla serie di fibonacci

#Definizione principale
def Serie_Di_Fibonacci(lengh):

    val = []
    a = 0 #Variabile 1
    b = 1 #Variabile 2
    c = 0 #Variabile 3

    #Ciclo principale
    for i in range(lengh):
        a = c + b #Addizzione   
        val.append(a)
        b = a + c #Addizzione   
        val.append(b)
        c = a + b #Addizzione 
        val.append(c)

    print(*val)

print()
print("Benvenuto nel programma che ti permette di stampare la serie di Fibonacci")
print("Quante iterazioni vuoi fare?")
print("(P.S '1' iterazione -> '3' numeri)")

cicle_1 = True

while cicle_1:
    
    cicle_2 = True
    
    iterazioni = int(input())
    print()
    Serie_Di_Fibonacci(iterazioni)
    print()

    print("Adesso cosa vuoi fare?")
    print("Premi '1' -> Continui")
    print("Premi '2' -> Esci dal programma")
    
    while cicle_2:

        decisione = int(input("Cosa vuoi fare quindi? "))

        if decisione == 1:
            cicle_2 = False
        
        elif decisione == 2:
            
            print()
            print("Ciao, alla prossima!, e grazie per aver usato il mio programma")
            
            cicle_2 = False
            cicle_1 = False
        
        else:
            print()
            print("Hai sbagliato a dgitare, riprova")


