#!/usr/bin/env python3


cats = [{"name": "garfield", "age": 45}, {"name": "snowball", "age": 7}, {"name": "fluffy", "age": 2}]

print(cats)

# an f string will make it easier to print out statements
for cat in cats:
    print(f"My cat named {cat['name']} is {cat['age']} years old.")

# without an f string this is what we would need to print for the same output
print("My cat named garfield is 45 years old.")
print("My cat named snowball is 7 years old.")
print("My cat named fluffy is 2 years old.")
