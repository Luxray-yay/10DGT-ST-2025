# Demonstrate how variable are created and hoe they work.
# Author: Elisabeta Bayer 
# Date: 19-09-2025
# Version 1.0

# Different types of variables
# Store a string 
greeting = "Hello World!" 
print(greeting)




















# Creating new variable
num_1 = 5
num_2 = 18

sum1 = 5 + 18 # This is not good practice
print(sum1)

sum1 = num_1 + num_2
print(sum1)

sum_string1 = "18"
sum_string2 = "5"

# Adding two strings together. This is called concatenation
sum = sum_string1 + sum_string2
print(sum)

# Print formatting. f stands for 'format' and insert the value of variales into curly brackets
print(f"My calculation for {num_1} and {num_2} together is {sum1}.")
