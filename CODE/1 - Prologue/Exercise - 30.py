def perfect_number(num):
    divisori = []
    divisore = 2
    copy_num = num

    if num == 1:
        print("Il tuo numero è perfetto")
    else:
        while num != divisore:
            if num % divisore == 0:
                divisori.append(divisore)
                divisore += 1
            else:
                divisore += 1
        if sum(divisori, 1) == copy_num:
            print("Il tuo numero è perfetto!")
        else:
            print("Il tuo numero non è perfetto...") 
    return divisori

while True:
    numero = int(input("Dimmi un numero per vedere se è perfetto! "))
    perfect_number(numero)
            
