import speech_recognition as sr
from time import ctime
import webbrowser
from playsound import playsound
import time
import playsound
import os
from gtts import gTTS
import random

def record_audio(ask=False):
     with sr.Microphone() as source:
          if ask:
               ava_speak(ask)
          audio=r.listen(source)
          voice_data=''
          try:
               voice_data=r.recognize_google(audio)
          except sr.UnknownValueError:
               ava_speak("Sorry, I did not get that")
          except sr.RequestError:
               ava_speak('Sorry, my speech service is down')
          return voice_data

def ava_speak(audio_string):
     tts=gTTS(text=audio_string, lang='en')
     r=random.randint(1,10000000)
     audio_file="audio"+ str(r) +".mp3"
     tts.save(audio_file)
     playsound.playsound(audio_file)
     print(audio_string)
     os.remove(audio_file)

def respond(data):
     if 'what is your name' in data:
          ava_speak('My name is Ava')
     if 'what time is it' in data:
          ava_speak(ctime())
     if 'search' in data:
          search=record_audio('what do you want to search for?')
          url='https://google.com/search?q=' + search
          webbrowser.get().open(url)
          ava_speak('Here is what I found for '+ search)
     if 'find location' in data:
          location=record_audio('What is the location?')
          url='https://google.co.ke/maps/place'+ location + '/&amp;'
          webbrowser.get().open(url)
          ava_speak('Here is the location of '+ location)
     if 'goodbye' in data:
          ava_speak("Going to sleep")
          exit()

if __name__ == '__main__':
     r=sr.Recognizer()
     ava_speak('My name is Ava. How can I help you?')
     while (1):
          my_voice=record_audio()
          respond(my_voice)