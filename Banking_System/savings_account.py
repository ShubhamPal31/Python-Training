from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, minimum_balance):
        try:
            super().__init__(account_number, account_holder, balance)
            if minimum_balance<0:
                raise Exception("Balance must be positive")
            self.minimum_balance = minimum_balance
        except Exception as e:
            print(e)
    
    def withdraw(self, amount):
        try:
            if amount<=0:
                raise Exception("Withdrawl amount must be positive")
            if self.balance-amount < self.minimum_balance:
                raise Exception("Cannpt go below Minimum Balance")
            self.balance -= amount
            print("Withdrawn successfully.")
        except Exception as e:
            print(e)
