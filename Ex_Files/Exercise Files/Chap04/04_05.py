# Challenge


"""
Guessing Game.

Ask user " What's my favourite food?

if enters correctly, output "Yep! So amazing!"

If incorrect, output "Yuck! That's not it!"

Regardless of what entered value is, output: "Thanks for playing!"
"""
fave_food = "chocolate"

guess = input("What's my favourite food?")


if guess == fave_food:
    print("Yep! So amazing!")
else:
    print("Yuck! That's not it!")
print("Thanks for playing!")
