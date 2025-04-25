class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_no, balance=0):
        self.accounts[acc_no] = balance

    def deposit(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no] += amount

    def withdraw(self, acc_no, amount):
        if acc_no in self.accounts and self.accounts[acc_no] >= amount:
            self.accounts[acc_no] -= amount

    def display(self, acc_no):
        print(f"Account {acc_no} balance: {self.accounts.get(acc_no, 'Account not found')}")

bank = Bank()
bank.create_account(123, 500)
bank.deposit(123, 200)
bank.display(123)
bank.withdraw(123, 100)
bank.display(123)