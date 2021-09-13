#!/usr/bin/python3

"""Dictionary examples"""

# a dictionary is made up of key-value pairs
# a key must be a string or a variable that resolves to a string
# A value may be any valid pythonic type, including: str, int, float, list, dict and more!

def main():
    # starting off with a blank dictionary of pets
    pets = {}

    # one way to add or update existing key-value pairs to a dictionary
    pets.update({"dogs": ["Toto"]})
    print(pets)

    pets["cats"] = ["fluffy", "snowball"]
    print(pets)
    
    pets["fish"] = "Dorothy"
    print(pets)
    
    print(pets["dogs"][0])


if __name__ == "__main__":
    main()
