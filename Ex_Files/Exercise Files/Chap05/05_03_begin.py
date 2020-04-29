# provide different outputs for some users based on input

# amount_paid here is a parameter


def wash_car(amount_paid):
    if (amount_paid == 12):
        # steps for platinum wash $12
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")

    if (amount_paid == 6):
        # steps for basic wash $6
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry")


# the values we give to our functions are the arguments - in the function call
# function_call(argument)
wash_car(12)
