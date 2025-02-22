print("Benvenuto nel programma che ti permette di creare una lista di numeri (i numeri che dovrai inseirire andranno da 5 a 30) senza far si che questi ultimi si ripetano. Senza altre spiegazioni, quindi, inziamo!")
print()
global scelta
scelta = int(input("Per prima cosa, dimmi quante volte vuoi fare questo procedimento? "))
for i in range(scelta):
             print()
             numeri = input("Inseriscimi la lista di numeri che vorrai utilizzare: ")
             numeri_lista = set()
             numeri_lista = numeri.split()
             numeri_lista = [float(i) for i in numeri_lista]
             lunghezza_lista = len(numeri_lista)
             if lunghezza_lista < 5 or lunghezza_lista > 30:
                print(lunghezza_lista)
                print("Hai messo o troppi, o troppi pochi valori, riprova")

             elif min(numeri_lista) < -1000 or max(numeri_lista) > 1000:
                 print("Hai messo uno o piu valori troppo grandi o troppo piccoli, riprova")

             else:
                 print(f"La tua lista 'ricontrollata' e sistemata é: --> {numeri_lista}")
                 print()
                
