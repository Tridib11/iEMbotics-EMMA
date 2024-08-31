import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import speech_recognition as sr
from gtts import gTTS
import pygame
import time

# Predefined questions and answers
qa_dict = {
    "hello": "Hi!, how may i help you",
    "how are you": "I am fine, thank you!",
    "what is your name": "My name is EMMA.",
    "what can you do": "I am a medical assistant robot.",
    "i am sick": "I will inform the doctors.",
    "where is the general medicine": "turn right you should see pharmacy, take left from pharmacy and use the stairs . on 2nd floor you can find general medicine block",
    "where is the eye department": "turn right from the pharmacy for ten steps."
}

# Initialize pygame for audio playback
pygame.mixer.init()

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.set_volume(1.0)  # Full volume
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.5)  # Increased speed by reducing sleep time

def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
    
    try:
        query = recognizer.recognize_google(audio)
        print(f"Recognized: {query}")
        return query.lower()
    except sr.UnknownValueError:
        return "Sorry, I did not understand that."

def handle_microphone_click():
    status_label.config(text="Listening...")
    root.update_idletasks()
    
    query = recognize_speech()
    if query in qa_dict:
        response = qa_dict[query]
    else:
        response = "Sorry, I don't have an answer for that."
    
    print(f"Response: {response}")
    text_to_speech(response)
    status_label.config(text=response)

def update_background():
    # Resize the background image to fit the window
    width = root.winfo_width()
    height = root.winfo_height()
    bg_image = Image.open("/home/pi/backg.jpg")
    bg_image = bg_image.resize((width, height), Image.ANTIALIAS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label.config(image=bg_photo)
    bg_label.image = bg_photo

# Create the main window
root = tk.Tk()
root.title("Speech Assistant")

# Set the window to full screen
root.attributes('-fullscreen', True)
root.bind("<F11>", lambda e: root.attributes('-fullscreen', True))  # Bind F11 to toggle fullscreen
root.bind("<Escape>", lambda e: root.attributes('-fullscreen', False))  # Bind Escape to exit fullscreen

# Load and set the background image
bg_image = Image.open("/home/pi/backg.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Bind the resize event to update the background image
root.bind("<Configure>", lambda event: update_background())

# Load and set the microphone button image
mic_image = Image.open("/home/pi/microphone.jpg")
mic_image = mic_image.resize((100, 100), Image.ANTIALIAS)  # Resize image as needed
mic_photo = ImageTk.PhotoImage(mic_image)
mic_button = Button(root, image=mic_photo, command=handle_microphone_click, borderwidth=0)
mic_button.place(relx=0.5, rely=0.4, anchor='center')

# Label to display the status or response
status_label = Label(root, text="", bg="white", font=("Helvetica", 12), wraplength=280)
status_label.place(relx=0.5, rely=0.7, anchor='center')

# Run the main loop
root.mainloop()
