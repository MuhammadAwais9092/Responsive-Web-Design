# Chapter 4 Exercise 5: Password Check

import tkinter as tk
from tkinter import messagebox
import re

class PasswordValidatorApp:
    def __init__(self):
        self.attempts_left = 5

        self.root = tk.Tk()
        self.root.title("Password Validator")
        self.root.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter Password:").pack(pady=10)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=10)

        validate_button = tk.Button(self.root, text="Validate Password", command=self.validate_password)
        validate_button.pack(pady=10)

    def validate_password(self):
        password = self.password_entry.get()

        if self.is_valid_password(password):
            messagebox.showinfo("Password Valid", "Password is valid!")
            self.root.destroy()  # Close the application if the password is valid
        else:
            self.attempts_left -= 1
            if self.attempts_left > 0:
                messagebox.showwarning("Invalid Password", f"Invalid password! {self.attempts_left} attempts left.")
            else:
                messagebox.showerror("Alert!", "Authorities have been alerted! Too many failed attempts.")
                self.root.destroy()

    def is_valid_password(self, password):
        # Password criteria
        if (
            re.search("[a-z]", password)
            and re.search("[0-9]", password)
            and re.search("[A-Z]", password)
            and re.search("[$#@]", password)
            and 6 <= len(password) <= 12
        ):
            return True
        else:
            return False

    def run(self):
        self.root.mainloop()

# Instantiate the PasswordValidatorApp class
app = PasswordValidatorApp()
app.run()
