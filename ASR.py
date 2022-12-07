import nemo
import nemo.collections.asr as nemo_asr
from threading import Thread

# https://pythonbasics.org/transcribe-audio/
# https://stackoverflow.com/questions/71094025/import-speech-recognition-could-not-be-resolved
# https://catalog.ngc.nvidia.com/orgs/nvidia/models/nemospeechmodels



class AutomaticSpeechRecognition(Thread):
    model = None

    def __init__(self, device):
        super().__init__()
        self.model = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="QuartzNet15x5Base-En")
        self.device = device
        return None

# after feeding the wave file    
# transcribe audio file                                                         
# Audio = "transcript.wav"


    def run(self, audio_file): #hanapin ko file neto 
        quartznet = self.model.to(device)
        text = quartznet.transcribe(paths2audio_files=[audio_file])
        output = punctuation.add_punctuation_capitalization(queries=text)
        return output

