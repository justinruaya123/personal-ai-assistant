from VAD import *
import pyaudio
from pvrecorder import PvRecorder

def main():
    print("Starting personal assistant...")
    devices = PvRecorder.get_audio_devices()
    for i in range(len(devices)):
        print("Device %d: %s" % (i, devices[i]))
    audio_device_index = int(input("Select audio device ID: "))

    while True:
        run("QDSbvyxt9Wg7uxOmdoa7Pi96CqjPHSek+Cxq2cTZxmuZY13MHvFVwA==", audio_device_index)
        print("\nVoice recorded: voice.wav")
        break


if __name__ == "__main__":
    main()