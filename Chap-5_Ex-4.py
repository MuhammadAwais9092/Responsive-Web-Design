# Chapter 5 Exercise 4: Shapes

import tkinter as tk
from math import pi

class Shape:
    def __init__(self):
        self.sides = []  # Initialize a list to store the sides of the shape

    def inputSides(self):
        pass  # To be implemented by subclasses, collects input for the sides

    def area(self):
        pass  # To be implemented by subclasses, calculates and returns the area

class Circle(Shape):
    def inputSides(self):
        radius = float(input("Enter the radius of the circle: "))
        self.sides = [radius]  # Store the radius in the sides list

    def area(self):
        return pi * self.sides[0] ** 2  # Calculate and return the area of the circle

class Rectangle(Shape):
    def inputSides(self):
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        self.sides = [length, width]  # Store the length and width in the sides list

    def area(self):
        return self.sides[0] * self.sides[1]  # Calculate and return the area of the rectangle

class Triangle(Shape):
    def inputSides(self):
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        self.sides = [base, height]  # Store the base and height in the sides list

    def area(self):
        return 0.5 * self.sides[0] * self.sides[1]  # Calculate and return the area of the triangle

class ShapeCalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shape Area Calculator")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.shape_label = tk.Label(self, text="Select a shape:")
        self.shape_label.pack()

        self.shape_var = tk.StringVar()
        self.shape_var.set("Circle")  # Default shape

        self.shape_menu = tk.OptionMenu(self, self.shape_var, "Circle", "Rectangle", "Triangle")
        self.shape_menu.pack()

        self.calculate_button = tk.Button(self, text="Calculate Area", command=self.calculate_area)
        self.calculate_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def calculate_area(self):
        selected_shape = self.shape_var.get()

        if selected_shape == "Circle":
            shape = Circle()
        elif selected_shape == "Rectangle":
            shape = Rectangle()
        elif selected_shape == "Triangle":
            shape = Triangle()
        else:
            return

        shape.inputSides()
        area_result = shape.area()

        self.result_label.config(text=f"Area of {selected_shape}: {area_result}")

# Instantiate the ShapeCalculatorGUI class
app = ShapeCalculatorGUI()
app.mainloop()
