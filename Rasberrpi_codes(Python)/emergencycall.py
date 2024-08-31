import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import serial
import time
import RPi.GPIO as GPIO

# Initialize GPIO and serial port
GPIO.setmode(GPIO.BOARD)
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

def call_doctor():
    port.write(b'ATD+917439433288;\r')  # AT command to dial a number
    print("Calling Doctor...")
    time.sleep(3)  # Wait to ensure the command is sent

def text_doctor():
    port.write(b'AT+CMGF=1\r')  # Set SMS mode
    time.sleep(1)
    port.write(b'AT+CMGS="+917439433288"\r')  # Set recipient
    time.sleep(1)
    port.write(str.encode("Hey Doctor, Patient need your help!!!" + chr(26)))  # Send message
    time.sleep(3)
    print("Message sent...")

def close_window():
    GPIO.cleanup()  # Clean up GPIO before closing
    root.destroy()  # Close the Tkinter window

# Create the main window
root = tk.Tk()
root.title("Doctor Communication")

# Make the window full screen
root.attributes('-fullscreen', True)

# Load and set background image
background_image_path = "/home/pi/background.jpg"
background_image = Image.open(background_image_path)
background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas to place the background image
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack(fill="both", expand=True)

# Add background image to canvas
canvas.create_image(0, 0, anchor="nw", image=background_photo)

# Load and resize the icon images
call_icon_image_path = "/home/pi/call.jpg"
call_icon_image = Image.open(call_icon_image_path)
call_icon_image = call_icon_image.resize((50, 50), Image.ANTIALIAS)  # Resize to 50x50 pixels
call_icon_photo = ImageTk.PhotoImage(call_icon_image)

text_icon_image_path = "/home/pi/text.jpg"
text_icon_image = Image.open(text_icon_image_path)
text_icon_image = text_icon_image.resize((50, 50), Image.ANTIALIAS)  # Resize to 50x50 pixels
text_icon_photo = ImageTk.PhotoImage(text_icon_image)

# Create and place the title label on the canvas
title_label = tk.Label(root, text="EMMA Emergency Call Service", font=('Arial', 30, 'bold'), bg='white', fg='black')
title_label_window = canvas.create_window(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 6, anchor="center", window=title_label)

# Create and place buttons on the canvas with icons
call_button = tk.Button(root, text="Call Doctor", command=call_doctor, font=('Arial', 20), bg='white', fg='black', image=call_icon_photo, compound="left")
call_button_window = canvas.create_window(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2, anchor="center", window=call_button)

text_button = tk.Button(root, text="Text Doctor", command=text_doctor, font=('Arial', 20), bg='white', fg='black', image=text_icon_photo, compound="left")
text_button_window = canvas.create_window(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 1.5, anchor="center", window=text_button)

# Create and place the close button
close_button = tk.Button(root, text="Close", command=close_window, font=('Arial', 20), bg='red', fg='white')
close_button_window = canvas.create_window(root.winfo_screenwidth() -590, root.winfo_screenheight() - 50, anchor="se", window=close_button)

# Start the GUI event loop
root.mainloop()

# Cleanup GPIO
GPIO.cleanup()
