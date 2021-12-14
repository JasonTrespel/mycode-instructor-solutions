#!/usr/bin/env python3


cats = [{"name": "garfield", "age": 45}, {"name": "snowball", "age": 7}, {"name": "fluffy", "age": 2}]

print(cats)

for cat in cats:
    print(f"My cat named {cat['name']} is {cat['age']} years old.")
