# return is a key word
def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance

# because we want to use the value later save in a variable
balance = withdraw_money(100, 80)

if (balance <= 50):
    print("We need to make a deposit")
else:
    print("Nothing to see here!")
