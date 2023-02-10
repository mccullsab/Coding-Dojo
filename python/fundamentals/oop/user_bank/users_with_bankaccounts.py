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
    
class User:
    def __init__(self, first_name):
        self.first_name = first_name
        self.account = BankAccount(interest_rate = .01, balance = 20)
        self.accounts = []
        self.accounts.append(self.account)

    # def add_account(self):

    def make_deposit(self, amount):
        self.account.deposit(amount)
        # print(self.account.balance)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self


abby = User("Abby")
print(abby.make_deposit(100).display_user_balance())
    

