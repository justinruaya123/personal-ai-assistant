import pvcobra
from pvrecorder import PvRecorder
from threading import Thread

import pyaudio

class VoiceActivationDetector(Thread):
    handle = None
    running = False
    output_path = None
    audio_device_index = None
    def __init__(self, key):
        self.handle = pvcobra.create(access_key = key)
        self.running = False

        devices = PvRecorder.get_audio_devices()

    
        for i in range(len(devices)):
            print("Device %d: %s" % (i, devices[i]))
        self.audio_device_index = int(input("Select audio device ID: "))
    
    # https://pypi.org/project/pvcobra/
    
    def run(self):
        self.running = True
        self.handleVAD()
    

    def stop(self):
        self.running = False
        print("Stopping VAD")
        self.handle.delete()


    # Outputs the file, threaded
    def handleVAD(self):
        print("Listening...")
        recorder = PvRecorder(device_index=self.audio_device_index, frame_length=512)
        recorder.start()
        while self.running:
            pcm = recorder.read()
            voice_probability = self.handle.process(pcm) 
            if voice_probability > 0.5:
                print("Voice detected", voice_probability) #Executes multiple times

        

