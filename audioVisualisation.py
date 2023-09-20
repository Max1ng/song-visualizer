import time
import tkinter
from PIL import Image, ImageTk
import math
from random import *

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
            

            self.drawBlob(750, 500, randint(100, 200))
            self.master.after_idle(self.nextFrame)
            yield
            #self.canvas.delete(self.blob)
            self.canvas.delete(rocketCanvas)
            

            #change direction every 25 deg
            if (angle - 330) % 25 == 0:
                direction *= -1

            angle += direction
            angle %= 360
            #wait .025 seconds between updates
            time.sleep(0.025)
            
    def drawBlob(self, x, y, size):
        blob_points = []
        num_points = 12  # You can adjust this number to control the complexity of the blob shape.
        
        for i in range(num_points):
            angle = math.radians(360 * i / num_points)  # Use a full circle (360 degrees) for the blob.
            radius = size + size * 0.3 * math.sin(angle * 5)  # Adjust the multiplier (5) for the blob shape.
            
            xPoint = x + radius * math.cos(angle)
            yPoint = y - radius * math.sin(angle)
            blob_points.extend([xPoint, yPoint])
        
        self.blob = self.canvas.create_polygon(blob_points, outline='blue', width=2, fill='cyan')


root = tkinter.Tk()
#window size
root.geometry("1920x1080")
app = audioVisualization(root, 'rocket.png', 'background.png')
root.mainloop()
