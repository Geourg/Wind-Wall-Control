import tkinter as tk
from tkinter import ttk

def update_color():
    for i in range(9):
        new_slider_value = color_sliders[i].get()
        new_rpm = int(new_slider_value * 255 / 100)
        color_value = int(255 * (1 - (new_rpm / 255)))
        color_hex = "#{:02X}{:02X}{:02X}".format(255, color_value, 0)
        fan_labels[i].config(text=f"Fan {i}\nRPM: {new_rpm}")
        fan_labels[i].configure(style="TLabel", background = color_hex)
window = tk.Tk()
window.title("Wind Wall GUI")
window.geometry("800x800")


# Set a modern style
style = ttk.Style()
style.configure("Horizontal.TScrollbar", sliderthickness=10)  # Customize slider appearance
style.map("Horizontal.TScrollbar", sliderlength=[("active", 20)])

# Create a 3x3 grid of fan control widgets with a modern appearance
fan_labels = []
color_sliders = []

for i in range(3):
    window.grid_rowconfigure(i, weight=1)  # Equal row weights

    for j in range(3):
        window.grid_columnconfigure(j, weight=1)
        fan_id = i * 3 + j

        label = ttk.Label(window, text=f"Fan {fan_id}\nRPM: 0", relief='solid', borderwidth=2, style="TLabel", width=5)
        label.grid(row=i, column=j, padx=5, pady=5, sticky='nsew')
        fan_labels.append(label)

        slider = tk.Scale(window, from_=0, to=100, orient='horizontal', length=100, label="Off - On")
        slider.set(0)
        slider.grid(row=i + 4, column=j, padx=5, pady=5)
        color_sliders.append(slider)

# Create a button with a modern appearance
update_button = ttk.Button(window, text="Update RPM", command=update_color)
update_button.grid(row=4, column=3, padx=10, pady=10, rowspan=3)

legend_canvas = tk.Canvas(window, width=150, height=100)
legend_canvas.grid(row=0, column=3, rowspan=3, padx=10, pady=10)

for i in range(256):
    color_value = 255 - i
    color_hex = "#{:02X}{:02X}{:02X}".format(255, color_value, 0)
    legend_canvas.create_line(i, 0, i, 100, fill=color_hex)

legend_canvas.create_text(0, 110, text="Min (0)", anchor='w')
legend_canvas.create_text(255, 110, text="Max (255)", anchor='e')

window.mainloop()
# need meshes
