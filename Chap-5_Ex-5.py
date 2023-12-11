# Chapter 5 Exercise 5: Playing around in class

import tkinter as tk

class Animal:
    def __init__(self, animal_type, name, color, age, weight, noise):
        # Initialize the Animal object with specified attributes
        self.animal_type = animal_type
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight
        self.noise = noise

    def sayHello(self):
        # Method to make the animal say hello
        return f"{self.name} says hello!"

    def makeNoise(self):
        # Method to make the animal produce its characteristic noise
        return f"{self.name} makes the noise: {self.noise}"

    def animalDetails(self):
        # Method to get a string representation of all details of the animal
        details = (
            f"Type: {self.animal_type}\n"
            f"Name: {self.name}\n"
            f"Color: {self.color}\n"
            f"Age: {self.age}\n"
            f"Weight: {self.weight} kg\n"
            f"Noise: {self.noise}"
        )
        return details

class AnimalGUI(tk.Tk):
    def __init__(self):
        # Initialize the AnimalGUI window
        super().__init__()
        self.title("Animal Information")
        self.geometry("400x300")
        self.create_animal_objects()

    def create_animal_objects(self):
        # Create instances of the Animal class
        dog = Animal("Dog", "Buddy", "Brown", 3, 10, "Woof")
        cow = Animal("Cow", "MooMoo", "Black and White", 5, 500, "Moo")

        # Create labels to display information for each animal
        dog_label = tk.Label(self, text=dog.animalDetails())
        dog_label.pack()

        cow_label = tk.Label(self, text=cow.animalDetails())
        cow_label.pack()

# Instantiate the AnimalGUI class
app = AnimalGUI()
app.mainloop()
