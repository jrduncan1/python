class BankAccount:

    def __init__(self, int_rate, balance=0):
        self.int_rate = 0.0325
        self.acct_balance = balance

    def deposit(self, amount):
        self.acct_balance += amount
        return self
    
    def withdraw(self, amount):
        if self.acct_balance < amount:
            print("Insufficient funds for withdrawal: Charing a $5 fee")
            self.acct_balance -= 5 + amount
        else:
            self.acct_balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Account Balance is ${self.acct_balance}")
        return self
    
    def yield_interest(self):
        if self.acct_balance >= 0:
            self.acct_balance *= self.int_rate + 1
        else:
            print("Insufficient funds for interest yield: No interest earned")
        return self

investment = BankAccount('0.0325', 500000)
checking = BankAccount('0.0325', 90)

investment.deposit(5000).deposit(300).deposit(40).withdraw(800).yield_interest().display_account_info()
checking.deposit(900).deposit(20).withdraw(700).withdraw(5).withdraw(5).withdraw(500).yield_interest().display_account_info()