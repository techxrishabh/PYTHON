# ========================= WORKING WITH LIST ===========================

'''Looping >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

'''naming conventions
for cat in cats:
for dog in dogs:
for item in list_of_items:
we can create the loops like this
'''

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"i can wait to see your next trick, {magician}.\n")
