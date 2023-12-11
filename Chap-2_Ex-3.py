# Chapter 2 Exercise 3: Login page

import tkinter as tk

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Basic authentication (replace with your actual authentication logic)
    if username == "admin" and password == "password":
        result_label.config(text="Login Successful", fg="green")
    else:
        result_label.config(text="Login Failed", fg="red")

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Create and place widgets using the Grid geometry manager
label_username = tk.Label(root, text="Username:")
label_password = tk.Label(root, text="Password:")
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")  # Show asterisks for password
login_button = tk.Button(root, text="Login", command=login)
result_label = tk.Label(root, text="", fg="black")

# Place widgets in the grid
label_username.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_username.grid(row=0, column=1, padx=10, pady=5)
label_password.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_password.grid(row=1, column=1, padx=10, pady=5)
login_button.grid(row=2, column=0, columnspan=2, pady=10)
result_label.grid(row=3, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
