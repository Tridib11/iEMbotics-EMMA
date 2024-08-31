import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import sys

class UserProfileCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("User Profile Creator")

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

        # Variables to store user inputs
        self.name_var = tk.StringVar()
        self.age_var = tk.IntVar()
        self.dob_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.photo_path = '/home/pi/Image.jpg'

        # Create labels and entry fields
        label_font = ("Helvetica", 24, "bold")
        entry_font = ("Helvetica", 24, "bold")
        label_color = "white"

        # Adjusting the positions to the left and down
        label_x = screen_width * 0.35
        entry_x = screen_width * 0.45
        start_y = screen_height * 0.25  # Starting y position for the first label
        vertical_spacing = screen_height * 0.07  # Space between each entry (reduced gap)

        # Add a title above the registration form
        self.canvas.create_text(screen_width / 2, start_y - vertical_spacing * 1.5, text="Automatic Registration", font=("Helvetica", 30, "bold"), fill="white")

        self.canvas.create_text(label_x, start_y, text="Name:", font=label_font, fill=label_color, anchor="w")
        self.name_entry = tk.Entry(self.root, textvariable=self.name_var, font=entry_font)
        self.canvas.create_window(entry_x, start_y, window=self.name_entry, anchor="w")

        self.canvas.create_text(label_x, start_y + vertical_spacing, text="Age:", font=label_font, fill=label_color, anchor="w")
        self.age_entry = tk.Entry(self.root, textvariable=self.age_var, font=entry_font)
        self.canvas.create_window(entry_x, start_y + vertical_spacing, window=self.age_entry, anchor="w")

        self.canvas.create_text(label_x, start_y + 2 * vertical_spacing, text="DOB:", font=label_font, fill=label_color, anchor="w")
        self.dob_entry = tk.Entry(self.root, textvariable=self.dob_var, font=entry_font)
        self.canvas.create_window(entry_x, start_y + 2 * vertical_spacing, window=self.dob_entry, anchor="w")

        self.canvas.create_text(label_x, start_y + 3 * vertical_spacing, text="Gender:", font=label_font, fill=label_color, anchor="w")
        self.gender_entry = tk.Entry(self.root, textvariable=self.gender_var, font=entry_font)
        self.canvas.create_window(entry_x, start_y + 3 * vertical_spacing, window=self.gender_entry, anchor="w")

        # Button to take picture
        self.take_picture_button = tk.Button(self.root, text="Take Picture", font=label_font, command=self.take_picture)
        self.canvas.create_window(entry_x+75, start_y + 4 * vertical_spacing, window=self.take_picture_button, anchor="w")

        # Button to create profile
        self.create_profile_button = tk.Button(self.root, text="Create Profile", font=label_font, command=self.create_profile)
        self.canvas.create_window(entry_x+65, start_y + 5 * vertical_spacing, window=self.create_profile_button, anchor="w")

        # Close button
        self.close_button = tk.Button(self.root, text="Close", font=label_font, command=self.close_app)
        self.canvas.create_window(entry_x+124, start_y + 6 * vertical_spacing, window=self.close_button, anchor="w")

    def take_picture(self):
        # Execute the command to take a picture
        try:
            subprocess.run(["rpicam-still", "-o", self.photo_path], check=True)
            messagebox.showinfo("Success", "Picture taken successfully!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to take picture: {e}")

    def create_profile(self):
        name = self.name_var.get()
        age = self.age_var.get()
        dob = self.dob_var.get()
        gender = self.gender_var.get()

        if not all([name, age, dob, gender]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        
        # Create user profile (you can store or process the information as needed)
        profile = {
            "Name": name,
            "Age": age,
            "DOB": dob,
            "Gender": gender,
            "Photo Path": self.photo_path
        }
        print("User Profile Created Successfully!")
        print(profile)

        # Open a new window to display the profile
        self.show_profile(profile)

    def show_profile(self, profile):
        new_window = tk.Toplevel(self.root)
        new_window.title("User Profile")

        # Set the window to fullscreen
        new_window.attributes("-fullscreen", True)

        # Get screen width and height
        screen_width = new_window.winfo_screenwidth()
        screen_height = new_window.winfo_screenheight()

        # Load and set the background image for the profile window
        profile_background_path = '/home/pi/bck.jpg'
        profile_bg_image = Image.open(profile_background_path)
        self.profile_bg_photo = ImageTk.PhotoImage(profile_bg_image.resize((screen_width, screen_height)))

        new_canvas = tk.Canvas(new_window, width=screen_width, height=screen_height)
        new_canvas.pack(fill="both", expand=True)
        new_canvas.create_image(0, 0, image=self.profile_bg_photo, anchor="nw")

        new_canvas.create_text(screen_width * 0.4, screen_height * 0.4, text=f"Name: {profile['Name']}", font=("Helvetica", 24, "bold"), fill="white", anchor="w")
        new_canvas.create_text(screen_width * 0.4, screen_height * 0.5, text=f"Age: {profile['Age']}", font=("Helvetica", 24, "bold"), fill="white", anchor="w")
        new_canvas.create_text(screen_width * 0.4, screen_height * 0.6, text=f"DOB: {profile['DOB']}", font=("Helvetica", 24, "bold"), fill="white", anchor="w")
        new_canvas.create_text(screen_width * 0.4, screen_height * 0.7, text=f"Gender: {profile['Gender']}", font=("Helvetica", 24, "bold"), fill="white", anchor="w")

        try:
            image = Image.open(profile["Photo Path"])
            image = image.resize((290, 290), Image.ANTIALIAS)  # Width x Height
            photo = ImageTk.PhotoImage(image)
            img_label = tk.Label(new_window, image=photo)
            img_label.photo = photo  # Keep a reference to avoid garbage collection
            new_canvas.create_window(screen_width * 0.5, screen_height * 0.2, window=img_label)
        except IOError:
            new_canvas.create_text(screen_width * 0.75, screen_height * 0.3, text="Error opening photo", font=("Helvetica", 24, "bold"), fill="white")

        # Back button
        back_button = tk.Button(new_window, text="Back", font=("Helvetica", 24, "bold"), command=new_window.destroy)
        new_canvas.create_window(screen_width * 0.5, screen_height * 0.8, window=back_button)

    def close_app(self):
        self.root.destroy()
        sys.exit()

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = UserProfileCreator(root)
    root.mainloop()
