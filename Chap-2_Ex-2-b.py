# Chapter 2 Exercise 2 b: Square Grid

import tkinter as tk

def create_square_grid():
    root = tk.Tk()
    root.title("Square Grid with Labels")

    # Create frames with a border of 5
    frame_left = tk.Frame(root, bd=5)
    frame_right = tk.Frame(root, bd=5)

    # Create labels for the frames
    label_a = tk.Label(frame_left, text="A", padx=10, pady=5, bd=5, relief=tk.GROOVE, bg="#2f2e42", fg="white")
    label_b = tk.Label(frame_left, text="B", padx=10, pady=5, bd=5, relief=tk.GROOVE, bg="white")
    label_c = tk.Label(frame_right, text="C", padx=10, pady=5, bd=5, relief=tk.GROOVE, bg="white")
    label_d = tk.Label(frame_right, text="D", padx=10, pady=5, bd=5, relief=tk.GROOVE, bg="#2f2e42", fg="white")

    # Pack labels with expand and fill options
    label_a.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    label_b.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
    label_c.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    label_d.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    # Pack frames with a border of 5, expand, and fill options
    frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    frame_right.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    root.mainloop()

# Call the function to create the square grid
create_square_grid()