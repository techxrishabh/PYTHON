'''================== Changing Case in a String with Methods ==============='''

name = "rishabh kumar"
print(name.title())

'''========= Using Variables in Strings ============'''

first_name = "rishabh"
last_name = "kumar"
full_name = f"{first_name} {last_name}"
print(full_name.title())

'''========== inserting a variable’s value into a string by placing the letter f ("These strings are called f-strings. The f is for format, because Python formats the string by replacing the name of any variable in braces with its value")'''

first_name = "Rishabh"
last_name = "Kumar"
full_name = (f"Hello, {first_name} {last_name}")
print(full_name.lower())

'''=========== Stripping Whitespace [ to remove the spaces in strings we use strip() method ]============='''

my_full_name = ' Rishabh Kumar '
'''without rstrip method'''

print(my_full_name)

'''with rstrip method'''

print(my_full_name.strip())

my_full_name1 = ' Rishabh Kumar '

''' === we can also use lstrip method to remove whitespaces of only left side === '''

print(my_full_name1.lstrip())

''' === we can also use rstrip method to remove whitespaces of only left side === '''

print(my_full_name1.rstrip())

''' ========== Removing prefixes =========== '''

my_url = "https://www.google.com"
my_simple_url = print(my_url.removeprefix("https://"))


'''T0 prinnnt quote we need to use this special tag called apostrophe [ ' ]'''

'''quotes of the famous personn'''

quote = 'Albert Einstein once said, “A person who never made a mistake never tried anything new.”'
print(quote)


''' ::::::::::::::::::::::::::::::::::::::::: EXERCISES :::::::::::::::::::::::::::::::::::::::: '''


'''2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never
tried anything new.”'''


'''2.6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous
person’s name using a variable called famous_person. Then compose your mes-
sage and represent it with a new variable called message. Print your message.'''

quote = 'Albert Einstein once said, “A person who never made a mistake never tried anything new.”'
famous_person = "- albert Einstein"

message = f"{quote} {famous_person}"
print(message)

'''2-7. Stripping Names: Use a variable to represent a person’s name, and
include some whitespace characters at the beginning and end of the name.
Make sure you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().'''

'''We can use /t for tab space and /n for new line'''

print("Line 1\tIndented\nLine 2\tIndented\nLine 3\tIndented")

person_name1 = '  Priyanshu Kumar  '
print(person_name1.strip())

'''2-8. File Extensions: Python has a removesuffix() method that works exactly
like removeprefix(). Assign the value 'python_notes.txt' to a variable called
filename. Then use the removesuffix() method to display the filename without
the file extension, like some file browsers do.'''

filename = 'python_notes.txt'
print(filename.removesuffix(".txt"))


''' :::::::::::::::::::::::::: STRINGS DONE WITH EXERCISES ::::::::::::::::::::::::::::::::::: '''

'''>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''
