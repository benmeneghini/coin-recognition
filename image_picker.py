import tkinter as tk
from tkinter import filedialog
from detect import detection
import cv2

def detect_from_image():
    """
    Method to select an image from the file dialog and run the detection function on it.
    """
    # Create a file dialog to select an image
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])

    if not file_path:
        return 
    
    # Read the image
    image = cv2.imread(file_path)

    detection(image)
    root.destroy()

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break