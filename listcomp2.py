import numbers
#// python list comprehension to print the square root of numbers in a list from 1 to 10

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# square root of numbers in a list from 1 to 10
sqr = [x**2 for x in numbers]
print(sqr)

#// python list comprehension to print the square root of odd numbers in a list from 1 to 10

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# square root of numbers in a list from 1 to 10

sqr = [x**2 for x in numbers1 if x%2 != 0]
print(sqr)

