import keyboard
import shutil
import time
import os

# TODO: File Collector - Possibilità di ricollegare file all'interno di una cartella
# * Step 1: creazione cartella all'interno della directory dove si presenta il file py
# * Step 2: Ricollegare i file presenti all'interno della cartella attraverso un dictionary

class Main:

    def main(slow_tipe):
        path = os.getcwd()
        file = os.listdir(path)
        
        monologue: str = "> Benvenuto/a nella mia applicazione. Grazie a quest'ultima, potrai andare a riordinare i tuoi file presenti nel computer. Se hai capito tutto, premi: 'INVIO'"
        slow_tipe(monologue)
        keyboard.wait("ENTER")
        monologue: str = "> Perfetto, adesso inizieremo il lavoro: "
        slow_tipe(monologue)

    def slow_tipe(text: str, tmp: int):
        List_Text = [text[x: x+20] for x in range(round(len(text) / 20))]
        List_Text = [x.insert(0, "  ") for x in List_Text if List_Text.index(x) != 0]
        for words in List_Text:
            for letter in words:
                print(letter)
                time.sleep(tmp)
    
    def collection(Files, path):
        File = {
            "File Di Testo": ".txt",
            "File Musicali": [".mp3", ".ogg", ".wav"],
            "File Immagini": [".jpg", ".png", ".bmp"],
            "File Eseguibili": [".exe", ".com", ".bat"],
            "Pagine Web": [".htm", ".html", ".css", ".shtml"],
            "File Word": [".doc", ".docx"],
            "File Excel": [".xls", ".xlsx"],
            "File Pdf": ".pdf",
            "File Compressi": [".zip", ".rar"],
            "File AUTOCAD" : [".dwg", "dxf"],
            "File Libre Office Word": ".odt",
            "File Libre Office Calc": ".ods",
            "File Libre Office Impress": ". odp",
        }

        for new in File.keys():
            os.makedirs(path + new)
        for file in Files:
            extention = os.path.basename(file).split(".")[-1]
            for x in File.keys():
                if File[x] == extention
            shutil.move(path + file, path + )
