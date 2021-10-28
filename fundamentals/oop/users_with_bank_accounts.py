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


class User:
    def __init__(self, name, type):
        self.name = name
        self.account = {type: BankAccount(int_rate = 0.0325, balance = 0)}
        self.type = type

    def make_deposit(self, amount, type):
        self.account[type].deposit(amount)
        return self
    
    def make_withdrawl(self, amount, type):
        self.account[type].withdraw(amount)
        return self
    
    def display_user_balance(self, type):
        print(f"{self.name}'s {self.type} account balance: ${self.account[type].acct_balance}")
        return self

    def establish_new_account(self, type):
        if type not in self.account:
            self.account[type] = BankAccount(int_rate = 0.0325, balance = 0)
        else:
            print('Account already exists.')

    # def transfer_money(self, name, amount):
    #     self.account -= amount
    #     self.receipient = name
    #     self.receipient.account += amount
    #     return self

steve = User("Steve", "investment")

steve.make_deposit(100, "investment").make_withdrawl(150, "investment").display_user_balance("investment")

steve.establish_new_account("business")

steve.make_deposit(5000, "business").display_user_balance("business") # need to determine how to print the correct acct name when using different account types

