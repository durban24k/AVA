from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
     print(audio)
     tts=gTTS(text=audio, lang='en')
     tts