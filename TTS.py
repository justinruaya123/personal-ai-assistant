from gtts import gTTS
import playsound

class TTS:
    tts = None 

    def process(input_text, language = 'en'): #Save tts to mp3
        tts = gTTS(input_text, lang= language)
        tts.save("reply.mp3")
    # Play the mp3 file with playsound
    def speak():
        playsound.playsound("reply.mp3")
        
       

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