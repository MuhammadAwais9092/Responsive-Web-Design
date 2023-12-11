# Chapter 2 Exercise 5: Calculator

import tkinter as tk

def perform_operation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operation_var.get()

        if operator == "Addition":
            result.set(num1 + num2)
        elif operator == "Subtraction":
            result.set(num1 - num2)
        elif operator == "Multiplication":
            result.set(num1 * num2)
        elif operator == "Division":
            result.set(num1 / num2)
        elif operator == "Modulo":
            result.set(num1 % num2)
        else:
            result.set("Invalid Operation")

    except ValueError:
        result.set("Invalid Input")

# Create the main window
root = tk.Tk()
root.title("Basic Arithmetic Calculator")

# Variables for user input, operation, and result
entry_num1 = tk.Entry(root, width=20)
entry_num2 = tk.Entry(root, width=20)
operation_var = tk.StringVar(value="Addition")
result = tk.StringVar()

# Widgets
tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division", "Modulo").grid(row=1, column=0, columnspan=2, padx=10, pady=10)
tk.Button(root, text="Calculate", command=perform_operation).grid(row=2, column=0, columnspan=2, padx=10, pady=10)
tk.Label(root, textvariable=result).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Arrange entry widgets
entry_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num2.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()