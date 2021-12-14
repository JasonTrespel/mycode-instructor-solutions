#!/usr/bin/env python3

# another example of if block
# define list of grades
grades = [99, 88, 77, 66, 55, 44, 101]

# create for loop for all grades
for g in grades:
    print(g, end=" - You ")
    if g > 100:
        print("cheater")
    elif g > 60:
        print("passed")
    else:
        print("dummy")
