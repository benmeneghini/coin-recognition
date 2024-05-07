import tkinter as tk
from tkinter import filedialog
from recognition import recognise

def recognise_from_image():
    # Create a file dialog to select an image
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    
    recognise(file_path)
    root.destroy()