"::::::::::::::::::: INTRO TO NUMBERS ::::::::::::::::::::"


''' ========================== Underscores in Numbers ====================== '''


'''When you’re writing long numbers, you can group digits using underscores
to make large numbers more readable:

>>> universe_age = 14_000_000_000

When you print a number that was defined using underscores, Python
prints only the digits:

>>> print(universe_age)
14000000000'''


'''============================ Constants ==================================

A constant is a variable whose value stays the same throughout the life of a
program. Python doesn’t have built-in constant types, but Python program-
mers use all capital letters to indicate a variable should be treated as a con-
stant and never be changed:


MAX_CONNECTIONS = 5000'''


''' :::::::::::::::::::::::::::::::::: EXERCISES ::::::::::::::::::::::::::::::::::::: '''

'''======= 2-9. Number Eight: Write addition, subtraction, multiplication, and division
operations that each result in the number 8. Be sure to enclose your operations
in print() calls to see the results. You should create four lines that look like this:'''

'''addition'''

print(5 + 3)

'''substraction'''

print(11 - 3)

'''multiplication'''

print(4 * 2)

'''division'''

print(16/2)

'''2-10. Favorite Number: Use a variable to represent your favorite number. Then,
using that variable, create a message that reveals your favorite number. Print
that message
'''
favouritenumber = 10
print(favouritenumber)
