#Create Budget class
class Budget():
    
    # print("""Available Commands Are:

    def __init__(self,budget_name,amount):
        self.budget_name = budget_name
        self.amount = amount

    def help(self):
    #Show available commands
        print("""
    'Remainder' - Shows monthly spending remainder
    'Increase' - Increase monthly speding limit
    'Decrease' - Decrease monthly spending limit
    'Recent' - Shows last 3 purchases
    'Can I' - Ask if you can afford a purchased
    'Did I' - Check if you paid already""")

    def remainder(self):
    #Shows remaining amount in monthly budget
        print(f"You have ${self.amount} left for this month")

    def add_funds(self,increase_amount):
        self.amount =  self.amount + increase_amount
        print(f"Your new budget amount is {self.amount}")

    def add_purchase(self,decrease_amount):
        purchases = []
        self.amount =  self.amount - decrease_amount
        print(f"Your new budget amount is {self.amount}")
        purchases.append(decrease_amount)
    
    def can_i(self,cost):
        if self.amount - cost > 0:
            print("Yes you can afford this")
        else:
            print("This would put you over your monthly spending limit")
    
    
    