import datetime

books = {}  
issued_books = {}   

def add_books():
    name = input("Enter the name of the book: ")
    qty = int(input("Enter the quantity: "))

    books[name] = books.get(name, 0) + qty
    print(f"{qty} copies of {name} added.\n")


def show_books():
    if not books:
        print("No book available")
        return
    for book, qty in books.items():
        print(f" {book} -> {qty} copies")
    print()

def issue_books():
    show_books()
    name = input("Enter the book name: ")
    if name not in books:
        print("Book not available")
        return
    
    student = input("Enter the student name: ")
    duration = int(input("Enter duration in days: "))

    issue_date = datetime.date.today()

    issued_books[name] = {
        "student": student,
        "issue_date": issue_date,
        "duration": duration
    }

    books[name] -= 1

    print(f"Book {name} issued to {student} on {issue_date}")


def return_book():
    name = input("Enter the book name: ")
    if name not in issued_books:
        print("This book was not issued")
        return
    record = issued_books[name]

    return_date = datetime.date.today()
    issue_date = record["issue_date"]
    duration = record["duration"]

    days_used = (return_date - issue_date).days

    fine= 0
    if days_used > duration:
        extra_days = days_used -duration
        weeks_late = (extra_days // 7) + 1
        fine = weeks_late * 20 #20 rupees fine per week

    books[name] += 1
    issued_books.pop(name)

    print(f"Return details: ")
    print(f"Student: {record['student']}")
    print(f"Issued on: {issue_date}")
    print(f"Returned on : {return_date}")
    print(f"Days used: {days_used}")

    if fine > 0:
        print(f"Late fine: {fine}")
    else:
        print("Book returned on time")

    print("Book returned Successfully")


def library():
    while True:
        print("1. Add Books")
        print("2. Show Books")
        print("3. Issue Books")
        print("4. Return Book")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank You!")
            break
        else:
            print("Invalid Choice")


library()
