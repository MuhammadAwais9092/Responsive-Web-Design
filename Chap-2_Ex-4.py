# Chapter 2 Exercise 4: Registration page

import tkinter as tk
from tkinter import ttk

def submit_form():
    # Retrieve and print the entered data (you can modify this part as needed)
    print("Student Name:", entry_name.get())
    print("Mobile Number:", entry_mobile.get())
    print("Email ID:", entry_email.get())
    print("Home Address:", entry_address.get())
    print("Gender:", var_gender.get())
    print("Course Enrolled:", var_course.get())
    print("Languages Known:", var_languages.get())
    print("Communication Skills:", scale_communication.get())

def clear_form():
    # Clear all entry fields and selections
    entry_name.delete(0, tk.END)
    entry_mobile.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    gender_choices.set("")  # Clear the combobox
    var_course.set("")  # Clear the radio buttons
    var_languages.set("")  # Clear the checkboxes
    scale_communication.set(0)  # Reset the scale

# Create the main window
root = tk.Tk()
root.title("Student Management System")

# University Picture (Replace 'path_to_image' with the actual path to your image)
img = tk.PhotoImage(file='bath spa.png')
# Adjust width and height using subsample
img = img.subsample(4, 4)  # Adjust these values to control the size
label_picture = tk.Label(root, image=img)
label_picture.grid(row=0, column=0, columnspan=2)

# Text labels and entry widgets
tk.Label(root, text="Student Management System").grid(row=1, column=0, columnspan=2)
tk.Label(root, text="New Student Registration").grid(row=2, column=0, columnspan=2)

tk.Label(root, text="Student Name:").grid(row=3, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=3, column=1)

tk.Label(root, text="Mobile Number:").grid(row=4, column=0)
entry_mobile = tk.Entry(root)
entry_mobile.grid(row=4, column=1)

tk.Label(root, text="Email ID:").grid(row=5, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=5, column=1)

tk.Label(root, text="Home Address:").grid(row=6, column=0)
entry_address = tk.Entry(root)
entry_address.grid(row=6, column=1)

tk.Label(root, text="Gender:").grid(row=7, column=0)
var_gender = tk.StringVar()
gender_choices = ttk.Combobox(root, textvariable=var_gender, values=["Male", "Female", "Other"])
gender_choices.grid(row=7, column=1)

tk.Label(root, text="Course Enrolled:").grid(row=8, column=0)
var_course = tk.StringVar()
course_choices = ttk.Radiobutton(root, text="Bsc CC", variable=var_course, value="Bsc CC")
course_choices.grid(row=8, column=1, sticky="w")
course_choices = ttk.Radiobutton(root, text="Bsc Cy", variable=var_course, value="Bsc Cy")
course_choices.grid(row=9, column=1, sticky="w")
course_choices = ttk.Radiobutton(root, text="Bsc Psy", variable=var_course, value="Bsc Psy")
course_choices.grid(row=10, column=1, sticky="w")
course_choices = ttk.Radiobutton(root, text="BA & BM", variable=var_course, value="BA & BM")
course_choices.grid(row=11, column=1, sticky="w")

tk.Label(root, text="Languages Known:").grid(row=12, column=0)
var_languages = tk.StringVar()
language_choices = ttk.Checkbutton(root, text="English", variable=var_languages, onvalue="English", offvalue="")
language_choices.grid(row=12, column=1, sticky="w")
language_choices = ttk.Checkbutton(root, text="Tagalog", variable=var_languages, onvalue="Tagalog", offvalue="")
language_choices.grid(row=13, column=1, sticky="w")
language_choices = ttk.Checkbutton(root, text="Urdu/Hindi", variable=var_languages, onvalue="Urdu/Hindi", offvalue="")
language_choices.grid(row=14, column=1, sticky="w")

tk.Label(root, text="Rate Your Communication Skills:").grid(row=15, column=0)
scale_communication = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, showvalue=0, length=200)
scale_communication.grid(row=15, column=1)

# Set date entry labels to grey
for child in root.winfo_children():
    if isinstance(child, tk.Label) and child.cget("text").endswith(":"):
        child.config(fg="grey")

# Clear and Submit buttons
clear_button = tk.Button(root, text="Clear", command=clear_form)
clear_button.grid(row=17, column=0, pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=17, column=1, pady=10)

# Run the GUI
root.mainloop()