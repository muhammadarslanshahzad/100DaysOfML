import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning !")
    elif hour >=12 and  hour <15:
        speak("Good Noon !")
    elif hour >=15 and hour < 17:
        speak("Good After Noon! ")
    elif hour >=17 and hour <19:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("I am ELSA Sir, How may I Help You?")

def takeCommand():
    '''it takes commands from the user'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please.....")
        return "None"
    return query
if __name__ == "__main__":
    wishME()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipeadia ...")
            query= query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences =2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'open github' in query:
            webbrowser.open('github.com')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\masmb\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'goodbye' in query:
            exit()
