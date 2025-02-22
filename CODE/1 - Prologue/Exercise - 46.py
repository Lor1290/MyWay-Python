import re

class Exercise:
    def Ex_1() -> int:
        print("[s] Inserisci un numero positivo")

        cicle: bool = True
        while(cicle):
            num = input(">>> ").trip()
            if not re.match("[0-9]+", num):
                print("[!] inserisci un numero valido")
                continue
            
            cicle = False
        
        Num: int = int(num)
        count: int = 0

        for x in range(1, Num+2):
            count += x
            if(count + (x+1) >= Num):
                return x;
            count += x
        return 0

res_1: int = Exercise.Ex_1()
print(f"[+] Il numero di occorrenze è: {res_1}")