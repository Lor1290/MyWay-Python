from random import randint
print("Benvenuto nel programma che ti permetterà di vedere una serie di liste create casualmente e messe poi in ordine")
print()
numero = int(input("Dimmi il range di numeri che vuoi io che crei: "))
print()
numero_1 = int(input("Dimmi poi, il valore massimo che vuoi sia presente: "))
lista_numeri = []
for i in range(numero):
    numeri = randint(0, numero_1)
    lista_numeri.append(numeri)
print()
lista_numeri.sort()
numeri_crescenti = lista_numeri 
print(f"La tua lista messa in ordine crescente sarà: {numeri_crescenti}")
print()
lista_numeri.reverse()
numeri_decrescenti = lista_numeri
print(f"La tua lista messa in ordine decrescente sarà: {numeri_decrescenti}")
    
