import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import os

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Hi! I am EMMA")

        # Set the window to fullscreen
        self.root.attributes("-fullscreen", True)

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Load and set the background image
        self.background_path = '/home/pi/background.jpg'
        self.bg_image = Image.open(self.background_path)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image.resize((screen_width, screen_height)))

        self.canvas = tk.Canvas(self.root, width=screen_width, height=screen_height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Add title and subtitle
        self.canvas.create_text(screen_width // 2.1, 180, text="Hi! I am EMMA", font=("Helvetica", 48, "bold"), fill="white")
        self.canvas.create_text(screen_width // 2.1, 280, text="How may I assist you?", font=("Helvetica", 36, "bold"), fill="white")

        # Button attributes
        button_font = ("Helvetica", 24, "bold")
        button_bg = "#333"
        button_fg = "white"
        button_active_bg = "#555"
        button_width = 22
        button_height = 2

        # Calculate button positions
        button_x1 = screen_width // 2.7
        button_x2 = screen_width * 5.8 // 10
        button_y_offset = 300
        button_y_gap = 120

        # Create buttons with spacing
        self.create_button("Automatic registration", button_x1, button_y_offset+button_y_gap, self.run_user_py)
        self.create_button("Check your vitals", button_x2, button_y_offset + button_y_gap, self.run_sp02_py)
        self.create_button("Play & Watch", button_x1, button_y_offset + 2*  button_y_gap, self.run_play_py)
        self.create_button("Emergency Call Service", button_x2, button_y_offset + 2*  button_y_gap, self.run_emergencycall_py)
        self.create_button("Chatbot", button_x1, button_y_offset + 3 * button_y_gap, self.run_chatbot2_py)
        self.create_button("Medicine dispenser", button_x2, button_y_offset + 3 * button_y_gap, self.placeholder_function)

    def create_button(self, text, x, y, command):
        button_font = ("Helvetica", 24, "bold")
        button_bg = "#333"
        button_fg = "white"
        button_active_bg = "#555"
        button_width = 20
        button_height = 2

        button = tk.Button(self.root, text=text, font=button_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, width=button_width, height=button_height, command=command)
        self.canvas.create_window(x, y, window=button)

    def run_user_py(self):
        # Execute the user.py script from the downloads folder
        try:
            script_path = os.path.expanduser("/home/pi/Downloads/user.py")
            subprocess.run(["python3", script_path], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to execute user.py: {e}")
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"File not found: {e}")
    def run_sp02_py(self):
        # Execute the user.py script from the downloads folder
        try:
            script_path = os.path.expanduser("/home/pi/Downloads/sp02.py")
            subprocess.run(["python3", script_path], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to execute user.py: {e}")
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"File not found: {e}")
    def run_chatbot2_py(self):
        # Execute the user.py script from the downloads folder
        try:
            script_path = os.path.expanduser("/home/pi/Downloads/chatbot2.py")
            subprocess.run(["python3", script_path], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to execute user.py: {e}")
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"File not found: {e}")
    def run_emergencycall_py(self):
        # Execute the user.py script from the downloads folder
        try:
            script_path = os.path.expanduser("/home/pi/Downloads/emergencycall.py")
            subprocess.run(["python3", script_path], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to execute user.py: {e}")
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"File not found: {e}")
    def run_play_py(self):
        # Execute the user.py script from the downloads folder
        try:
            script_path = os.path.expanduser("/home/pi/Downloads/play.py")
            subprocess.run(["python3", script_path], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to execute user.py: {e}")
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"File not found: {e}")       

    def placeholder_function(self):
        # Placeholder function for other buttons
        messagebox.showinfo("Info", "This button is not yet implemented.")

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
