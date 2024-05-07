import tkinter as tk
from image_picker import recognise_from_image

def run():
    root = tk.Tk()
    root.title("NZ Coin Recognition")
    root.geometry("300x150")

    # Button for recognition with individual images from files
    detect_button = tk.Button(root, text="Detect with Image", command=recognise_from_image)
    detect_button.pack(pady=15)

    root.mainloop()


if __name__ == "__main__":
    run()