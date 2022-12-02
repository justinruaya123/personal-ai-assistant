import pvcobra
from pvrecorder import PvRecorder

import pyaudio
import wave
import struct
import time
import sys

class VoiceActivationDetector:
    handle = None
    audio_device_index = None
    audio_timeout = 1000 #Timeout in miliseconds
    def __init__(self, key):
        self.handle = pvcobra.create(access_key = key)
        self.running = False
        devices = PvRecorder.get_audio_devices()
        for i in range(len(devices)):
            print("Device %d: %s" % (i, devices[i]))
        self.audio_device_index = int(input("Select audio device ID: "))

    def getTimeInMS(self):
        return int(round(time.time() * 1000))

    def run(self):
        print("Listening...")
        recorder = PvRecorder(device_index=self.audio_device_index, frame_length=512)
        recorder.start()
        #Start wave file
        wav_file = wave.open("voice.wav", "w")
        wav_file.setparams((1, 2, 16000, 512, "NONE", "NONE"))       
        #For timeout logic
        write_file = False
        since_recognized = int(round(time.time() * 1000))
        
        while True:
            pcm = recorder.read()
            voice_probability = self.handle.process(pcm) 
            #Output
            percentage = voice_probability * 100
            bar_length = int((percentage / 10) * 3)
            empty_length = 30 - bar_length
            sys.stdout.write("Voice Probability: \r[%3d]|%s%s|" % (
                percentage, '█' * bar_length, ' ' * empty_length))
            sys.stdout.flush()
            if voice_probability > 0.5:
                write_file = True
                since_recognized = self.getTimeInMS()
            else:
                if (self.getTimeInMS() - since_recognized) >= self.audio_timeout:
                    write_file = False
                    break
            if write_file:
                wav_file.writeframes(struct.pack("h" * len(pcm), *pcm))

    
    