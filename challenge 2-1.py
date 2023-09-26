class BankAccount:
    def __init__(self, account_number, account_holder_name, account_balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            raise ValueError("Insufficient balance")
        self.account_balance -= amount

    def get_balance(self):
        return self.account_balance

    def __str__(self):
        return f"Account number: {self.account_number}\nAccount holder name: {self.account_holder_name}\nAccount balance: {self.account_balance}"
bank_account = BankAccount(1234567890, "John Doe", 1000)
bank_account.deposit(500)
bank_account.withdraw(200)
print(bank_account.get_balance())
