import pvcobra
from pvrecorder import PvRecorder

import pyaudio
import wave
import struct
import time
import sys
audio_timeout = 1000 #Timeout in miliseconds

def getTimeInMS():
    return int(round(time.time() * 1000))


def run(key, audio_device_index):
    handle = pvcobra.create(access_key = key)
    recorder = PvRecorder(device_index=audio_device_index, frame_length=512)   
    print("Listening...")
    recorder.start()
    
    #Start wave file
    wav_file = wave.open("voice.wav", "w")
    wav_file.setparams((1, 2, 16000, 512, "NONE", "NONE"))  
    #For timeout logic
    since_recognized = int(round(time.time() * 1000))
    
    while True:
        pcm = recorder.read()
        voice_probability = handle.process(pcm) 
        #Output
        percentage = voice_probability * 100
        bar_length = int((percentage / 10) * 3)
        empty_length = 30 - bar_length
        sys.stdout.write("\r[%3d]|%s%s|: %s" % (
            percentage, '█' * bar_length, ' ' * empty_length, "I hear you! Speak your request. " if voice_probability>0.5 else "I can't hear you for now. "))
        sys.stdout.flush()
        wav_file.writeframes(struct.pack("h" * len(pcm), *pcm))
        if voice_probability > 0.5:
            since_recognized = getTimeInMS()
            continue
        if (getTimeInMS() - since_recognized) >= audio_timeout:
            recorder.stop()
            break
    wav_file.close()
    handle.delete()
        

    
    