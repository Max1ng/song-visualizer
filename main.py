from api import api
from audio import audio

#rocket?


if __name__ == "__main__":
    api = api()
    api.printSongs()
    topSong = api.getTopSongURI()

    
    audio = audio()
    audio.playSong(topSong)
    audio.createFigure()
    audio.createAnimation()
    audio.showPlot()

