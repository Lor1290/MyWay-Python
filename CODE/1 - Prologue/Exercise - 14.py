from random import randint
print("Ecco mdiecimila numeri generati casualmente: ")
lista_numeri = []
for i in range(10000):
    numeri = randint(0, 1000000)
    lista_numeri.append(numeri)
print()
print(lista_numeri)
print()
print(f"Il valore massimo presente è stato: {max(lista_numeri)}")
print()
print(f"IL valore minimo presente è stato: {min(lista_numeri)}")
print()
totale = sum(lista_numeri)
diviso = len(lista_numeri)
print(f"La media presente nella lista è stata di: {totale/diviso}")
    
