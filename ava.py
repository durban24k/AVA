from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
     print(audio)
     tts=gTTS(text=audio, lang='en')
     tts.save('audio.mp3')
     os.system('mpg123 audio.mp3')

# listening commands
def myCommand():
     r=sr.Recognizer()
     with sr.Microphone() as source:
          print('Hello, I am Ava. What can I do for you?')
          r.pause_threshold=1
          r.adjust_for_ambient_noise(source, duration=1)
          audio=r.listener(source)
     try:
          command=r.recognize_google(audio)
          print('You said: '+ command + '/n')
     # loop to listen for new instructions
     except sr.UnknownValueError:
          assistant(myCommand())
     return command

def assistant(command):
     if "open barbara's instagram" in command:
          chrome_path='C:\Program Files\Google\Chrome\Application\chrome.exe'
          url='https://www.instagram.com/_thedroppedcroissant_/'
          webbrowser.get(chrome_path).open(url)
     if 'whats\'s up' in command:
          talkToMe('Just taking it easy myself')

talkToMe('I am ready to assist you')

while True:
     assistant(myCommand())