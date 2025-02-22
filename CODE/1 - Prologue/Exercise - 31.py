lista_colori = []

print("Inserisci dieci colori nella lista dei colori! ")
for i in range(10):
    colore = input()
    lista_colori.append(colore)

while True:
    prova = input("Di una lettera, ti trovero i colori che inizieranno con codesta: ")
    for i in range(len(lista_colori)):
        if i.lower()[0] == prova.lower():
            print(i)

