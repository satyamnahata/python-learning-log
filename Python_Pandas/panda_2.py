#What is a DataFrame?
"""A Pandas DataFrame is a 2 dimensional data structure, 
like a 2 dimensional array, or a table with rows and columns."""

import pandas as pd 

# Creating a DataFrame with custom indices
students_df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 21, 22],
    'Grade': ['A', 'B', 'C']
}, index=['s1', 's2', 's3'])
print(students_df)

# Output:
#          Name  Age Grade
# s1      Alice   20    A
# s2        Bob   21    B
# s3    Charlie   22    C

# Accessing a specific student's name using index
print(students_df.loc['s2', 'Name'])  # Accessing Bob's name
# Output: Bob 

# Accessing a specific student's age using index
print(students_df.loc['s1', 'Age'])  # Accessing Alice's age
# Output: 20

# Accessing multiple students using their indices
print(students_df.loc[['s1', 's3']])  # Accessing Alice and Charlie
# Output:
#          Name  Age Grade
# s1      Alice   20    A
# s3    Charlie   22    C       

print(students_df.index)  # Displaying the indices of the DataFrame
# Output: Index(['s1', 's2', 's3'], dtype='object)  

print(students_df.values)  # Displaying the values of the DataFrame
# Output:
# [['Alice' 20 'A']
#  ['Bob' 21 'B']
#  ['Charlie' 22 'C']]

print(students_df.columns)  # Displaying the column names of the DataFrame
# Output: Index(['Name', 'Age', 'Grade'], dtype='object')

print(students_df.shape)  # Displaying the shape of the DataFrame
# Output: (3, 3)  # 3 rows and 3 columns   

print(students_df.dtypes)  # Displaying the data types of each column
# Output:
# Name      object
# Age        int64
# Grade     object
# dtype: object 

# Setting a name for the DataFrame
students_df.name = 'Student Information'
print(students_df.name)  # Displaying the name of the DataFrame
# Output: Student Information
print(students_df)  # Displaying the DataFrame after setting the name
# Output:
#          Name  Age Grade
# s1      Alice   20    A
# s2        Bob   21    B
# s3    Charlie   22    C
# Converting the DataFrame to a Series
print(students_df['Name'])  # Converting the 'Name' column to a Series
# Output:
# s1      Alice
# s2        Bob
# s3    Charlie
# Name: Name, dtype: object         

# Converting the DataFrame to a Series with a specific column name
print(students_df['Name'].to_frame(name='Student Names'))  # Converting to DataFrame with a specific column name
# Output:
#            Student Names
# s1      Alice
# s2        Bob
# s3    Charlie
# Name: Name, dtype: object

# Converting the DataFrame to a Series with a specific index
print(students_df['Name'].to_frame(index=['s1', 's3']))
# Output:
#            Name
# s1      Alice
# s3    Charlie
# Name: Name, dtype: object

# Converting the DataFrame to a Series with a specific index and column name
print(students_df['Name'].to_frame(name='Student Names', index=['s1', 's3']))
# Output:
#            Student Names
# s1      Alice
# s3    Charlie
# Name: Name, dtype: object