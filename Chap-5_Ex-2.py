# Chapter 5 Exercise 2: Student Class

import tkinter as tk

class Students:
    def __init__(self, name, mark1, mark2, mark3):
        # Constructor to initialize student attributes
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calcGrade(self):
        # Method to calculate the average grade
        return (self.mark1 + self.mark2 + self.mark3) / 3

    def display(self):
        # Method to display student information
        average = self.calcGrade()
        return f"Student Name: {self.name}\nAverage Grade: {average:.2f}"

class StudentsGUI(tk.Tk):
    def __init__(self):
        # GUI constructor
        super().__init__()
        self.title("Students Information")
        self.geometry("300x200")
        self.create_student_objects()

    def create_student_objects(self):
        # Method to create GUI components
        self.label = tk.Label(self, text="Student Information will be displayed here.")
        self.label.pack()

        input_button = tk.Button(self, text="Enter Student Information", command=self.get_student_info)
        input_button.pack()

    def get_student_info(self):
        # Method to get student information and display it
        try:
            name = input("Enter Student Name: ")
            mark1 = int(input("Enter Mark 1: "))
            mark2 = int(input("Enter Mark 2: "))
            mark3 = int(input("Enter Mark 3: "))

            student = Students(name, mark1, mark2, mark3)

            self.label.config(text=student.display())
        except ValueError:
            print("Invalid input for marks. Please enter numerical values.")

# Instantiate the StudentsGUI class
app = StudentsGUI()
app.mainloop()
