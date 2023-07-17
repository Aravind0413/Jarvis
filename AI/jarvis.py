#=========================We have to install the imported modules first to start our FRIDAY ASSISTANT program==================================
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pyautogui
import wolframalpha
import random
import requests
from datetime import date, time
import speech_recognition as sr
import sys
import smtplib
from email.message import EmailMessage
import subprocess
from tkinter import *
from PIL import ImageTk, Image
#from playsound import playsound
#playsound('D:\\Jarvis.mp3')

client = wolframalpha.Client('QWWL5J-RVK5GHY5HT')

#==============from here the friday code is starting first the voice setting is done======================
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def speak(audio):
    print('JARVIS:', audio)
    engine.setProperty('voice', voices[len(voices) - 1].id)
    engine.say(audio)
    engine.runAndWait()

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Try again')
        pass

    return query
#==============here we need wishing from friday when we start it at any time=====================

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning Sir!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon Sir!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening Sir!')

def screenshot():
    img = pyautogui.screenshot()
    img.save('D:\\friday\\jarvis\\js.jpg')
#=====================frontend coded============================
class Widget:
    def __init__(self):
       root = Tk()
       root.title('JARVIS(MK-04)')
       root.config(background='Red')
       root.geometry('400x750')
       root.resizable(0, 0)
       img = ImageTk.PhotoImage(Image.open(r"D:\\friday\\jarvis.jpg"))
       panel = Label(root, image = img)
       panel.pack(side = "bottom", fill = "both", expand = "no")

       self.compText = StringVar()
       self.userText = StringVar()

       self.userText.set('Click \'Start Listening\' to Give commands')

       userFrame = LabelFrame(root, text="USER", font=('Black ops one', 10, 'bold'))
       userFrame.pack(fill="both", expand="yes")
         
       left2 = Message(userFrame, textvariable=self.userText, bg='dodgerBlue', fg='white')
       left2.config(font=("Comic Sans MS", 10, 'bold'))
       left2.pack(fill='both', expand='yes')

       compFrame = LabelFrame(root, text="JARVIS", font=('Black ops one', 10, 'bold'))
       compFrame.pack(fill="both", expand="yes")
         
       left1 = Message(compFrame, textvariable=self.compText, bg='Red',fg='white')
       left1.config(font=("Comic Sans MS", 10, 'bold'))
       left1.pack(fill='both', expand='yes')
       
       btn = Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'), bg='deepSkyBlue', fg='white', command=self.clicked).pack(fill='x', expand='no')
       btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='deepSkyBlue', fg='white', command=root.destroy).pack(fill='x', expand='no')

       
       speak('Hello, I am JARVIS! What should I do for You?')
       self.compText.set('Hello, I am friday! What should I do for You?')

       root.bind("<Return>", self.clicked) # handle the enter key event of your keyboard
       root.mainloop()
    
    def clicked(self):
        print('Working')
        query = myCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()

#==============here the are given commands to friday to run according what we need and started with web browsering=========

        if 'wikipedia' in query:
          speak("Searching wikipedia sir")
          self.compText.set('Searching wikipedia sir')
          query = query.replace("wikipedia", "")
          results = wikipedia.summary(query, sentences=2)
          speak("According to wikipedia")
          print(results)
          speak(results)
          
        elif 'open google chrome' in query:
            self.compText.set('okay sir')
            speak('okay sir')
            subprocess.call(r'C:\Program Files\Google\Chrome\Application\chrome.exe')

        elif 'open internet explorer' in query:
            self.compText.set('okay sir')
            speak('okay sir')
            subprocess.call(r"C:\Program Files\Internet Explorer\iexplore.exe")

        elif 'open youtube' in query:
            self.compText.set('okay sir')
            speak('okay sir')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            self.compText.set('okay sir')
            speak('okay sir')
            webbrowser.open('www.google.co.in')

        elif 'open hotstar' in query:
            webbrowser.open('https://www.hotstar.com/in/')
            self.compText.set('okay sir')
            speak('okay sir')
        
        elif 'open gmail' in query:
            self.compText.set('okay sir')
            speak('okay sir')
            webbrowser.open('www.gmail.com')

        elif 'open news' in query:
            self.compText.set('opening in browser sir please wait')
            speak('opening in browser sir please wait')
            webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

        elif 'who is' in query:
            self.compText.set('searching sir')
            speak('searching sir')
            webbrowser.open(query)

        elif 'weather today' in query:
            self.compText.set('searching Sir')
            speak('searching Sir')
            webbrowser.open('https://www.google.com/search?client=firefox-b-d&biw=1366&bih=654&ei=CKqgX73lKOHYz7sPlJqUoAM&q=weather+today&oq=+weather&gs_lcp=CgZwc3ktYWIQARgDMgcIABCxAxBDMgQIABBDMgQIABBDMgcIABCxAxBDMgcIABCxAxBDMgQIABBDMgcIABCxAxBDMgUIABCxAzIFCAAQsQMyAggAOgQIABBHOgkIABCxAxAHEB46BggAEAcQHlC0IFiyJ2D1P2gAcAN4AYABywKIAbQKkgEHMC4xLjIuMpgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab')

#=========================Music command other internal======================
        
        elif 'music' in query or "play songs" in query:
          self.compText.set('Okay sir, here is your music! Enjoy!')
          speak('Okay sir, here is your music! Enjoy!')
          music_dir = 'C:\\Users\Aravind\Music'
          songs = os.listdir(music_dir)
          print(songs)
          random = os.startfile(os.path.join(music_dir, songs[78]))   
        
        elif 'open media ' in query:
            speak('opening Sir')
            self.compText.set('opening Sir')
            codepath = "C:\\ProgramFiles(x86)\\Windows Media Player\\wmplayer.exe"
            os.startfile(codepath)

        elif 'open code' in query:
            speak('opening Sir')

            codepath = "C:\\Users\\Aravind\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'shutdown' in query:
            self.compText.set('okay')
            speak('okay')
            os.system('shutdown -s')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            self.compText.set(random.choice(stMsgs))
            speak(random.choice(stMsgs))


