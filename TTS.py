import nemo
import nemo.collections.tts as nemo_tts

class TextToSpeech:
    language = 'en'
    spectrogram_generator = nemo_tts.models.FastPitchModel.from_pretrained(model_name="tts_en_fastpitch").cuda()
    vocoder = nemo_tts.models.HifiGanModel.from_pretrained(model_name="tts_hifigan").cuda()

    def __init__(self):
        #Initialize the TTS module here

        return
    
    def Speak(text):
        print(text)
        #Logic for speaking here
    
    def text_to_audio(text):
        parsed = spectrogram_generator.parse(text)
        spectrogram = spectrogram_generator.generate_spectrogram(tokens=parsed)
        audio = vocoder.convert_spectrogram_to_audio(spec=spectrogram)
        return audio.to('cpu').numpy()
    audio = text_to_audio(english_text[0])


#Driver code, will be ran at asssistant.py
tts = TextToSpeech()
tts.Speak("Hi there")