import pvcobra


class VAD:
    handle = None
    running = False
    def __init__(key, self):
        self.handle = pvcobra.create(access_key = key)
    def run(self):
        running = True
    
    def stop(self):
        running = False

    def handleVAD(self):
        while running:
            voice_probability = handle.process(get_next_audio_frame())
        
    def get_next_audio_frame(self):
        pass

