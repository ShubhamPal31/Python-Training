def student_grade_book():
    grade_book = [] 
    while True:
        print("----- Student Grade Book -----")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Show Class Average")
        print("4. Show Top Performer")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(grade_book)
        elif choice == "2":
            search_student(grade_book)
        elif choice == "3":
            class_average(grade_book)
        elif choice == "4":
            top_student(grade_book)
        elif choice == "5":
            print("Thank You!")
            break
        else:
            print("Invalid choice, try again.\n")
    

def add_student(grade_book):
    name = input("Enter student name: ")
    marks = []
    while True:
        mark = input("Enter a mark (or type 'done' to finish): ")
        if mark.lower() == "done":
            break
        try:
            marks.append(float(mark))
        except ValueError:
            print("Invalid input, please enter a number.")
    grade_book.append({"name": name, "grades": marks})
    print(f"Student {name} added successfully!\n")


def search_student(grade_book):
    name = input("Enter name to search: ")
    for student in grade_book:
        if student["name"].lower() == name.lower():
            print(f"Student Found: {student['name']}  Grades: {student['grades']}")
            return
    print("Student not found.\n")


def top_student(grade_book):
    if not grade_book:
        print("No students yet.\n")
        return
    top = None
    top_avg = 0
    for student in grade_book:
        if len(student["grades"]) == 0:
            continue
        avg = sum(student["grades"]) / len(student["grades"])
        if avg > top_avg:
            top_avg = avg
            top = student
    if top:
        print(f"Top Student: {top['name']} with average {top_avg:.2f}\n")
    else:
        print("No grades to calculate top performer.\n")


def class_average(grade_book):
    total = 0
    count = 0
    for student in grade_book:
        for g in student["grades"]:
            total += g
            count += 1
    if count == 0:
        print("No grades available yet.\n")
    else:
        print(f"Class Average: {total / count:.2f}\n")

if __name__ == "__main__":
    student_grade_book()
 






