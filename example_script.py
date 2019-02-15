# This script covers the second half of what we'll be addressing in the elementary Python tutorial.

# Import packages
import numpy as np
import pandas as pd
#import matplotlib.pylot as plt

# To add a directory to your path for this session only
# import sys; sys.path.append('path_to_directory')

# Basic loop syntax
print('Basic loop syntax')
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
for prime in primes:
	print(prime)

# Syntax using "range"
print('\nRange with a single input')
for x in range(5):
	print(x)
print('\nRange with a two inputs')
for x in range(3,6):
	print(x)
print('\nRange with a two inputs')
for x in range(3,6,2):
	print(x)

# While loops
print('\nWhile loop')
count = 0
while count < 5:
	print(count)
	count += 1

# Break statements
print('\nUsing a break statement ends the loop')
count = 0
while True:
	print(count)
	count += 1
	if count >= 5:
		break
print('\nUsing a continue statement ends only that iteration of the loop')
for x in range(10):
	if x%2 == 0:
		continue
	print(x)

# Else clause
print('\nIt is even possible to use else clauses with loops!')
for x in range(0,10):
	if x%5 == 0:
		continue
	print(x)
else:
	print('x was divisible by 5')

# ***** Classes and Objects *****
print('\nWe can define classes')
class MyClass:
	variable = 'MyVariable'
	def function(self):
		print('This is a test function')

myobject1 = MyClass()
myobject2 = MyClass()

myobject1.variable = 'AnotherVariable'

print(myobject1.variable)
print(myobject2.variable)

def myf(x):
    y = x+10
    z = x**2
    return y,z
myOutput = myf(2)
print(myOutput)

# ***** There are also fancy lists called "dictionaries" *****
dict = {"name": ["Bob", "Bruce", "Bill"],
       "grade": ["F", "F", "F-"]}
print(dict)

# ***** Now we'll look at Pandas *****
print('\nA simple dataframe')
studs = pd.DataFrame(dict)
print(studs)

# We can change the indices
print('\nChanging the indices')
studs.index = ['Bb', 'Br', 'Bl']
print(studs)

# We can read from a CSV as well
print('\nReading from a CSV')
ex_csv = pd.read_csv('example.csv')
print(ex_csv)

# To access parts of a dataframe:
print("\nSelect an entire column using df['col_name']")
print(studs['name'])
print("\nSelect several rows using df[start#:end#]")
print(studs[0:1])
print("\nSelect a row by its integer index using df.iloc[#]")
print(studs.iloc[2])
print("\nSelect a row by name using df.loc['name']")
print(studs.loc[['Bb']])

# Excel files can also be read
hsdt = pd.read_excel('pa_seamount_ages.xlsx',sheetname='Hawaii')