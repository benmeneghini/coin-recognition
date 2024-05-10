import tkinter as tk
from image_picker import detect_from_image
from live_feed import get_live_feed

def run():
    """
    Main method to run the application.
    """
    root = tk.Tk()
    root.title("Face Mask Detector")
    root.geometry("300x150")

    # Button for capturing live video for real-time recognition
    capture_button = tk.Button(root, text="Real-time Recognition", command=get_live_feed)
    capture_button.pack(pady=15)

    # Button for recognition with individual images from files
    detect_button = tk.Button(root, text="Detect with Image", command=detect_from_image)
    detect_button.pack(pady=15)

    # If ESC key is pressed, close the window
    root.bind("<Escape>", lambda e: root.quit())

    root.mainloop()


run()