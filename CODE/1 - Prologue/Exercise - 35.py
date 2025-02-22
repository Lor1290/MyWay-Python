class Test:
    def Len(self, String):
        
        self.String = String
        contatore = 0

        for i in self.String:
            contatore += 1
        
        print(f"La Lunghezza di '{self.String}' é: {contatore}")

Parola = Test()

while True:

    scelta = input("Dimmi una parola e io ti diro la sua lunghezza: ")
    Parola.Len(scelta)
