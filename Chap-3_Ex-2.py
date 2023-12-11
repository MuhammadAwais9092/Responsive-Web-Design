# Chapter 3 Exercise 2: Coffee Vending Machine

import tkinter as tk
from tkinter import ttk, messagebox

class CoffeeVendingMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Vending Machine")

        # Coffee options
        self.coffee_var = tk.StringVar()
        self.coffee_var.set("Select Coffee")

        # Add some coffee options
        coffee_options = ["Espresso", "Cappuccino", "Latte", "Americano"]

        # Create Coffee Frame
        coffee_frame = tk.Frame(root, padx=20, pady=20)
        coffee_frame.grid(row=0, column=0)

        # Label and Dropdown for Coffee selection
        coffee_label_text = tk.Label(coffee_frame, text="Select Coffee:")
        coffee_label_text.grid(row=0, column=0)

        coffee_dropdown = ttk.Combobox(coffee_frame, textvariable=self.coffee_var, values=coffee_options)
        coffee_dropdown.grid(row=0, column=1)

        # Add image for coffee (replace 'path_to_image' with the actual path to your images)
        coffee_image = tk.PhotoImage(file='bath spa.png')
        coffee_label_image = tk.Label(coffee_frame, image=coffee_image)
        coffee_label_image.image = coffee_image
        coffee_label_image.grid(row=1, column=0, columnspan=2, pady=(10, 0))

        # Create Options Frame
        options_frame = tk.Frame(root, padx=20, pady=20)
        options_frame.grid(row=1, column=0)

        # Checkbuttons for options
        self.sugar_var = tk.IntVar()
        sugar_check = tk.Checkbutton(options_frame, text="Sugar", variable=self.sugar_var)
        sugar_check.grid(row=0, column=0)

        self.milk_var = tk.IntVar()
        milk_check = tk.Checkbutton(options_frame, text="Milk", variable=self.milk_var)
        milk_check.grid(row=0, column=1)

        # Button to confirm and display message
        confirm_button = tk.Button(root, text="Confirm", command=self.display_message)
        confirm_button.grid(row=2, column=0, pady=10)

    def display_message(self):
        coffee_choice = self.coffee_var.get()
        sugar_choice = "with Sugar" if self.sugar_var.get() else "without Sugar"
        milk_choice = "with Milk" if self.milk_var.get() else "without Milk"

        message = f"You selected {coffee_choice} {sugar_choice} {milk_choice}."

        # Display message using messagebox
        messagebox.showinfo("Order Summary", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeVendingMachine(root)
    root.mainloop()