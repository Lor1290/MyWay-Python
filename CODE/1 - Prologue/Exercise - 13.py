import string
import random
print("benvenuto nel tuo generatore di password fatto da: Poli! Grazie a me potrai creare delle pasword nuove, semplici o complesse, da utilizzare, prima di partire, però, dimmi: ")
a = input("che tipo dipassword vuoi avere? semplice o complessa? (scrivi una delle due) ")
password2 = "5[/|ù§^çò@#°àabcdeuyewwiudwiucuhe1289294878"
if a == "semplice":
    n = int(input("quante password ti servono nuove ? "))
    print("ecco le tue password! ")
    for i in range (n):
        print("".join(random.choice(string.ascii_letters + string.digits) for i in range (8)))
if a == "complessa":
    n = int(input("quante password ti servono nuove? "))
    print("ecco le tue password! ")
    for i in range (n):
        print("".join(random.choice(password2) for i in range (20)))
print("arrivederci!")
            
        
        
    
