# Chapter 4 Exercise 3: Reading to a List

# Open the file in read mode
with open('numbers.txt', 'r') as file:
    # Read all lines from the file and convert each line to an integer
    numbers = [int(line.strip()) for line in file]

# Output the values in integer format
for number in numbers:
    print(number)
