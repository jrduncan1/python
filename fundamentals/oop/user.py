class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"{self.name}'s balance: ${self.account_balance}")
        return self

    def transfer_money(self, name, amount):
        self.account_balance -= amount
        self.receipient = name
        self.receipient.account_balance += amount
        return self

max = User("Max")

jon = User("Jon")

wei = User("Wei")

max.make_deposit(100).make_deposit(500).make_deposit(0.90).make_withdrawl(20).display_user_balance()

jon.make_deposit(2500).make_deposit(20).make_withdrawl(900).make_withdrawl(35).display_user_balance()

wei.make_deposit(500000000).make_withdrawl(5).make_withdrawl(5).make_withdrawl(7).display_user_balance()

max.transfer_money(wei, 400).display_user_balance()
wei.display_user_balance()

