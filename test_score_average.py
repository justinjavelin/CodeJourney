# This program finds the average of three test scores based off the input
# function, with user input as a float value instead of an integer.
# Get three test scores and assign them to the
# test1, test2, and test3 variables.
# For a simpler output, an f-string is used with .2 as a precision
# designator to round repeating decimal float values to two decimal places.

test1 = float(input('Enter the first test score: '))
test2 = float(input('Enter the second test score: '))
test3 = float(input('Enter the third test score: '))

# Calculate the average of the three scores
# and assign the result to the average variable.

average = (test1 + test2 + test3) / 3.0

# Display the average.

print(f'The average score is {average: .2f}.')
