import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import spotipy
from spotipy.oauth2 import SpotifyOAuth



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
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-library-read user-modify-playback-state"))
        

    def createFigure(self): 
        self.fig, ax = plt.subplots()
        self.x = np.arange(0, self.chunk_size)
        self.line, = ax.plot(self.x, np.random.rand(self.chunk_size))
        ax.set_ylim(-32768, 32767)
    
    def update(self, frame):
        
        try:
            # read audio data from stream
            audioData = np.frombuffer(self.stream.read(self.chunk_size), dtype=np.int16)
            
            # update plot
            self.line.set_ydata(audioData)
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
        self.ani = FuncAnimation(self.fig, self.update, blit=True, cache_frame_data=False)

    def showPlot(self):
        plt.show()

    def playSong(self, song):
        self.sp.start_playback(uris=[song])
