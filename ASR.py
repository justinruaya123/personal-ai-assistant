#import nemo
#import nemo.collections.asr as nemo_asr #This won't import!!
import wave

import speech_recognition as sr


# https://pythonbasics.org/transcribe-audio/
# https://stackoverflow.com/questions/71094025/import-speech-recognition-could-not-be-resolved
# https://catalog.ngc.nvidia.com/orgs/nvidia/models/nemospeechmodels

class AutomaticSpeechRecognition:
    # model = None
    # def __init(self):
    #     self.model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-crdnn-rnnlm-librispeech", savedir="pretrained_models/asr-crdnn-rnnlm-librispeech") #This returns nonetype :(
    # def run(self, audio_file):
    #     return self.model.transcribe_file('models/example.wav') #nonetype raw kahit nandoon naman file..
    # recognizer = None 
    def __init__(self):
        self.recognizer = sr.Recognizer()
    def run(self, filename):
        with sr.AudioFile(filename) as source:
            audio_data = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio_data)
            return text

# class AutomaticSpeechRecognition:
#     model = None

#     def __init__(self, device):
#         super().__init__()
#         self.model = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="QuartzNet15x5Base-En").cuda()
#         self.device = device
#         return None



#     def run(self, audio_file): #hanapin ko file neto 
#         file = wave.open(audio_file, "rb")
#         text = self.model.transcribe(paths2audio_files=[audio_file])
#         #output = punctuation.add_punctuation_capitalization(queries=text)
#         return text



## link: https://huggingface.co/docs/transformers/model_doc/speech_to_text if magpapalit




#        import torch
#        from transformers import Speech2TextProcessor, Speech2TextForConditionalGeneration
#        from datasets import load_dataset

#        model = Speech2TextForConditionalGeneration.from_pretrained("facebook/s2t-small-librispeech-asr")
#        processor = Speech2TextProcessor.from_pretrained("facebook/s2t-small-librispeech-asr")


#        ds = load_dataset("hf-internal-testing/librispeech_asr_demo", "clean", split="validation")

#        inputs = processor(ds[0]["audio"]["array"], sampling_rate=ds[0]["audio"]["sampling_rate"], return_tensors="pt")
#        generated_ids = model.generate(inputs["input_features"], attention_mask=inputs["attention_mask"])

#        transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)
#        transcription
#        ['mister quilter is the apostle of the middle classes and we are glad to welcome his gospel']


## wait lang huhu
#from transformers import Speech2TextConfig, Speech2TextModel

# Initializing a Speech2Text s2t_transformer_s style configuration
#configuration = Speech2TextConfig()

# Initializing a model (with random weights) from the s2t_transformer_s style configuration
#model = Speech2TextModel(configuration)

# Accessing the model configuration
#configuration = model.config


