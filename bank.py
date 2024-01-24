class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Amount Withdrew:", amount)
        else:
            print("Insufficient funds")
    def display_balance(self):
       print("Available Balance:", self.balance)