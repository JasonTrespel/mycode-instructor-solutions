#!usr/bin/env python3

## Creating for loop to display farms to stdout

# this is the data we want to loop across
# it is a list containing 3 dictionaries

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# loop across one of the lists
for f in farms:
    print("
