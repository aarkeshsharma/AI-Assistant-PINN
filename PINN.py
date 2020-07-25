import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today's date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour<15:
        speak("Good afternoon Sir!")
    elif hour >= 15 and hour<19:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("This is PINN at your service, How can I help You Sir??")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        speak("Anything else Sir?")
        return "None"
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\dharm\\Desktop\\AI Assistant\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('Cpu usage is'+ usage)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
            
        elif 'search in chrome' in query:
            speak("What should i search sir?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
        elif 'play songs' in query:
            songs_dir = 'D:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak("What should i remember sir??")
            data = takeCommand()
            speak("You told to remember"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'do you remember what i told you before' in query:
            remember =open('data.txt', 'r')
            speak("Yes Sir, You told me that..."+remember.read())
        
        elif 'take screenshot' in query:
            screenshot()
            speak("Done Sir!")
        
        elif 'cpu' in query:
            cpu()

        elif 'jokes' in query:
            jokes()

        elif 'offline' in query:
            speak("Ok Sir")
            quit()



