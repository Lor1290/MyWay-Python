from math import sqrt
print("Benvenuto nel programma che ti permette di calcolare l'ipotenusa di un trangolo rettangolo")
C,s,c = input("Inserisci i valori dei cateti: ")
C = int(C)
c = int(c)
ipotenusa = sqrt(C*C + c*c)
print(ipotenusa)


