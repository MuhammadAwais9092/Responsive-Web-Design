# Chapter 2 Exercise 1: Welcome

import tkinter as tk
from tkinter import font

def change_font():
    new_font = font.Font(framelabel, framelabel.cget("font"))
    new_font.config(family="Arial", weight="bold", size=16)
    framelabel.configure(font=new_font)

# Create the main window
root = tk.Tk()
root.title("Welcome Message")

# Set the default window size
root.geometry("400x200")

# Disable resizing the window
root.resizable(False, False)

# Add background color to the window
root.configure(bg="#ff1f1f")

# Create a frame
frame = tk.Frame(root, bg="#ff1f1f")

# Create a label in the frame
framelabel = tk.Label(frame, text="Welcome to My GUI Program!", font=("Helvetica", 14), bg="#ff1f1f")
framelabel.pack(pady=20)

# Create a button to change font style
change_font_button = tk.Button(frame, text="Change Font", command=change_font)
change_font_button.pack()

# Pack the frame into the main window
frame.pack(expand=True, fill="both")

# Run the main loop
root.mainloop()