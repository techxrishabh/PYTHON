# =============== TRY IT YOURSELF =================

# QUESTIONS__________________________________________

'''4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.
4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing CTRL-C or by closing the output window.)
4-5. Summing a Million: Make a list of the numbers from one to one million, and
then use min() and max() to make sure your list actually starts at one and ends
at one million. Also, use the sum() function to see how quickly Python can add
a million numbers.
4-6. Odd Numbers: Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20. Use a for loop to print each number.
4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to
print the numbers in your list.
4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.
4-9. Cube Comprehension: Use a list comprehension to generate a list of the first
10 cubes.'''

# ANSWERS__________________________________________
# print('printing numbers from 1 to 20')
# for value in range(1, 21):
#     print(value)


# print('from one to one million')
# numbers = list(range(1, 1000001))
# for number in numbers:
#     print(number)


# number1 = list(range(1, 1000001))
# print(min(number1))
# print(max(number1))
# print(sum(number1))

'''odd numbers'''
for odd_numbers in range(1, 21, 2):
    print(odd_numbers)

for multipleof3 in range(3, 31, 3):
    print(multipleof3)


for value in range(1, 11):
    print(value**3)

cube = [value**3 for value in range(1, 11)]
print(cube)
