import speech_recognition as sr

def Audio_Recorder():

    V_Recorder = sr.Recognizer()
    V_Recorder_List = []
    cicle = "Exit"
    text = ""

    while cicle != text:
        
        with sr.Microphone() as source:
            V_Recorder.adjust_for_ambient_noise(source)
            V_Recorder.pause_trashold = 5.0
            print(">>> Listening")
            audio = V_Recorder.listen(source)

            try:
                text = V_Recorder.recognize_google(audio, language="it-IT")
                V_Recorder_List.append(text)
                print(">>> " + text)
            except Exception as e:
                print(e)

Audio_Recorder()
print(V_Recorder_List)
