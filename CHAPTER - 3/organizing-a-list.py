''':::::::::::::::::::::::::::::::: ORGANIZING A LIST :::::::::::::::::::::::::::::::::::::'''

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

"""We can organize it alphabetically by using sort() method permanently, and we can never revert to the original order again """

cars.sort()
print(cars)

'''We can also reverse this list by passing the argument reverse=True in sort() method'''

cars.sort(reverse=True)
print(cars)


'''We can sorted a list temporarily with the sorted() Function'''

laptopBrands = ['hp', 'samsung', 'lenovo', 'asus', 'acer', 'msi']

'1. Here is the original list of what we want to print'
print('Here is the original list:')
print(laptopBrands)

'2. Here is the sorted list which we sorted by using sorted method'
print('\nHere is the sorted list:')
print(sorted(laptopBrands))

'3. Here is again the original list which we wanted to print at the first place'
print('\nHere is the original list again:')
print(laptopBrands)


'We can reverse the order of a list by using reverse() method'
laptopBrands.reverse()
print(laptopBrands)

'''NOTES: The reverse() method changes the order of a list permanently, but you
can revert to the original order anytime by applying reverse() to the same
list a second timeThe reverse() method changes the order of a list permanently, but you
can revert to the original order anytime by applying reverse() to the same
list a second time. '''


'''We can find this length by using the len() function'''


print(len(laptopBrands))

'''Python counts the items in a list starting with one, so you shouldn’t run into any
off-by-one errors when determining the length of a list'''
