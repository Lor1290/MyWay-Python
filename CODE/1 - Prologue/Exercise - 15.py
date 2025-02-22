from random import randint
#Programma
tot = int(input("Quanti numeri random vuoi stampare sul nuovo file di testo? "))
tot_1 = []
for i in range(tot):
    n = randint(0, 1000000)
    tot_1.append(n)
tot_1.sort()
lista_somma = sum(tot_1)
lista_media = (lista_somma/len(tot_1))
#File
testo = open("Numeri.txt", "x")
testo.write("Numeri generati randomicamente - Esercitazione 1")
testo.writelines(["\nNumeri: " + str(tot_1), "\nSomma: " + str(lista_somma) + "  Media: "+ str(lista_media)])
testo.close()
