import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

zira = pyttsx3.init('sapi5')
voices = zira.getProperty('voices')
zira.setProperty('voice', voices[1].id)
#print(voices[1].id) 
'''
The voice we are using is a female voice 'Zira'
'''

def speak(audio):
    zira.say(audio)
    zira.runAndWait()
    
def greetings():
    global assname
    global uname
    assname = 'Zira'
    speak("What should I call you?")
    uname = takeCommand()
    wishMe()
    speak(f"{uname} I am your personal assistant {assname}. How may I help you")
    
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")  

def takeCommand():
    r = sr.Recognizer()
    #Recognizer class helps us to recognize audio
    with sr.Microphone() as source:
        '''
        In this snippet we are saying that the physical microphone of our system should be taken as source for detecting audio
        '''
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)   
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said {query}\n")
    except Exception as e:
        print(e)
        print("I did not understand can you repeat please...")
        return "None"
    return query
  
def sendEmail(to, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('kpsrushti68@gmail.com', 's.rushtiii@6')
        server.sendmail('kpsrushti68@gmail.com', to, body)
        server.quit()   
        return True
    except smtplib.SMTPAuthenticationError as e:
        print("SMTP Authentication Error:", e)
        return False
    except Exception as e:
        print("An err occured" , e)
        return False
      
if __name__ == '__main__':
    greetings()
    while True:
        query = takeCommand().lower()
        
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')
              
        elif 'open amazon' in query:
            webbrowser.open('https://www.amazon.in/')
            
        elif 'open google' in query:
            webbrowser.open('https://www.google.com/')
            
        elif 'open bootstrap' in query:
            webbrowser.open('https://getbootstrap.com/')
            
        elif 'open w3schools' in query:
            webbrowser.open('https://www.w3schools.com/')
        
        elif 'play music' in query:
            music_dir = 'C:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"the Time is : {strTime}")
        
        elif 'day' in query:
            day = datetime.datetime.today().weekday() + 1
            Day_Dict = {
                1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday', 7: 'Sunday'
            }
            if day in Day_Dict:
                print(Day_Dict[day])
                speak(f"Today is {Day_Dict[day]}")
        
        elif 'year' in query:
            Year = datetime.datetime.now().year
            print(Year)
            speak(f"We are in {Year}")
        
        elif 'open code' in query:
            codepath = "C:\\Users\\msi18\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
        elif 'send email' in query:
            #This snippet will show problem because the settings in google for less secure hasent been done
            speak("Whom do you want to send mail?")
            recipient = takeCommand()
            email_dict = {
                'myself' : 'kpsrushti68@gmail.com',
                'college' : '21512854.dypit@dypvp.edu.in'
            }
            if recipient in email_dict:
                try:
                    speak("What do you want to mail")
                    body = takeCommand()
                    to = email_dict[recipient]
                    sendEmail(to, body)
                    if sendEmail(to, body):
                        speak("Email has been sent!")
                    else:
                        speak("Sorry, I couldn't send the email.")
                except Exception as e:
                    print("An error occurred:", e)
                    speak("Sorry, I encountered a problem and couldn't send the email.")
        #elif 'thank you' or 'thanks' or 'thank' in query:
         #   speak(f"I am glad to help you.It was nice interacting with you. For now bye {uname}")
            