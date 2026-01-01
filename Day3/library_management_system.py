# Design and implement a class hierarchy for a library system (Book, Magazine, and DVD classes).
# Each class should include attributes and methods to check out items, return items, and display item details. 
# Create a collection of library items and use iteration to manage and display their information.

class Library:
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self.is_checked_out = False

    def checkout(self):
        if self.is_checked_out:
            print("Item already checked out.")
        else:
            self.is_checked_out = True
            print(f"{self.title} checked out successfully.")

    def return_item(self):
        if not self.is_checked_out:
            print("Item was not checked out.")
        else:
            self.is_checked_out = False
            print(f"{self.title} returned successfully.")

    def display_details(self):
        status = "Checked out" if self.is_checked_out else "Available"
        print(f"ID: {self.item_id}  |  Title: {self.title}  | Status: {status}")

class Book(Library):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.author = author

    def display_details(self):
        super().display_details()
        print(f"Author: {self.author}")

class Magazine(Library):
    def __init__(self, item_id, title, issue):
        super().__init__(item_id, title)
        self.issue = issue
    
    def display_details(self):
        super().display_details()
        print(f"Issue: {self.issue}")

class DVD(Library):
    def __init__(self, item_id, title, duration):
        super().__init__(item_id, title)
        self.duration = duration

    def display_details(self):
        super().display_details()
        print(f"Duration: {self.duration} minutes")

def find_item_by_id(library_items, item_id):
    for item in library_items:
        if item.item_id == item_id:
            return item
    return None 

def main():
    library_items = [
        Book(1, "Clean Code", "Robert C. Martin"),
        Magazine(2, "Time", "April 2024"),
        DVD(3, "Inception", 148),
        Book(4, "One Piece Volume 1", "Eichiiro Oda"),
        DVD(5, "Interstellar", 190),
        Magazine(6, "Forbes", "October 2025")
    ]

    while True:
        print("\n===== Library Menu =====")
        print("1. Display all items")
        print("2. Checkout an item")
        print("3. Return an item")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice==1:
            for item in library_items:
                item.display_details()
                print("-"*30)
        elif choice==2:
            item_id = int(input("Enter item ID to checkout: "))
            item = find_item_by_id(library_items, item_id)
            if item:
                item.checkout()
            else:
                print("No item exists with that item id.")
        elif choice==3:
            item_id = int(input("Enter item ID to return: "))
            item = find_item_by_id(library_items, item_id)
            if item:
                item.return_item()
            else:
                print("No item exists with that item id.")
        elif choice==4:
            print("Thank You!!")
            break
        else:
            print("Invalid choice!!")

if __name__=="__main__":
    main()


        