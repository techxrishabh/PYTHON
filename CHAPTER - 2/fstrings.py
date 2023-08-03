"::::::::::::::: USE OF FSTRINGS IN PYTHON ::::::::::::::::"

"""Lets see how String looks without using f string >>>>>>>>>>"""

name = 'Rishabh'
age = 18
height = '1.6'

"Without using fstrings >>>>>>>>>>>>>"

print("My name is", name, "I am", age, "Years old",
      "My height is", height, "meters")

"With fstrings >>>>>>>>>>>"

print(
    f"My name is {name} and I am {age} years old and My height is {height} meters")

'''We can also use expressions like multiplication, division etc by using fstrings >>>>>>>>>>>>>>>>> '''

print(
    f"My name is {name} and I am {age*2} years old and My height is {height} meters")
