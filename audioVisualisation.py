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
        self.blobPoints = []
        #background size
        self.canvas = tkinter.Canvas(master, width=1920, height=1080)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.onCanvasClick)

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
            
            #create blob and rocket
            self.drawBlob(750, 500, 200)
            self.master.after_idle(self.nextFrame)
            yield
            #delete current rocket and blob
            self.canvas.delete(rocketCanvas)
            self.canvas.delete(self.blob)

            #change direction every 25 deg
            if (angle - 330) % 25 == 0:
                direction *= -1

            angle += direction
            angle %= 360
            #wait .025 seconds between updates
            time.sleep(0.025)
            
    def drawBlob(self, x, y, size):
        
        points = 500  #complexity of the blob
        self.blobPoints = []

        for i in range(points):
            angle = math.radians(360 * i / points) 
            radius = size + size * 0.075 * math.sin(angle * 20) 
            
            xPoint = x + radius * math.cos(angle)
            yPoint = y - radius * math.sin(angle)
            self.blobPoints.extend([xPoint, yPoint])
        
        self.blob = self.canvas.create_polygon(self.blobPoints, outline='blue', width=2, fill='red')

    def onCanvasClick(self, event):
        x, y = event.x, event.y
        # Find the nearest blob point
        min_distance = float('inf')
        nearest_point_index = 0
        for i in range(0, len(self.blobPoints), 2):
            px, py = self.blobPoints[i], self.blobPoints[i + 1]
            distance = math.sqrt((x - px) ** 2 + (y - py) ** 2)
            if distance < min_distance:
                min_distance = distance
                nearest_point_index = i

        # Update the nearest blob point to the mouse click position
        self.blobPoints[nearest_point_index] = x
        self.blobPoints[nearest_point_index + 1] = y
        # Redraw the blob
        self.canvas.delete(self.blob)
        self.blob = self.canvas.create_polygon(self.blobPoints, outline='blue', width=2, fill='red')


root = tkinter.Tk()
#window size
root.geometry("1920x1080")
app = audioVisualization(root, 'rocket.png', 'background.png')
root.mainloop()
