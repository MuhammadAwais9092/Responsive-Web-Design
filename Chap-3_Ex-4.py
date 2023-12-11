# Chapter 3 Exercise 4: Draw Shape

import tkinter as tk
from tkinter import ttk

def draw_shape():
    canvas.delete("all")  # Clear the canvas

    selected_shape = shape_var.get()

    if selected_shape == "Oval":
        canvas.create_oval(100, 100, 300, 200, outline="black", fill="red")
    elif selected_shape == "Rectangle":
        canvas.create_rectangle(100, 100, 300, 200, outline="black", fill="green")
    elif selected_shape == "Square":
        canvas.create_rectangle(100, 100, 200, 200, outline="black", fill="blue")
    elif selected_shape == "Triangle":
        canvas.create_polygon(100, 200, 200, 100, 300, 200, outline="black", fill="yellow")

# Create the main window
root = tk.Tk()
root.title("Shape Drawer")

# Create a frame to hold the controls
frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0)

# Create a Label and Combobox for shape selection
label_shape = ttk.Label(frame, text="Select Shape:")
label_shape.grid(row=0, column=0, padx=10, pady=10)

shapes = ["Oval", "Rectangle", "Square", "Triangle"]
shape_var = tk.StringVar()
shape_combobox = ttk.Combobox(frame, textvariable=shape_var, values=shapes)
shape_combobox.grid(row=0, column=1, padx=10, pady=10)
shape_combobox.set(shapes[0])  # Set the default shape

# Create a button to draw the selected shape
draw_button = ttk.Button(frame, text="Draw Shape", command=draw_shape)
draw_button.grid(row=1, column=0, columnspan=2, pady=20)

# Create a canvas to draw the shapes
canvas = tk.Canvas(root, width=400, height=300, borderwidth=2, relief="solid")
canvas.grid(row=1, column=0, padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()
