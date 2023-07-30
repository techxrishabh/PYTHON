'''================== Changing Case in a String with Methods ==============='''

name = "rishabh kumar"
print(name.title())

'''========= Using Variables in Strings ============'''

first_name = "rishabh"
last_name = "kumar"
full_name = f"{first_name} {last_name}"
print(full_name.title())

'''========== insertig a variable’s value into a string by placig the letter f ("These strings are called f-strings. The f is for format, because Python formats the string by replacing the name of any variable in braces with its value")'''

first_name = "Rishabh"
last_name = "Kumar"
full_name = (f"Hello, {first_name} {last_name}")
print(full_name.lower())

'''=========== Stripping Whitespace (to remove the space in strings we use strip() method )============='''

my_full_name = ' Rishabh Kumar '
'''without rstrip method'''

print(my_full_name)

'''with rstrip method'''

print(my_full_name.strip())

'''quotes of the famous personn'''
