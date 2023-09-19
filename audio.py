import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class audio:

    def __init__(self) -> None:
        self.sample_rate = 44100
        self.chunk_size = 1024
        self.p = pyaudio.PyAudio()

        #open input stream
        self.stream = self.p.open(
            format=pyaudio.paInt16, 
            #mono audio
            channels=1,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk_size
        )

    def createFigure(self): 
        self.fig, ax = plt.subplots()
        self.x = np.arange(0, self.chunk_size)
        self.line, = ax.plot(self.x, np.random.rand(self.chunk_size))
        ax.set_ylim(-32768, 32767)
    
    def update(self, frame):
        try:
            # read audio data from stream
            audio_data = np.frombuffer(self.stream.read(self.chunk_size), dtype=np.int16)
            
            # update plot
            self.line.set_ydata(audio_data)
            return self.line,
        
        except KeyboardInterrupt:
            self.ani.event_source.stop()
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()
            plt.close(self.fig)
            return []

    # create animation to update plot
    def createAnimation(self):
        self.ani = FuncAnimation(self.fig, self.update, blit=True)

    def showPlot(self):
        plt.show()
