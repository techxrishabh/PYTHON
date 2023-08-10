'''=================== Looping - Making numerical lists in python ======================'''

for value in range(1, 5):
    print(value)

'''In this example, range() prints only the numbers 1 through 4. This is
another result of the off-by-one behavior you’ll see often in programming
languages. The range() function causes Python to start counting at the first
value you give it, and it stops when it reaches the second value you provide.
Because it stops at that second value, the output never contains the end
value, which would have been 5 in this case.
To print the numbers from 1 to 5, you would use range(1, 6):'''

print('This time the output starts at 1 and ends at 5')
for value in range(1, 6):
    print(value)

''':::::::::::::::::::::::: Using range() to Make a List of Numbers :::::::::::::::::::::::'''
print("making a list of number by using list")
numbers = list(range(1, 6))
print(numbers)


'''If you pass a third argument to range(), Python uses that value
as a step size when generating numbers.'''

print('here’s how to list the even numbers between 1 and 10')

even_numbers = list(range(1, 11, 2))
print(even_numbers)
