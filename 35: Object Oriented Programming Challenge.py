class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance = amount + self.balance
        print(f"Deposit accepted! \nYour new balance is {self.balance}\n")
    def withdraw(self, amount):
        if not amount > self.balance:
            self.balance = self.balance - amount
            print(f"Withdrawal accepted! \nYour new balance is {self.balance}\n")
        else:
            print("Funds unavailable! \nSorry, the amount you want to withdraw exceeds your available balance!")
    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: {self.balance}\n"


acct1 = Account('Jose', 100)
print(acct1)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
