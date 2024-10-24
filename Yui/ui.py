# Import required Libraries
from tkinter import *
from PIL import Image, ImageTk
import cv2


# Create an instance of TKinter Window or frame
win = Tk()
win.config(bg="black")
win.title("Ender 3 Pro")

# Set the size of the window
win.minsize(width=300, height=300)

label_text = Label(text="ENDER 3 PRO", bg="black", fg="white", font=("Hallowen Inline", 24, "bold"))
label_text.grid(row=0, column=1)
label = Label(win, bg="black", padx=25, pady=25)
label.grid(row=1, column=0, columnspan=3)
cap = cv2.VideoCapture(0)


# Define function to show frame
def show_frames():
    # Get the latest frame and convert into Image
    cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    # Repeat after an interval to capture continiously
    label.after(20, show_frames)


show_frames()
win.mainloop()
