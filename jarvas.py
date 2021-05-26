import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
import smtplib
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
volume = engine.getProperty('volume')
engine.setProperty('voice',voices[1].id)
engine. setProperty("rate", 138)
engine. setProperty("volume", 5098)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    '''
    Wishes user according to the present time
    '''
    hour = (datetime.datetime.now().hour)
    if hour<=0 and hour<11:
        speak("Good Morning")
    elif hour<=11 and hour<15:   
        speak("Good Afternoon")
    elif hour<=15 and hour<=18:  
        speak("Good Evening")    
    else:  
        speak("Hello sir") 
    speak("I am computer, how may I help you")

def takecommand():
    ''' 
    Listens what user says
    and also excepts command if not understood saying- "say that again"
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("lisening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recogniging......")  
        query = r.recognize_google(audio, language='en-in')  
        print(f"user said: {query}\n")

    except Exception as e:
        print('Say that again please......')
        return "None"

    return query    

def sendEmail(to,content):
    '''
    Functon to send email 
    '''
    servar = smtplib.SMTP('smtp.gmail.com',587)
    # servar.source_address('gmail.com')
    servar.ehlo()
    servar.starttls()
    print("ok")
    speak("ok")
    servar.login("saha93942@gmail.com", 'Saha@987654321')
    servar.sendmail('saha93942@gmail.com',to,content)
    servar.close()

if __name__ == '__main__':
    wish()
    while(True):
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching query......')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")    
        elif 'on youtube' in query:
            q1 = query.split('search')
            q2 = q1[1].split('on')
            q3 = q2[0]
            webbrowser.open(f"https://www.youtube.com/results?search_query={q3}")   
        elif 'search on google' in query:
            speak("What do yo wanna search: ")
            q = takecommand()
            webbrowser.open(f"https://www.google.com/search?q={q}&oq={q}&aqs=chrome..69i57j46i131i433j46i433j46i131i433l2j0i131i433j46i433j0i433j46i433j0i271.908j0j15&sourceid=chrome&ie=UTF-8")   
        elif 'open google' in query:
            webbrowser.open("google.com")    
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")    
        elif 'play music' in query:
            dirc = 'E:\\software'
            songs = os.listdir(dirc)
            print(songs)
            i = random.randint(0,4);
            os.startfile(os.path.join(dirc,songs[i]))
        elif 'what time' in query:
            nowtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is, {nowtime}")     
        elif 'exit' in query:
            sys.exit(0)
        elif 'open code' in query:
            dir2 = '"F:\\code 2021\\web development\\Microsoft VS Code\\Code.exe"'
            os.startfile(dir2)
        elif 'send email to' in query:
            try:
                speak("What should I say......")
                content = takecommand()
                to = "gouravkali123098@gmail.com"
                sendEmail(to , content)
                speak("Email Sent.")
            except Exception as e:
                speak("Sorry cannot send email!")    
        else:
            speak('Say that again please......')    