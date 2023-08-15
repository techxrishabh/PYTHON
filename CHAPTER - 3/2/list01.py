'<<<<<<<<<<<<<MODIFYING, ADDING AND REMOVING ELEMENTS IN LISTS>>>>>>>>>>>'

"========= Modifying Elements In A List =============="

motorcycles = ['Honda', 'Yamaha', 'Suzuki', 'Hayabusa']
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)

"Adding elements to the list"

"======== appending(means add) elements to the end of list ============"

motorcycles.append('pulser')
print(motorcycles)

cars = []

print(cars)

cars.append('Bugati')
cars.append('Ford')
cars.append('Audi')

print(cars)

'Inserting an elements into a list by using its index no. from where we want'

onePiece = ['Luffy', 'Nami', 'Sanji']
print(onePiece)
print(onePiece[2])
onePiece.insert(2, 'Brook')
print(onePiece[2])
print(onePiece)

'We can also remove an item from array by using del statement'

animals = ['Elephant', 'Lion', 'Tiger', 'Crockodile']
del animals[2]
print(animals)
