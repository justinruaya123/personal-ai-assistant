from VAD import *
import pyaudio

def main():
    print("Starting personal assistant...")
    VAD_layer = VoiceActivationDetector("QDSbvyxt9Wg7uxOmdoa7Pi96CqjPHSek+Cxq2cTZxmuZY13MHvFVwA==")

    VAD_layer.run()
if __name__ == "__main__":
    main()