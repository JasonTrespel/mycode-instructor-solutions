#!/usr/bin/env python3

car = {"make": "ferrari", "model": "fancy", "year": 2007, "color": "red", "purchase_price": 199000}

# print the purchase_price
print(car['purchase_price'])

# print the color, year, make
print(car['color'], car['year'], car['make'])

# add a new key-value pair to the dict
car['street_cred'] = "over 9000"

print(car)
# {"make": "ferrari", "model": "fancy", "year": 2007, "color": "red", "purchase_price": 199000, "street_cred": "over 9000"}

# update a key-value pair with the .update method   (give it a paint job)
car.update({"color": "metallic gold"})
print(car)
# {"make": "ferrari", "model": "fancy", "year": 2007, "color": "metallic gold", "purchase_price": 199000, "street_cred": "over 9000"}

# OR update the key's value directly
car["color"] = "neon pink"
print(car)
# {"make": "ferrari", "model": "fancy", "year": 2007, "color": "neon pink", "purchase_price": 199000, "street_cred": "over 9000"}
