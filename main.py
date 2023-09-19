from api import api
from audio import audio
from recordSystemAudio import recordSystemAudio
#rocket?


if __name__ == "__main__":
    api = api()
    api.printSongs()
    topSong = api.getTopSongURI()

    recordSystemAudio = recordSystemAudio()
    recordSystemAudio.captureAudio()

    

    audio = audio()
    audio.playSong(topSong)
    audio.createFigure()
    audio.createAnimation()
    audio.showPlot()

