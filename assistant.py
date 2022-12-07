from VAD import *
from pvrecorder import PvRecorder
import keyboard



def main():
    print("Press 'Q' to stop the assistant.")
    devices = PvRecorder.get_audio_devices()
    for i in range(len(devices)):
        print("Device %d: %s" % (i, devices[i]))
    audio_device_index = int(input("Select audio device ID: "))

    while True:
        if not RUN_VAD("QDSbvyxt9Wg7uxOmdoa7Pi96CqjPHSek+Cxq2cTZxmuZY13MHvFVwA==", audio_device_index):
            continue

        print("\nVoice recorded: voice.wav")


if __name__ == "__main__":
    main()