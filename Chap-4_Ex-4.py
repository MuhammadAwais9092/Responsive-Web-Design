# Chapter 4 Exercise 4: letter count

import tkinter as tk
from tkinter import filedialog

def count_occurrences():
    # Get the selected file
    file_path = file_var.get()

    # Read the content of the file
    try:
        with open(file_path, "r") as file:
            content = file.read()

        # Get the character entered by the user
        char_to_count = char_entry.get()

        # Count occurrences of the character
        char_count = content.count(char_to_count)

        # Display the result
        result_label.config(text=f"Occurrences of '{char_to_count}': {char_count}")

    except FileNotFoundError:
        result_label.config(text="File not found. Please select a valid file.")

# Create the main window
root = tk.Tk()
root.title("Character Occurrence Counter")

# Create a frame to hold the controls
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Create an entry for file path
file_var = tk.StringVar()
file_entry = tk.Entry(frame, textvariable=file_var, state="readonly", width=40)
file_entry.grid(row=0, column=0, padx=10, pady=10)

# Create a button to browse for a file
browse_button = tk.Button(frame, text="Browse", command=lambda: browse_file("sentences.txt"))
browse_button.grid(row=0, column=1, padx=10, pady=10)

# Create an entry for the character
char_entry_label = tk.Label(frame, text="Enter a character:")
char_entry_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

char_entry = tk.Entry(frame, width=5)
char_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a button to count occurrences
count_button = tk.Button(frame, text="Count Occurrences", command=count_occurrences)
count_button.grid(row=2, column=0, columnspan=2, pady=20)

# Create a label to display the result
result_label = tk.Label(frame, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

# Function to browse for a file
def browse_file(default_filename):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")], initialfile=default_filename)
    file_var.set(file_path)

# Run the Tkinter event loop
root.mainloop()
