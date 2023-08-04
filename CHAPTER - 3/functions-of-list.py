'''In Python, when working with lists, there are several built-in functions that you can use to perform various operations. These functions can be categorized into different types based on the actions they perform:

    Element Access:
        len(): Returns the number of elements in the list.
        index(): Returns the index of the first occurrence of a specified element in the list.
        count(): Returns the number of occurrences of a specified element in the list.

    Element Modification:
        append(): Adds an element to the end of the list.
        extend(): Extends the list by appending elements from another iterable.
        insert(): Inserts an element at a specified position in the list.
        remove(): Removes the first occurrence of a specified element from the list.
        pop(): Removes and returns the element at a specified index (by default, the last element).

    List Sorting and Reversal:
        sort(): Sorts the list in ascending order (in-place).
        sorted(): Returns a new sorted list without modifying the original list.
        reverse(): Reverses the elements of the list in-place.

    List Copy and Creation:
        copy(): Creates a shallow copy of the list (a new list with the same elements).
        list(): Converts an iterable (e.g., tuple, string) into a new list.'''


# QUESTION ===========================================

'''3-10. Every Function: Think of things you could store in a list. For example, you
could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items and
then uses each function introduced in this chapter at least once.'''

# SOLUTION =========================================

rivers = ['nile', 'ganga', 'yamuna', 'amazon', 'indus']
mountains = ['everest', 'fuji', 'rushmore', 'kangchenjunga', 'nanda devi']
countries = ['india', 'china', 'america', 'indoneia', 'pakistan']
cities = ['chennai', 'hydrabad', 'mumbai', 'bhopal', 'surat']
languages = ['hindi', 'english', 'chinese', 'french', 'japanese']
countries01 = ['french', 'sri-lanka', 'antartica', 'egypt', 'ukrain']

# len()
print("len() function ======")
print(len(rivers))

# index()
print(mountains.index('rushmore'))

# count()
print(rivers.count('ganga'))

# append(
countries.append('bhutan')
print(countries)

# extend()
countries.extend(countries01)
print(countries)

# insert()
languages.insert(4, 'koreans')
print(languages)

# remove
rivers.remove('ganga')
print(rivers)

# pop
mountains.pop()
mountains.pop()
mountains.pop()
mountains.pop()
print(mountains)

# sort()
rivers.sort()
print(rivers)

# sorted()
print(sorted(cities))


# reverse()
languages.reverse()
print(languages)

# copy()
# list()
