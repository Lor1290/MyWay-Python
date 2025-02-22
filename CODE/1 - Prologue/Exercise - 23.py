print("Benvenuto nel programma che ti calcola la statistica di numeri Random!")
print()
from random import randint
lista_random = []
lista_pari = []
lista_over_70 = []
lista_varianza = []
lista_varianza1 = []
for i in range(20):
    numeri_random = randint(1, 100)
    lista_random.append(numeri_random)
tot = sum(lista_random) / 20
for i in lista_random:
    if i > 70:
        lista_over_70.append(i)
    elif i % 2 == 0:
        lista_pari.append(i)
for i in lista_random:
    i -= tot
    lista_varianza.append(i)
for i in lista_varianza:
    i *= i
    lista_varianza1.append(i)
tot1 = sum(lista_varianza1)
varianza = (tot1/20)
print("La lista dei numeri pari che sono stati casualmente genrati e superano il valore di 70 sono: ")
print(f"--> {lista_over_70}")
print()
print("La lista dei numeri pari che sono stati casualmente generati e non superano il valore di 70 sono, invece: ")
print(f"-->{lista_pari}")
print()
print(f"La media matematica di tutti i numeri è stata: {tot}")
print()
print(f"La varianza di tutti i numeri è invece: {varianza}")



    
