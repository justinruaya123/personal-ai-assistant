from VAD import *
from ASR import * 
from TTS import *
from LLM import *
from pvrecorder import PvRecorder
from pynput import keyboard
from pynput.keyboard import Key, KeyCode, Listener

enabled = True

def main():
    print("Press 'Q' to stop the assistant.")
    devices = PvRecorder.get_audio_devices()
    for i in range(len(devices)):
        print("Device %d: %s" % (i, devices[i]))
    audio_device_index = int(input("Select audio device ID: "))
    response_key = input("Do you have an OpenAI key? [Y/N] > ")
    if(response_key[0]== "y" or response_key[0]== "Y"):
        LLM.setKey(input("Enter key here > "))
    count = 0

    while enabled:
        if not RUN_VAD("QDSbvyxt9Wg7uxOmdoa7Pi96CqjPHSek+Cxq2cTZxmuZY13MHvFVwA==", audio_device_index):
            continue
        text = AutomaticSpeechRecognition().run("voice.wav")
        print(count, "You said:", text)
        response = generate(text)
        print(count, "[uWu Machine]:", response)
        TTS.process(response, 'en')
        TTS.speak()
        print("=====================================")
        count+=1

def on_press(key):
    if key == keyboard.KeyCode.from_char('q'):
        print("\n[uWu Machine]: Bye-bye!...")
        enabled = False
        sys.exit(0)


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    main()