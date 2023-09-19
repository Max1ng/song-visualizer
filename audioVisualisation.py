import tkinter as tk
from PIL import Image, ImageTk

# Create a tkinter window
root = tk.Tk()
root.title("Canvas with PNG Background")

# Create a canvas
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Load the background PNG image
background_image = Image.open("background.png")
background_photo = ImageTk.PhotoImage(background_image)

# Display the background image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

# Load the second PNG image with a transparent background
second_image = Image.open("rocket.png")
second_photo = ImageTk.PhotoImage(second_image, format="png")

# Create a tkinter Label widget for the second image
second_label = tk.Label(root, image=second_photo)

# Place the second image on top of the canvas at specific coordinates (x, y)
x, y = 100, 100  # Adjust these coordinates as needed
second_label.place(x=x, y=y)

# Keep references to the images and the Label widget to prevent them from being garbage collected
canvas.background_photo = background_photo
second_label.photo = second_photo

# Run the tkinter main loop
root.mainloop()
