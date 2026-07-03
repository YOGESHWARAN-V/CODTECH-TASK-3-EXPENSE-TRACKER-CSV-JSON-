import csv
import os

FILE_NAME = "expenses.csv"

def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    amount = input("Enter Amount: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense added successfully!\n")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expense records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        print("\nDate\t\tCategory\tAmount")
        print("-" * 35)
        total = 0

        for row in reader:
            if len(row) == 3:
                print(f"{row[0]}\t{row[1]}\t\t{row[2]}")
                total += float(row[2])

        print("-" * 35)
        print("Total Expense:", total)
        print()


while True:
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!\n")