print("Inserisci due numeri, ti diremo poi dopo la loro somma: ")
Bit_1 = int(input("> "), base = 2)
Bit_2 = int(input("> "), base = 2)

AddBinary = lambda x, y: x + y
BinaryTot = AddBinary(Bit_1, Bit_2)

print(BinaryTot)
Resault = ""

while BinaryTot >= 1:
    if BinaryTot % 2 == 0: Resault += "0"
    else: Resault += "1"

    BinaryTot //= 2
    print(BinaryTot)

print(Resault[::-1])
