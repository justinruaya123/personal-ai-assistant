from gtts import gTTS
import os

class TextToSpeech:
    language = 'en'

    def __init__(self):
        #Initialize the TTS module here

        return
    
    def Speak(text):
        print(text)
        #Logic for speaking here



#Driver code, will be ran at asssistant.py
tts = TextToSpeech()
tts.Speak("Hi there")