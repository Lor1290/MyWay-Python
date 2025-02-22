print("Benvenuto nel programma che ti permette di calcolare la somma di tutti i numeri che vengono prima del tuo numero deciso e dato in input")
print()
numero = int(input("Dimmi quindi, come singola cosa, quale numero vuoi utilizzare? "))
somma = 0
for i in range(numero):
    somma += i
print(f"La tua somma è: {somma}")
