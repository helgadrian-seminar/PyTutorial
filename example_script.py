# This script covers the second half of what we'll be addressing in the elementary Python tutorial.

# Import packages
import numpy as np
import pandas as pd
#import maplotlib.pylot as plt

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
		break
	print(x)
else:
	print('x was divisible by 5')



