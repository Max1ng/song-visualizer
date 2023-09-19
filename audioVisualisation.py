import time
import tkinter
from PIL import Image, ImageTk

class audioVisualization(object):
    def __init__(self, master, rocket, backgroundFile):
        self.master = master
        self.rocket = rocket
        self.backgroundFile = backgroundFile
        #background size
        self.canvas = tkinter.Canvas(master, width=1920, height=1080)
        self.canvas.pack()

        # set the background image
        backgroundImage = Image.open(self.backgroundFile)
        self.backgroundPhoto = ImageTk.PhotoImage(backgroundImage)
        self.canvas.create_image(0, 0, anchor=tkinter.NW, image=self.backgroundPhoto)

        self.nextFrame = self.draw().__next__ 
        master.after(1, self.nextFrame)

    def draw(self):
        image = Image.open(self.rocket)
        image = image.resize((image.width // 2, image.height // 2))  # change image size
        angle = 330 #start pointing NE
        direction = 1

        while True:
            rotatingImage = ImageTk.PhotoImage(image.rotate(angle))
            #image location
            rocketCanvas = self.canvas.create_image(750, 500, image=rotatingImage)
            self.master.after_idle(self.nextFrame)
            yield
            self.canvas.delete(rocketCanvas)

            #change direction every 25 deg
            if (angle - 330) % 25 == 0:
                direction *= -1

            angle += direction
            angle %= 360
            #wait .025 seconds between updates
            time.sleep(0.025)

root = tkinter.Tk()
#window size
root.geometry("1920x1080")
app = audioVisualization(root, 'rocket.png', 'background.png')
root.mainloop()
