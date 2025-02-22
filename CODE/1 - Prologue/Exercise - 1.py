print("Benvenuto nel programma che ti permette di calcolare la serie di fibonacci!")
print()
contatore = int(input("Dimmi quanti numeri vuoi che io ti mostri della serie di fibonacci: "))
lista = [1, 1]
numero_1 = 1
numero_2 = 1
numero_3 = 0
for i in range(contatore):
    numero_3 = numero_1 + numero_2
    lista.append(numero_3)
    numero_1 = 0
    numero_1 = numero_3 + numero_2
    lista.append(numero_1)
    numero_2 = 0
    numero_2 = numero_1 + numero_3
    lista.append(numero_2)
    numero_3 = 0
lista[contatore ::] = []
print(f"La tua serie di fibonacci e: {lista}")
