#!/usr/bin/env python3

# creating a basic for loop
# a for loop will iterate across all items in a list/dictionary/tuple

# start with a list of pet names
petlist = ["Fluffy", "Garfield", "Snowball", "Oliver"]

# loop across list
for pets in petlist:
    print(petlist)

# change list to change loop
petlist = ["Oliver", "Garfield", "Poofy"]

for pets in petlist:
    print(petlist[1])

print(petlist[2])
