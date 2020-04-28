"""
If Statements:

if condition      
    do work
end if

if true it runs the code if not it gets ignored and keeps interpreting line by line.

we always make decisions based on current conditions.

if it's raining, take an umbrella.
if you're tired, grab a cup of coffee

Examples here show 1 path, line by line, next chapter we will write more interesting programs

"""
# indentations is important
# only 1 statement in our block
if 5 < 6:
    print("Yes, 5 is less than 6.")

# a block ends when line is not indented any more. will get error if not indented properly (4 spaces!)
if 5 < 6:
    print("Yes, 5 is less than 6.")  # in the if block
    print("Everyone knows that!.")   # in the if block
print("I'm not in the block")

# Example

print("Hi!")

name = input("What's your name? ")
print("It's nice to meet you,", name)

answer = input("Are you enjoying the course? ")

if answer == "Yes":
    # this line is ignored if don't type Yes
    print("That's good to hear!")

print("Final statement")
