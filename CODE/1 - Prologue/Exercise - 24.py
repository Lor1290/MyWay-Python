from random import randint
n = int(input("Benvenuto nel programma che ti permette di determinare se il numero da te inserito è perfetto. Come unica cosa che dovrai fare, quindi, sarà dirmi codesto numero: "))
n1 = n
lista = []
conta = 0
if n % 2 != 0:
    print(f"{n} è un numero dispari, non può essere quindi un numero perfetto :(")
else:
    for i in range(1, n):
        conta = n - 1
        if (n % conta) == 0:
            lista.append(conta)
        n -= 1
    if sum(lista) == n1:
                print("Il tuo numero è perfetto!")
    else:
        print(lista)
        print("Il tuo numero non è perfetto...")
    
