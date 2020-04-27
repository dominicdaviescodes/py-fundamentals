"""
Strict
some languages make you define vars and their types before you use them
can't change type later from a string to an integer
fewer suprises later!

Python - more relaxed (flexable)
we declare and use a var at the same time
interpreter figures out the type based on the value we provide
can change type later.

"""

# can change type later in python
cookies = 'Sugar'
print(cookies)
print(type(cookies))

cookies = 1
print(cookies)
print(type(cookies))

Cookies = 3
print(Cookies)
print(cookies)

# variable names are case sensitive are 2 different locations in memory

first_name = "Jeff"
print(first_name)

first_Name = "Sara"
print(first_name)
