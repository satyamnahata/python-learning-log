#What is a Series?
"""A Pandas Series is like a column in a table.
It is a one-dimensional array holding data of any type."""

# Importing the pandas library1
import pandas as pd
students = pd.Series(['Alice', 'Bob', 'Charlie'], index=['s1', 's2', 's3'])
print(students)

#this will print the Series with custom indices
# Output:
# s1      Alice
# s2        Bob
# s3    Charlie
# dtype: object
print(students['s2'])  # Accessing a specific student's name using index
# Output: Bob
print(students[['s1', 's3']])  # Accessing multiple students using
# their indices
# Output:
# s1      Alice
# s3    Charlie
# dtype: object
print(students.index)  # Displaying the indices of the Series
# Output: Index(['s1', 's2', 's3'], dtype='object)

print(students.values)  # Displaying the values of the Series
# Output: array(['Alice', 'Bob', 'Charlie'], dtype=object)    
#           
print(students.name)  # Displaying the name of the Series
# Output: None (since we haven't set a name for the Series)

students.name = 'Student Names' # Setting a name for the Series

print(students.name)  # Displaying the name of the Series after setting it
# Output: Student Names

print(students)  # Displaying the Series after setting the name
# Output:
# s1      Alice
# s2        Bob
# s3    Charlie
# Name: Student Names, dtype: object

print(students.to_frame())  # Converting the Series to a DataFrame
# Output:
#            0
# s1      Alice
# s2        Bob
# s3    Charlie
# Name: Student Names, dtype: object

print(students.to_frame(name='Name'))  # Converting to DataFrame with a specific column name
# Output:
#            Name
# s1      Alice
# s2        Bob
# s3    Charlie
# Name: Student Names, dtype: object



#This code will help u understand how to create a series in pandas
# and how to access its elements, indices, values, and name.
# It also demonstrates how to convert a Series to a DataFrame.
# The outputs are shown as comments next to the print statements.
# You can run this code in a Python environment with pandas installed to see the results.
# Make sure to have pandas installed in your environment.