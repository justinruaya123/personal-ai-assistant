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

#Returns true if wave file successfully overwritten
def RUN_VAD(key, audio_device_index):
    handle = pvcobra.create(access_key = key)
    recorder = PvRecorder(device_index=audio_device_index, frame_length=512)   
    recorder.start()

    #Start wave file

    #For timeout logic
    since_recognized = int(round(time.time() * 1000))
    write = False
    ran_write = False

    while True:
        pcm = recorder.read()
        voice_probability = handle.process(pcm) 
        #Output
        percentage = voice_probability * 100
        bar_length = int((percentage / 10) * 3)
        empty_length = 30 - bar_length
        sys.stdout.write("\r[%3d]|%s%s|: %s" % (
            percentage, '█' * bar_length, ' ' * empty_length, "I hear you! Speak your request. " if voice_probability>0.5 else "I can't hear you for now. "))

        if voice_probability > 0.5:
            since_recognized = getTimeInMS()
            write = True 
        else:
            if (getTimeInMS() - since_recognized) >= audio_timeout:
                recorder.stop()
                handle.delete()
                break
        if write and not ran_write:
            wav_file = wave.open("voice.wav", "w")
            wav_file.setparams((1, 2, 16000, 512, "NONE", "NONE"))  
            ran_write = True
        if write:
            wav_file.writeframes(struct.pack("h" * len(pcm), *pcm))
    if ran_write:
        wav_file.close()

    sys.stdout.write("")
    sys.stdout.flush()
    return ran_write