class BankAccount:
    def __init__(self, account_number):
        self.balance = 0.0
    def deposit(self):
        amount = float(input("Deposit an amount to the balance: "))
        self.balance += amount
        print("Amount Deposited:", amount)
    def withdraw(self):
        amount = float(input("Withdraw an amount from the balance: "))
        if self.balance >= amount:
            self.balance -= amount
            print("Amount Withdrew:", amount)
        else:
            print("Insufficient funds")
    def display_balance(self):
       print("Available Balance: ", self.balance)

m = BankAccount(12345)
m.deposit()
m.withdraw()
m.display_balance()
