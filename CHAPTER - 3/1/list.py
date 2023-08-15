
":::::::::::::::: INTRODUCTION OF LISTS :::::::::::::::::::"

bicycle = ['trek', 'redline', 'specialized', 'cannondale']
print(bicycle)

'''Index position always start at o, not 1'''

print(bicycle[0])
print(bicycle[0].title())

'''We can access the last item by using negative value'''

print(bicycle[-1])

'''Making strings by using list'''

message = f"my first bicycle was a {bicycle[3].title()}"

print(message)


" <<<<<<<<<<::::::::::::::::::::: EXERCISES ::::::::::::::::::::>>>>>>>>"

'''
                           TRY IT YOURSELF


Try these short programs to get some firsthand experience with Python’s lists.
You might want to create a new folder for each chapter’s exercises, to keep
them organized.
3-1. Names: Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time.
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each mes-
sage should be the same, but each message should be personalized with the
person’s name.
3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”'''


"Solution"

name = ['Rishabh', 'Priyanshu', 'Manish', 'Rishu']

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(f"Hello there {name[0]}, How are you?")
print(f"Hello there {name[1]}, How are you?")
print(f"Hello there {name[2]}, How are you?")
print(f"Hello there {name[3]}, How are you?")
