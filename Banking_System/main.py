from bank_account import BankAccount
from savings_account import SavingsAccount

a1 = BankAccount(101, "Luffy", 1000)
a2 = BankAccount(102, "Zoro", 700)
a3 = SavingsAccount(103, "Nami", 5000, 100)

a1.deposit(100)
a2.withdraw(-100)
a3.withdraw(4500)

accounts = [a1, a2, a3]

for acc in accounts:
    acc.display_details()

