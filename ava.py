import speech_recognition as sr
from time import ctime
import webbrowser

r=sr.Recognizer()

def record_audio(ask=False):
     with sr.Microphone() as source:
          if ask:
               print(ask)
               audio=r.listen(source)
               voice_data=''
          try:
               voice_data=r.recognize_google(audio)
          except sr.UnknownValueError:
               print("Sorry, I did not get that")
          except sr.RequestError:
               print('Sorry, my speech service is down')
          return voice_data

def respond(data):
     if 'what is your name' in data:
          print('My name is Googles')
     if 'what time is it' in data:
          print(ctime())
     if 'search' in voice_data:
          search=record_audio('what do you want to search for')
          url='https://www.google.com?q='+search
          webbrowser.get().open(url)
          print('Here is what I found for '+ search)


print('How can I help you?')
voice_data=record_audio()
respond(voice_data)