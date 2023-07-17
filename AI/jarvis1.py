import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyautogui
import wolframalpha
import random
import requests
from datetime import date, time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
  engine.say(audio)
  engine.runAndWait()
  
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("This is your jarvis. how may I help you sir")
    

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r. pause_threshold = 1
        audio =r.listen(source)

    try:
        print("understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("sir say that again please...")
        return "None"
    return query

app = wolframalpha.Client("QWWL5J-RVK5GHY5HT")

if __name__ == "__main__":
    WishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('opening sir')
            webbrowser.open("https:\\www.youtube.com")

        elif 'open google' in query:
            speak('opening sir')
            webbrowser.open("https:\\www.google.com")

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'who is' in query:
                webbrowser.open(query)

        elif 'music' in query or "play song" in query:
                speak("Here you go with music")
                music_dir = 'C:\\Users\Aravind\Music'
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[1]))   
        
        elif 'open media ' in query:
            speak('opening sir')
            codepath = "C:\\ProgramFiles(x86)\\Windows Media Player\\wmplayer.exe"
            os.startfile(codepath)
             
        elif 'open code' in query:
            speak('opening sir')
            codepath = "C:\\Users\\Aravind\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'introduce about yourself' in query:
            speak('I am jarvis a personal assistant where i can speak and help you to open any websites and i will follow your all commands sir')
        
        elif 'weather today' in query:
            speak('searchind sir')
            webbrowser.open('https://www.google.com/search?client=firefox-b-d&biw=1366&bih=654&ei=CKqgX73lKOHYz7sPlJqUoAM&q=weather+today&oq=+weather&gs_lcp=CgZwc3ktYWIQARgDMgcIABCxAxBDMgQIABBDMgQIABBDMgcIABCxAxBDMgcIABCxAxBDMgQIABBDMgcIABCxAxBDMgUIABCxAzIFCAAQsQMyAggAOgQIABBHOgkIABCxAxAHEB46BggAEAcQHlC0IFiyJ2D1P2gAcAN4AYABywKIAbQKkgEHMC4xLjIuMpgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir,the time is {strTime}")

        elif 'today' in query:
                speak("It is")
                speak(date.today())
                speak("today")

        elif 'hello'in query:
            speak('hello welcome back sir')
        
        elif 'goodbye' in query:
            speak('Goodbye boss')
            exit()

        elif 'go offline' in query:
            speak("ok sir shutting down the system")
            quit()
      

        elif 'temperature' in query:
            rs = app.query(query)
            speak(next(rs.results).text)

        elif 'up'in query:
                pyautogui.press('up')
                
        elif 'down' in query:
                pyautogui.press('down')
                
        elif 'left' in query:
                pyautogui.press('left')
                
        elif 'right' in query:
                pyautogui.press('right')
                
        elif 'enter'in query:
                pyautogui.press('enter')

        elif 'shutdown' in query or 'sleep my' in query:
                speak(f"souting down")
                os.system("shutdown /h")

        elif "restart" in query:
                os.system('shutdown /r')

        elif 'minimise the windows 'in query or'minimise the window'in query :
                speak("minimize the window")
                pyautogui.hotkey('Win','d')

        elif 'maximize the windows'in query or'maximize the window'in query :

                speak("maximizeing windows")
                pyautogui.hotkey('Win', 'd')

        elif 'new tab'in query:
                pyautogui.hotkey('ctrl','t')

        elif 'new file'in query:
                pyautogui.hotkey('ctrl','n')

        elif 'switch the windows'in query  or 'switch the tab'in query:
                pyautogui.hotkey('ctrl','shift','tab')

        elif 'volume up' in query:
                speak('valume up sir')
                pyautogui.hotkey('volumeup')

        elif 'i want to search' in query or 'write'in query:
    
                speak("ok sir please say what you want to write or search sir")
                s=takecommand()
                pyautogui.write(s)
                time.sleep(3)
                pyautogui.press('enter')

        elif 'next song' in query:
             music_dir = 'C:\\Users\Aravind\Music'
             songs = os.listdir(music_dir)
             print(songs)
             random = os.startfile(os.path.join(music_dir, songs[4]))   


        elif 'open chrome' in query:
                    speak("opening broswer sir")
                    p = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                    os.startfile(p)