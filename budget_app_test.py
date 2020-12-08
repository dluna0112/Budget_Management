#Import budget module
from Budget import Budget
# Date information to set month
import datetime
date = datetime.datetime.now()
month = (date.strftime("%B"))
year = (date.year)


#Introduction to program
print("Hello & welcome my name is 'Mafu'") # Money.Assistant.For.You
name = input("I can help you manage your monthly budget, but first can you tell me your name ")
print(f"Great nice to meet you {name}.")
budget_name = input("Now tell me what type of budget would you like to create ie; 'take-out','entertainment' etc... \n")
print("Perfect")
amount = float(input("Now please tell me the amount you would like to set your budget too: "))

while True:
    confirm = input(f"Lastly let's just confirm you would like to create a {budget_name} budget and set it to ${amount}  (y/n): ")
    if confirm.lower() == 'y':
        print(f"Your monthly {budget_name} budget for {month}-{year} is set to ${amount}")
        break
    else:
        change = input("Would you like to change the type of budget or amount: ")
        if change == 'budget':
            budget_name = input("What would you like to change the budget to: ")
            print(f"Your budget type has been changed to {budget_name}")
        elif change == 'amount':
            amount = input("What would you like to change the amount to: ")
            input(f"The amount for your budget has been changed to {amount}")
        else:
            print("Please only enter budget or amount")

budget_type = budget_name + 'budget'
budget_type = Budget(budget_name,amount)

print("List of available commands are")
print("""
    'Remainder' - Shows monthly spending remainder
    'Increase' - Increase monthly speding limit
    'Decrease' - Decrease monthly spending limit
    'Recent' - Shows last 3 purchases
    'Can I' - Ask if you can afford a purchased
    'Did I' - Check if you paid already""")
print("To see these again at anytime just type help")

budget_type.remainder()
budget_type.add_funds(10)
budget_type.add_purchase(30)
budget_type.remainder()
budget_type.can_i(200)