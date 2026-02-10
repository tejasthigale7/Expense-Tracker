from modules.expense import Expense
from modules.file_operations import load_expenses, save_expense
from modules.category_summarizer import summarize_expenses
from modules.validators import is_valid_date

FILEPATH = "data/expenses.txt"


def display_menu():
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Summarize by Category")
    print("4. Exit")


# --------------------------
# ADD EXPENSE
# --------------------------
def add_expense():
    amount = input("Enter amount: ")

    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except:
        print("Invalid amount. Please enter a numeric value.")
        return

    category = input("Enter category: ")

    date = input("Enter date (YYYY-MM-DD): ")
    if not is_valid_date(date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    expense = Expense(amount, category, date)
    save_expense(FILEPATH, expense)

    print("Expense added successfully!")


# --------------------------
# VIEW EXPENSES
# --------------------------
def view_expenses():
    expenses = load_expenses(FILEPATH)

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nAmount       Category       Date")
    print("---------------------------------")

    for exp in expenses:
        print(exp)


# --------------------------
# SUMMARY
# --------------------------
def summarize():
    expenses = load_expenses(FILEPATH)

    if not expenses:
        print("No expenses to summarize.")
        return

    totals = summarize_expenses(expenses)

    print("\n--- Expense Summary by Category ---")
    print("Category       Total Amount")
    print("---------------------------------")

    for cat, total in totals.items():
        print(f"{cat:<15}{total:.2f}")


# --------------------------
# MAIN LOOP
# --------------------------
def main():
    print("Welcome to Expense Tracker")

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            summarize()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
