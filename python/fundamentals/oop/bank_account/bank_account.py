class BankAccount:
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance    
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if (self.balance - amount >=0):
                self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        self.balance = self.balance * self.interest_rate
        return self

matt_acc = BankAccount(.01, 100)
abby_acc = BankAccount(.5, 220)

matt_acc.deposit(50).deposit(100).withdraw(10).yield_interest().display_account_info()
abby_acc.deposit(1000).deposit(1).withdraw(20).withdraw(10000).withdraw(1).withdraw(1).yield_interest().display_account_info()