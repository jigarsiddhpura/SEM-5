class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} into account {self.account_number}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from account {self.account_number}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.01):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of ${interest} applied to account {self.account_number}.")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=100):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew ${amount} from account {self.account_number}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

# Create instances of BankAccount, SavingsAccount, and CheckingAccount
account1 = BankAccount("001", "Alice", 1000)
savings_account1 = SavingsAccount("002", "Bob", 5000, 0.02)
checking_account1 = CheckingAccount("003", "Charlie", 2000, 500)

# Create a Bank and add accounts to it
bank = Bank()
bank.add_account(account1)
bank.add_account(savings_account1)
bank.add_account(checking_account1)

# Perform transactions
account1.deposit(500)
account1.withdraw(200)
account1.display_balance()

savings_account1.deposit(1000)
savings_account1.apply_interest()
savings_account1.display_balance()

checking_account1.withdraw(2500)
checking_account1.display_balance()
