# Chapter 6 Exercise 4: Line graph

import tkinter as tk

def draw_line(canvas, start, end, color, width):
    # Draw a line from start to end
    line = canvas.create_line(start[0], start[1], end[0], end[1], fill=color, width=width)

def draw_dotted_line(canvas, points, color, width, dash):
    # Draw a dotted line through the specified points
    dotted_line = canvas.create_line(*points, fill=color, width=width, dash=dash)

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=600)
    canvas.pack()

    # Draw a solid line from (1, 2) to (6, 8)
    draw_line(canvas, (100, 200), (300, 400), "blue", 2)

    # Draw a dotted line from (1, 3) to (2, 8) then to (6, 1) and finally to (8, 10)
    draw_dotted_line(canvas, [200, 300, 250, 400, 300, 100, 400, 500], "red", 4, (5, 5))

    root.mainloop()

if __name__ == "__main__":
    main()
