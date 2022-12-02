

# https://pythonbasics.org/transcribe-audio/
# https://stackoverflow.com/questions/71094025/import-speech-recognition-could-not-be-resolved

class AutomaticSpeechRecognition(Thread):
    def __init__(self, model, tokenizer, device):
        return


# after feeding the wave file    
# transcribe audio file                                                         
# Audio = "transcript.wav"

# use the audio file as the audio source                                        
# r = sr.Recognizer()
# with sr.AudioFile(Audio) as source:
#         sound = r.record(source)  # read the entire audio file                  

#         print("Transcription: " + r.recognize_google(sound))