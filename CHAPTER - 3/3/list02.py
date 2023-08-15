'<<<:::::::::::: REMOVING AN ITEM USING POP() METHOD ::::::::::::>>>>>>>>'


'''The pop() method removes the last item in a list, but it lets you work
with that item after removing it.'''


'INPUT'

'1.'
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

'2.'
popped_motorcycle = motorcycles.pop()

'3.'
print(motorcycles)

'4.'
print(popped_motorcycle)


'''We start by defining and printing the list motorcycles 1. Then we pop a
value from the list, and assign that value to the variable popped_motorcycle 2.
We print the list 3 to show that a value has been removed from the list.
Then we print the popped value 4 to prove that we still have access to the
value that was removed.
The output shows that the value 'suzuki' was removed from the end of
the list and is now assigned to the variable popped_motorcycle:'''

'OUTPUT'

'''['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki'''


'''we can also pop the elements of an array by using the index value'''

pokemon = ['pikachu', 'richu', 'balbasaur', 'dragonite']

popped_pokemon = pokemon.pop(2)

print(popped_pokemon)


'''We can also remove any items from an array by using its value with the help of remove method'''

flowers = ['rose', 'lily', 'sunflower', 'daffodil']

flowers.remove('rose')

print(flowers)
