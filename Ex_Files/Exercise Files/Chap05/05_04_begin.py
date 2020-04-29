# Return a value.  When we need something back
# keyword is used to send back values from a Python function.

def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        print("The balance is", current_balance)


withdraw_money(100, 80)  # 20

