n = []
n_1 = input("inserisci una lista di elementi: ")
n.append(n_1)
n_1.split()
n_2 = input("facciamo adesso una conferma: prova a mettere un valore a tuo piacimento e vediamo se è nella lista: ")
if n_2 in n_1:
    s = n_1.index(n_2)
    print("il tuo elemento è presente, e si trova nella posizione: " + str(s))
else:
    print("mi dispiace, il tuo elemento non è presente, riprova un altra volta, addio!")

