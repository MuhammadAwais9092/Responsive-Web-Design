# Chapter 6 Exercise 2: Numpy Array

import numpy as np

# Given array
a = np.array([20, 23, 82, 40, 32, 15, 67, 52])

# Find the indices of even numbers
even_indices = np.where(a % 2 == 0)
print(f"Indices of even numbers: {even_indices}")

# Sort the array
sorted_array = np.sort(a)
print(f"Sorted array: {sorted_array}")

# Slice elements from index 3 to the end of the array
slice_1 = a[3:]
print(f"Slice from index 3 to the end: {slice_1}")

# Slice elements from index 0 to index 4
slice_2 = a[:5]
print(f"Slice from index 0 to index 4: {slice_2}")

# Print [32 15 67] using negative slicing
negative_slice = a[-5:-2]
print(f"Negative slicing to get [32 15 67]: {negative_slice}")
