print("Benvenuto nel programma chhe ti permette di capire quali sono gli elementi presenti dentro una tua parola messa in input!")
print()
parola = input("Dimmi questa parola: ")
lettere = 0
numeri = 0
altri_caratteri = 0
for i in parola:
    if i in "abcdefghijklmnopqrstuvx":
        lettere += 1
    elif i in "1234567890":
        numeri += 1
    else:
        altri_caratteri += 1
print(f"La tua parola: Lungezza -> {len(parola)}, lettere -> {lettere}, numeri -> {numeri}, altri caratteri -> {altri_caratteri}")
