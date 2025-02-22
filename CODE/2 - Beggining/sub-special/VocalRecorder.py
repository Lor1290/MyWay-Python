import speech_recognition as sr

def Audio_Recorder(timer):

    V_Recorder = sr.Recognizer()
    V_Recorder_List = []
    cicle = "exit"
    text = ""

    while cicle != text.lower():
        
        with sr.Microphone() as source:
            V_Recorder.adjust_for_ambient_noise(source)
            V_Recorder.pause_trashold = timer
            print(">>> Listening")
            audio = V_Recorder.listen(source)

            try:
                text = V_Recorder.recognize_google(audio, language="it-IT")
                V_Recorder_List.append(text)
                for i in text:
                    if i.lower() == "virgola":
                        text.replace(i, ",")
                    if i.lower() == "punto":
                        text.replace(i, ".")
                    if i.lower() == "punto e virgola":
                        text.replace(i, ";")
                    if i.lower() == "aperta tonda":
                        text.replace(i, "(")
                    if i.lower() == "chiusa tonda":
                        text.replace(i, ")")
                    if i.lower() =="aperta quadra":
                        text.replace(i, "[")
                    if i.lower() == "chiusa quadra":
                        text.replace(i, "]")
                    if i.lower() == "aperta graffa":
                        text.replace(i, "{")
                    if i.lower() =="chiusa graffa":
                        text.replace(i, "}")
                    if i.lower() == "slash":
                        text.replace(i, "/")
                    if i.lower() == "percento":
                        text.replace(i, "%")
                    if i.lower() =="and":
                        text.replace(i, "&&")
                    if i.lower() == "or":
                        text.replace(i, "||")
                    if i.lower() == "not":
                        text.replace(i, "!")
                    if i.lower() == "uguale":
                        text.replace(i, "=")

            except Exception as e:
                print(e)

    print(">", end = " ")
    print(V_Recorder_List)

cicle_1 = True
cicle_2 = True

print()
print("Welcome to the app were you can record your own voice")
print("Now...")

while cicle_1:

    try:        
        print()
        time = int(input(">>> Digit how much time you want for each pause in your phrase: "))
        cicle_1 = False
    except ValueError:
        print("Invalid data, retry")
        continue

    print()
    print("Remember:")
    print("        - To Leave, wai the new cicle and say 'Exit'")
    print("        - For the simbol, just say it by their name")
    print()
                
    Audio_Recorder(time)

    while cicle_2:

        print()
        decision = input("Want to continue? (y/n) ")

        if decision.lower() == "y":
            cicle_2 = False
        elif decision.lower() == "n":
            cicle_2 = False
            cicle_1 = False
        else:
            print("Invalid data, retry")
    
