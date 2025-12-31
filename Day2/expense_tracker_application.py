def expense_tracker_application():
    days = int(input("Enter the number of days for which the expenses are to be tracked: "))
    if(days<=0):
        return
    expenses = [0.0]*days
    for i in range(days):
        amt = float(input(f"Enter the expense for day {i+1}: "))
        expenses[i] = amt if amt>=0 else 0
    
    print("CHOOSE WHAT TO DO:")
    print("1. Summary Report")
    print("2. Show minimum expense")
    print("3. Sow maximum expense")
    print("4. Show average expense")
    print("5. Add expense for a particular day")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    while choice!=6:
        if choice==1:
            display_summary(expenses)
        elif choice==2:
            display_minimum_expense(expenses)
        elif choice==3:
            display_maximum_expense(expenses)
        elif choice==4:
            display_average_expense(expenses)
        elif choice==5:
            i = int(input("Enter the day for which expense is to be added: "))
            if i<0 or i>=len(expenses):
                print("Invalid input!")
            else:
                amt = int(input(f"Enter the expense to be added for day {i}: "))
                expenses[i-1] += amt if amt>=0 else 0
                print("Expense added")
        elif choice==6:
            break
        else:
            print("Invalid choice!!")
        choice = int(input("Enter your choice: "))    
    print("THANK YOU")

def display_summary(expenses):
    print("Expense Summary:")
    display_minimum_expense(expenses)
    display_maximum_expense(expenses)
    display_average_expense(expenses)

def display_average_expense(expenses):
    sum = 0.0
    for i in expenses:
        sum += i
    avg = sum/len(expenses)
    print(f"Average: {avg}")

def display_minimum_expense(expenses):
    print(f"Minimum expense: {min(expenses)}")

def display_maximum_expense(expenses):
    print(f"Maximum expense: {max(expenses)}") 

if __name__=="__main__":
    expense_tracker_application()