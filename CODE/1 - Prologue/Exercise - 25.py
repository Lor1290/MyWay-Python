lista_1 = []
lista_1 = input("Inserisci un numero indefinito di parole da te deciso, dividendole da uno spazio: ")
lista_2 = lista_1.split()
lista_3 = [len(i) for i in  lista_2]
print("Ecco gli elementi della lista" + str(lista_2))
print("Ecco poi la loro lunghezza" + str(lista_3))
