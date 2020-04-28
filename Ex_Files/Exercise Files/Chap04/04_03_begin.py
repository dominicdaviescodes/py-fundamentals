"""
if-else statement
add more flexability. so far if condition is false nothing happens.

if condition:
    do work
else:                           # else clause
    do something else

if 5 > 6:
    print("5 is greater than 6. Weird!")  # skips this
else:
    print("5 is not greater than 6")

"""


plant = "Cacti"

if plant == "Cacti":
    print(plant, "don't need a lot of water")
else:
    print(plant, "love water")

print("Thanks!")   # regardless of the value of the variable we always print thanks