#======================Controlling the mails====================

        elif 'email' in query:
            self.compText.set('Who is the recipient? ')
            speak('Who is the recipient? ')
            recipient = myCommand()
            self.userText.set(recipient)
            recipient = recipient.lower()

            if 'me' in recipient:
                try:
                    self.compText.set('What should I say? ')
                    speak('What should I say? ')
                    content = myCommand()
                    self.userText.set(content)
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("aravindlucky413@gmail.com", 'b.facebook')
                    server.sendmail('aravindlucky413@gmail.com', "luckyaravind83@gmail.com", content)
                    server.close()
                    self.compText.set('Email sent!')
                    speak('Email sent!')

                except:
                    
                    speak('Sorry ' + 'Sir' + '!, I am unable to send your message at this moment!')


#============next this commands to talk simply with friday================

        elif 'introduce about yourself' in query:
            self.compText.set('I am Jarvis a personal virtual programed assistant where i can speak and help you to open any websites and i will follow your all commands and i am very helpful for')
            speak('I am Jarvis a personal virtual programed assistant where i can speak and help you to open any websites and i will follow your all commands and i am very helpful for')
        
       
        elif 'time' in query:
            self.compText.set("result in bg see see it sir")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir,the time is {strTime}")

        elif 'joke' in query:
            self.compText.set(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif 'today' in query:
            speak("Sir it is")
            self.compText.set(date.today())
            speak(date.today())
            speak("today")

        elif 'hello'in query:
            self.compText.set('hello welcome back sir')
            speak('hello welcome back sir')
        
        elif 'goodbye' in query:
            self.compText.set('Goddbye sir')
            playsound('D:/JARVIS Goodbye Sir.wav')
            exit()

        elif 'go offline' in query:
            self.compText.set('ok ssir shutting down the system')
            speak("ok sir shutting down the system")
            quit()
      

        elif 'temperature' in query:
            res = client.query(query)
            self.compText.set(next(res.results).text)
            speak(next(res.results).text)
        
        elif 'calculate'in query:
            speak('what should i calculate sir?')
            gh = myCommand().lower()
            res = client.query(gh)
            self.compText.set(next(res.results).text)
            speak(next(res.results).text)        
        
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            self.compText.set('Okay')
            speak('okay')
            self.compText.set('Bye sir, have a good day.')
            speak('Bye sir, have a good day.')
           
        #======================the below commands is simple operations are done==========================
        elif 'up'in query:
            pyautogui.press('up')
            self.compText.set('Okay sir')
            speak('okay sir')
                
        elif 'down' in query:
            pyautogui.press('down')
            self.compText.set('Okay sir')
            speak('okay sir')
                
        elif 'left' in query:
            self.compText.set('Okay sir')
            speak('okay sir')
            pyautogui.press('left')
                
        elif 'right' in query:
            self.compText.set('Okay sir')
            speak('okay sir')
            pyautogui.press('right')
                
        elif 'enter'in query:
            self.compText.set('Okay sir')
            speak('okay sir')
            pyautogui.press('enter')

        elif 'screenshot' in query:
            self.compText.set("i have taken a screenshot sir")
            speak('i have taken a screenshot sir')
            screenshot()       

        elif 'minimise the windows 'in query or'minimise the window'in query :
                speak("minimiseing the window sir")
                self.compText.set('minimiseing the window sir')
                pyautogui.hotkey('Win','d')

        elif 'maximize the windows'in query or'maximize the window'in query :
                speak("maximizeing windows sir")
                self.compText.set('maximizeing windows sir')
                pyautogui.hotkey('Win', 'd')

        elif 'open run' in query:
            speak('okay sirs')
            self.compText.set("okay sir")
            pyautogui.hotkey('win','r')        
        
        elif 'open pc' in query:
            speak('okay sir')
            self.compText.set("okay sir")
            pyautogui.hotkey('win','e')   
        
        elif 'close the window'in query:
            pyautogui.hotkey('ALT','F4')
            self.compText.set('okay sir')
            speak('okay sir')        
        
        elif 'new tab'in query:
                pyautogui.hotkey('ctrl','t')
                self.compText.set('Okay sir')
                speak('okay sir')

        elif 'new file'in query:
                pyautogui.hotkey('ctrl','n')
                self.compText.set('Okay sir')
                speak('okay sir')

        elif 'switch the windows'in query  or 'switch the tab'in query:
                pyautogui.hotkey('ctrl','shift','tab')
                self.compText.set('Okay sir')
                speak('okay sir')

        elif 'volume up' in query:
                speak('valume up sir')
                self.compText.set('volume up sir')
                pyautogui.hotkey('volumeup')

        elif 'i want to search' in query or 'write'in query:
    
                speak("ok sir please say what you want to write or search sir")
                s=myCommand()
                pyautogui.write(s)
                time.sleep(3)
                pyautogui.press('enter')

        
            
        else:
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    self.compText.set(results)
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    self.compText.set(results)
                    speak(results)
        
            except:
                speak('I don\'t know sir! Google is smarter than me!')
                self.compText.set('I don\'t know sir! Google is smarter than me!')
                webbrowser.open('www.google.com')
                
if __name__ == '__main__':
    greetMe()
    widget = Widget()        
