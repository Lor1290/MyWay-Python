prezzo_giornaliero = 30
P =(prezzo_giornaliero)
Giorni = float(input("da quanti giorni hai nolleggiato la auto?"))
G = (Giorni)
if (G > 6):
    Pt = (P * G)
    Ps = float((Pt * 10)/100)
    ans = (Pt - Ps)
    print("il prezzo che dovrai pagare è di: " + str(ans))
else:
    ans = (P * G)
    print("il prezzo che dovrai pagare è di: " + str(ans))
