# Chapter 6 Exercise 5: Working with JSON File

import json

def write_to_json(filename, data):
    # Open the JSON file in write mode and use json.dump to write data to the file
    with open(filename, 'w') as file:
        json.dump(data, file)

def read_from_json(filename):
    # Open the JSON file in read mode and use json.load to read data from the file
    with open(filename, 'r') as file:
        data = json.load(file)
        return data

def main():
    # Task 1: Write to JSON file
    student_data = {}
    # Get input from the user for student name, ID, and course
    student_data['Name'] = input("Enter the student name: ")
    student_data['ID'] = int(input("Enter the student ID: "))
    student_data['Course'] = input("Enter the student course: ")

    # Append CourseDetails dictionary to student_data
    student_data['CourseDetails'] = {
        'Group': input("Enter the student group: "),
        'Year': int(input("Enter the student year: "))
    }

    # Call the write_to_json function to write data to the JSON file
    write_to_json('StudentJson.json', student_data)
    print("Details of the student are written to StudentJson.json")

    # Task 2: Read from JSON file
    # Call the read_from_json function to read data from the JSON file
    retrieved_data = read_from_json('StudentJson.json')

    print("\nDetails of the Student are")
    print(f"  Name: {retrieved_data['Name']}")
    print(f"  ID: {retrieved_data['ID']}")
    print(f"  Course: {retrieved_data['Course']}")

    # Display CourseDetails
    print("  CourseDetails:")
    print(f"    Group: {retrieved_data['CourseDetails']['Group']}")
    print(f"    Year: {retrieved_data['CourseDetails']['Year']}")

if __name__ == "__main__":
    main()
