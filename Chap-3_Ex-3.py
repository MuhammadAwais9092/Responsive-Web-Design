# Chapter 3 Exercise 3: Area Function

import tkinter as tk
from tkinter import ttk
import math

def calculate_circle_area():
    try:
        radius = float(entry_circle_radius.get())
        area = math.pi * (radius ** 2)
        result_circle_var.set(f"Area of Circle: {area:.2f} square units")
    except ValueError:
        result_circle_var.set("Invalid input. Please enter a valid number.")

def calculate_square_area():
    try:
        side_length = float(entry_square_side.get())
        area = side_length ** 2
        result_square_var.set(f"Area of Square: {area:.2f} square units")
    except ValueError:
        result_square_var.set("Invalid input. Please enter a valid number.")

def calculate_rectangle_area():
    try:
        length = float(entry_rectangle_length.get())
        width = float(entry_rectangle_width.get())
        area = length * width
        result_rectangle_var.set(f"Area of Rectangle: {area:.2f} square units")
    except ValueError:
        result_rectangle_var.set("Invalid input. Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Shape Area Calculator")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)

# Create tabs for Circle, Square, and Rectangle
tab_circle = ttk.Frame(notebook)
tab_square = ttk.Frame(notebook)
tab_rectangle = ttk.Frame(notebook)

notebook.add(tab_circle, text="Circle")
notebook.add(tab_square, text="Square")
notebook.add(tab_rectangle, text="Rectangle")

notebook.pack(fill="both", expand=True)

# Circle Tab
label_circle_radius = tk.Label(tab_circle, text="Enter Radius:")
entry_circle_radius = tk.Entry(tab_circle)
button_calculate_circle = tk.Button(tab_circle, text="Calculate", command=calculate_circle_area)
result_circle_var = tk.StringVar()
label_result_circle = tk.Label(tab_circle, textvariable=result_circle_var)

label_circle_radius.grid(row=0, column=0, padx=10, pady=5)
entry_circle_radius.grid(row=0, column=1, padx=10, pady=5)
button_calculate_circle.grid(row=1, column=0, columnspan=2, pady=10)
label_result_circle.grid(row=2, column=0, columnspan=2)

# Square Tab
label_square_side = tk.Label(tab_square, text="Enter Side Length:")
entry_square_side = tk.Entry(tab_square)
button_calculate_square = tk.Button(tab_square, text="Calculate", command=calculate_square_area)
result_square_var = tk.StringVar()
label_result_square = tk.Label(tab_square, textvariable=result_square_var)

label_square_side.grid(row=0, column=0, padx=10, pady=5)
entry_square_side.grid(row=0, column=1, padx=10, pady=5)
button_calculate_square.grid(row=1, column=0, columnspan=2, pady=10)
label_result_square.grid(row=2, column=0, columnspan=2)

# Rectangle Tab
label_rectangle_length = tk.Label(tab_rectangle, text="Enter Length:")
label_rectangle_width = tk.Label(tab_rectangle, text="Enter Width:")
entry_rectangle_length = tk.Entry(tab_rectangle)
entry_rectangle_width = tk.Entry(tab_rectangle)
button_calculate_rectangle = tk.Button(tab_rectangle, text="Calculate", command=calculate_rectangle_area)
result_rectangle_var = tk.StringVar()
label_result_rectangle = tk.Label(tab_rectangle, textvariable=result_rectangle_var)

label_rectangle_length.grid(row=0, column=0, padx=10, pady=5)
entry_rectangle_length.grid(row=0, column=1, padx=10, pady=5)
label_rectangle_width.grid(row=1, column=0, padx=10, pady=5)
entry_rectangle_width.grid(row=1, column=1, padx=10, pady=5)
button_calculate_rectangle.grid(row=2, column=0, columnspan=2, pady=10)
label_result_rectangle.grid(row=3, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()