from VAD import *
import pyaudio

def main():
    print("Starting personal assistant...")
    VAD_layer = VoiceActivationDetector("QDSbvyxt9Wg7uxOmdoa7Pi96CqjPHSek+Cxq2cTZxmuZY13MHvFVwA==")
    while True:
        VAD_layer.run() # FIXME - [WARN] Overflow - reader is not reading fast enough; this happens if PROBABILITY < 0.5
        print("Voice recorded: voice.wav")

if __name__ == "__main__":
    main()