class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        try:
            self.account_number = account_number
            self.account_holder = account_holder
            if balance<0:
                raise Exception("Balance must be positive")
            self.balance = balance
        except Exception as e:
            print(e)

    def deposit(self, amount):
        try:
            if amount<=0:
                raise Exception("Desposit amount must be positive")
            self.balance += amount
            print(f"{amount}$ Deposited successfully.")
        except Exception as e:
            print(e)

    def withdraw(self, amount):
        try:
            if amount<=0:
                raise Exception("Withdrawl amount must be positive")
            if amount>self.balance:
                raise Exception("Withdrawl amount exceeds current balance")
            self.balance -= amount
            print("Withdrawn successfully.")
        except Exception as e:
            print(e)
    
    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")
        print("-"*30)