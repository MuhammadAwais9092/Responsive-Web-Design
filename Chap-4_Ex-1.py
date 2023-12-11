# Chapter 4 Exercise 1: User information

import tkinter as tk
from tkinter import ttk

def save_bio():
    # Get user input
    name = entry_name.get()
    age = entry_age.get()
    hometown = entry_hometown.get()

    # Write data to the file
    file_path = "bio.txt"
    with open(file_path, "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Hometown: {hometown}\n")

def read_bio():
    # Read data from the file
    file_path = "bio.txt"
    try:
        with open(file_path, "r") as file:
            bio_data = file.read()
        text_output.delete(1.0, tk.END)  # Clear previous output
        text_output.insert(tk.END, bio_data)
    except FileNotFoundError:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "Bio file not found. Please save your bio first.")

# Create the main window
root = tk.Tk()
root.title("Bio Data App")

# Create a frame to hold the controls
frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0)

# Create entry widgets for user input
label_name = ttk.Label(frame, text="Name:")
label_age = ttk.Label(frame, text="Age:")
label_hometown = ttk.Label(frame, text="Hometown:")
entry_name = ttk.Entry(frame)
entry_age = ttk.Entry(frame)
entry_hometown = ttk.Entry(frame)

label_name.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_name.grid(row=0, column=1, padx=10, pady=10)
label_age.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_age.grid(row=1, column=1, padx=10, pady=10)
label_hometown.grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_hometown.grid(row=2, column=1, padx=10, pady=10)

# Create buttons to save and read bio
button_save = ttk.Button(frame, text="Save Bio", command=save_bio)
button_save.grid(row=3, column=0, columnspan=2, pady=20)
button_read = ttk.Button(frame, text="Read Bio", command=read_bio)
button_read.grid(row=4, column=0, columnspan=2, pady=20)

# Create a text widget to display bio data
text_output = tk.Text(root, width=40, height=10)
text_output.grid(row=1, column=0, padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()