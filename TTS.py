from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
import wave
import os
import playsound
#import time


#input_text = 'I want to cry!' #trial input pero change to output ng ASR kapag meron na
#language = 'en'

class TTS:
    tts = None 

    def process(input_text, language): #Save tts to mp3
        tts = gTTS(input_text, lang= language)
        tts.save("response.mp3")
    # Play the mp3 file with playsound
    def speak():
        playsound.playsound("response.mp3")




                                                        
    



#playsound.playsound(filename)
#os.remove(filename)

# sound = speak()
# sound.seek(0)
# mixer.music.load(sound, "mp3")
# mixer.music.play()
# time.sleep(5)


#from os import path
#from pydub import AudioSegment

# files                                                                         
#src = "transcript.mp3"
#dst = "test.wav"

# convert wav to mp3                                                            
#sound = AudioSegment.from_mp3(src)
#sound.export(dst, format="wav")