import soundcard as sc

class recordSystemAudio:

    def __init__(self) -> None:
        self.sampleRate = 44100
        self.recordSec = 5

    def captureAudio(self):
        with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=self.sampleRate) as mic:
            
            for _ in range(self.recordSec):
                self.currentlyPlaying = mic.record(numframes=self.sampleRate)
                #stores as a float64 type



""" if __name__ == "__main__":
    recorder = recordSystemAudio()
    recorder.captureAudio() """