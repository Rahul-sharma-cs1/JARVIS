import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
# download pyaudio module
# download openai module

api_key = "59d2d299834a40d0910c33d612b899b5"
# begin

sr.AudioFile.FLAC_CONVERTER = "/opt/homebrew/bin/flac"

recognizer = sr.Recognizer()
engine = pyttsx3.init() 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if  "open google" in c.lower():
        webbrowser.open("https://google.com") 
    elif  "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif  "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif  "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "", 1).strip()
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])[:5]
            speak("top 5 news of today") 
            for article in articles:
                print(article["title"])
                speak(article["title"])
            if not articles:
                speak("Sorry, I couldn't find any news at the moment.")

    else:
        #let open ai handle the request
        pass



if(__name__ == "__main__"):
    speak("initialising jarvis...")
    #listen for the wake word jarvis
    # obtain audio from the microphone
    while True:
        r = sr.Recognizer() 
        
        # recognize speech using google
        try:
            with sr.Microphone() as source: 
                print("Listening...")
                audio = r.listen(source,timeout=1,phrase_time_limit=1)
            print("recognizing...")
            word = r.recognize_google(audio) 
            if(word.lower() == "jarvis"):
                speak("Yes sir")
            #listen for command
            with sr.Microphone() as source:
                print("Jarvis active...")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                processCommand(command)
                
        except Exception as e:
            print("error; {0}".format(e)) 
