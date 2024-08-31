import tkinter as tk
from tkinter import Label, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time

# Function to update the plot
def animate(i):
    global x_data, y_hr_data, y_spo2_data, y_resp_data

    # Simulate sensor data for now (replace with actual sensor reading code)
    hr = random.randint(50, 100)
    spo2 = random.uniform(95, 100)
    resp = random.randint(20, 40)

    hr_label.config(text=f"HR: {hr} bpm")
    spo2_label.config(text=f"SpO2: {spo2:.1f} %")
    resp_label.config(text=f"RESP: {resp} rpm")

    x_data.append(time.time())
    y_hr_data.append(hr)
    y_spo2_data.append(spo2)
    y_resp_data.append(resp)

    if len(x_data) > 50:
        x_data = x_data[-50:]
        y_hr_data = y_hr_data[-50:]
        y_spo2_data = y_spo2_data[-50:]
        y_resp_data = y_resp_data[-50:]

    ax1.clear()
    ax2.clear()
    ax3.clear()

    ax1.plot(x_data, y_hr_data, 'g-')
    ax2.plot(x_data, y_spo2_data, 'b-')
    ax3.plot(x_data, y_resp_data, 'r-')

    ax1.set_title('Heart Rate (HR)')
    ax2.set_title('Oxygen Saturation (SpO2)')
    ax3.set_title('Respiration Rate (RESP)')

    # Write the latest values on the right side of each graph
    ax1.text(1.01, 0.5, f"{hr} bpm", transform=ax1.transAxes, fontsize=12, verticalalignment='center')
    ax2.text(1.01, 0.5, f"{spo2:.1f} %", transform=ax2.transAxes, fontsize=12, verticalalignment='center')
    ax3.text(1.01, 0.5, f"{resp} rpm", transform=ax3.transAxes, fontsize=12, verticalalignment='center')

ani = None  # Initialize the animation variable

# Function to start the animation
def start_animation():
    global ani
    if ani is None:
        ani = animation.FuncAnimation(fig, animate, interval=1000)
        canvas.draw()

# Function to stop the animation and clear the output
def stop_animation():
    global ani
    if ani is not None:
        ani.event_source.stop()
        ani = None
        x_data.clear()
        y_hr_data.clear()
        y_spo2_data.clear()
        y_resp_data.clear()
        ax1.clear()
        ax2.clear()
        ax3.clear()
        hr_label.config(text="HR: -- bpm")
        spo2_label.config(text="SpO2: -- %")
        resp_label.config(text="RESP: -- rpm")
        canvas.draw()

# Create the main application window
root = tk.Tk()
root.title("Health Monitor")
root.attributes('-fullscreen', True)  # Set the window to full screen

# Create a heading label
heading_label = Label(root, text="Vital Sign Checking", font=("Helvetica", 30))
heading_label.pack(pady=10)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, pady=5)

start_button = Button(button_frame, text="Start", command=start_animation, font=("Helvetica", 14))
start_button.pack(side=tk.LEFT, padx=5)

stop_button = Button(button_frame, text="Stop", command=stop_animation, font=("Helvetica", 14))
stop_button.pack(side=tk.LEFT, padx=5)

# Create a close button
close_button = Button(button_frame, text="Close", command=root.quit, font=("Helvetica", 14))
close_button.pack(side=tk.LEFT, padx=5)

# Create a frame to hold the canvas and labels
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Create a frame for the canvas
canvas_frame = tk.Frame(main_frame)
canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a figure for the plot
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))  # Adjust the figure size
fig.tight_layout(pad=3.0)

# Setup the plot
canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Create a frame for the labels
label_frame = tk.Frame(main_frame)
label_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

# Create a label for heart rate
hr_label = Label(label_frame, text="HR: -- bpm", font=("Helvetica", 20))
hr_label.pack(anchor='n', pady=10)

# Create a label for SpO2
spo2_label = Label(label_frame, text="SpO2: -- %", font=("Helvetica", 20))
spo2_label.pack(anchor='n', pady=20)

# Create a label for respiration rate
resp_label = Label(label_frame, text="RESP: -- rpm", font=("Helvetica", 20))
resp_label.pack(anchor='n', pady=10)

x_data = []
y_hr_data = []
y_spo2_data = []
y_resp_data = []

root.mainloop()
