#!/usr/bin/env python3

# creating a basic for loop
# a for loop will iterate across all items in a list/dictionary/tuple

# start with a list of pet names
petlist = ["Fluffy", "Garfield", "Snowball", "Olvier"]

# loop across list
for pet in petlist:
    print(petlist)

# loop in a different way
for each in petlist:
    print(each)

# change list to change loop
petlist = ["Oliver", "Garfield", "Poofy"]

for pets in petlist:
    print("I have a pet named:" + pets)

