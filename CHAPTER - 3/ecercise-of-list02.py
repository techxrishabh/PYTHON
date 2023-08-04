'''<<<<<<<<<<<::::::::::::::::: EXERCISES ::::::::::::::::::::>>>>>>>>>'''

'''3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.'''

myGuest = ['Manish', 'Priyanshu', 'Rishu', 'Vikash', 'Saurav']

print(
    f"hey there {myGuest[0]}, i would like you to come to my birthday party.")
print(
    f"hey there {myGuest[1]}, i would like you to come to my dinner party.")
print(
    f"hey there {myGuest[2]}, i would like you to come to my dinner party.")
print(
    f"hey there {myGuest[3]}, i would like you to come to my dinner party.")
print(
    f"hey there {myGuest[4]}, i would like you to come to my dinner party.")


'''3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.

• Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in
your list.3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.'''

print(
    f"unfortunately our guest {myGuest[4]} could be able to make to the party..")

myGuest[4] = 'Sahil'
print(myGuest)

print(
    f"hey there {myGuest[0]}, i would like you to come to my birthday party.")
print(
    f"hey there {myGuest[1]}, i would like you to come to my dinner party.")
print(
    f"hey there {myGuest[2]}, i would like you to come to my dinner party.")
print(
    f"hey there {myGuest[3]}, i would like you to come to my dinner party.")
print(
    f"hey there {myGuest[4]}, i would like you to come to my dinner party.")

'''INVITING SOME MORE MEMBER TO THE PARTY SINCE I FIND A BIGGER TABLE'''

print(f"I would like to kindly inform you all that the party is going to be more bigger than usually planned since I found a bigger dinner Table")

myGuest.insert(0, 'Ashish')
print(myGuest)

myGuest.insert(3, 'Vicky')
print(myGuest)

myGuest.append('Happy')
print(myGuest)

print(f"{myGuest[0]}, every great party requires a professional entertainer. Since we can’t afford one, we have decided to invite you.")
print(f"{myGuest[1]}, every great party requires a professional entertainer. Since we can’t afford one, we have decided to invite you.")
print(f"{myGuest[2]}, every great party requires a professional entertainer. Since we can’t afford one, we have decided to invite you.")
print(f"{myGuest[3]}, every great party requires a professional entertainer. Since we can’t afford one, we have decided to invite you.")
print(f"{myGuest[4]}, every great party requires a professional entertainer. Since we can’t afford one, we have decided to invite you.")
print(f"{myGuest[4]}, every great party requires a professional entertainer. Since we can’t afford one, we have decided to invite you.")
print(f"{myGuest[5]}, every great party requires a professional entertainer. Since we can’t afford one, we have decided to invite you.")
print(f"{myGuest[6]}, every great party requires a professional entertainer. Since we can’t afford one, we have decided to invite you.")
print(f"{myGuest[7]}, every great party requires a professional entertainer. Since we can’t afford one, we have decided to invite you.")


print(f"We have just found that our new table wont be able to arrive on time and now i have the space of only 2 peoples sorry for the inconvenience")

popped_guest = myGuest.pop()
print(
    f"sorry {popped_guest} we couldnot be able to invite you anymore due to some issue")
popped_guest = myGuest.pop()
print(
    f"sorry {popped_guest} we couldnot be able to invite you anymore due to some issue")
popped_guest = myGuest.pop()
print(
    f"sorry {popped_guest} we couldnot be able to invite you anymore due to some issue")
popped_guest = myGuest.pop()
print(
    f"sorry {popped_guest} we couldnot be able to invite you anymore due to some issue")
popped_guest = myGuest.pop()
print(
    f"sorry {popped_guest} we couldnot be able to invite you anymore due to some issue")
popped_guest = myGuest.pop()
print(
    f"sorry {popped_guest} we couldnot be able to invite you anymore due to some issue")
print(myGuest)


'''Printing the members who are still invited'''

print(
    f"Hey there, {myGuest[0]} you are still invited..... please come to the dinner party")
print(
    f"Hey there, {myGuest[1]} you are still invited..... please come to the dinner party")

print(myGuest)

del myGuest[0]

print(myGuest)

del myGuest[0]

print(myGuest)

# We can calculate then length of a list by using len function ===============

print(len(myGuest))
