# Chapter 4 Exercise 2: CountString

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def create_sentences_file():
    # Create a file named sentences.txt with sample content
    file_path = "sentences.txt"
    with open(file_path, "w") as file:
        file.write("Hello my name is Peter Parker\n")
        file.write("I love Python Programming\n")
        file.write("Love\n")
        file.write("Enemy\n")
    file_var.set(file_path)

def count_occurrences():
    # Get the selected file
    file_path = file_var.get()

    # Read the content of the file
    try:
        with open(file_path, "r") as file:
            content = file.read()

        # Get the search strings
        search_strings = [entry.get() for entry in entry_list]

        # Count occurrences for each search string
        result = {search_string: content.count(search_string) for search_string in search_strings}

        # Display the results
        text_output.delete(1.0, tk.END)
        for search_string, count in result.items():
            text_output.insert(tk.END, f"{search_string}: {count} occurrences\n")

    except FileNotFoundError:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "File not found. Please create sentences.txt first.")

# Create the main window
root = tk.Tk()
root.title("String Occurrence Counter")

# Create a frame to hold the controls
frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0)

# Create a button to create the sentences.txt file
create_button = ttk.Button(frame, text="Create sentences.txt", command=create_sentences_file)
create_button.grid(row=0, column=0, columnspan=3, pady=10)

# Create an entry for file path
file_var = tk.StringVar()
file_entry = ttk.Entry(frame, textvariable=file_var, state="readonly")
file_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Create a button to browse for a file
browse_button = ttk.Button(frame, text="Browse", command=lambda: browse_file("sentences.txt"))
browse_button.grid(row=1, column=2, padx=10, pady=10)

# Create entry widgets for search strings
entry_list = []
search_strings = ["Hello my name is Peter Parker", "I love Python Programming", "Love", "Enemy"]
for i, search_string in enumerate(search_strings):
    ttk.Label(frame, text=f"Search String {i+1}:").grid(row=i+2, column=0, padx=10, pady=5, sticky="e")
    entry = ttk.Entry(frame)
    entry.insert(tk.END, search_string)
    entry.grid(row=i+2, column=1, padx=10, pady=5)
    entry_list.append(entry)

# Create a button to count occurrences
count_button = ttk.Button(frame, text="Count Occurrences", command=count_occurrences)
count_button.grid(row=len(search_strings)+2, column=0, columnspan=3, pady=20)

# Create a text widget to display results
text_output = tk.Text(root, width=40, height=10)
text_output.grid(row=1, column=0, padx=20, pady=20)

# Function to browse for a file
def browse_file(default_filename):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")], initialfile=default_filename)
    file_var.set(file_path)

# Run the Tkinter event loop
root.mainloop()
