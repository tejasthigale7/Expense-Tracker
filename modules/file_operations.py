from modules.expense import Expense


def load_expenses(filepath):
    expenses = []

    try:
        with open(filepath, "r") as f:
            for line in f:
                amount, category, date = line.strip().split(",")
                expenses.append(Expense(float(amount), category, date))
    except FileNotFoundError:
        open(filepath, "w").close()  # auto create file

    return expenses


def save_expense(filepath, expense: Expense):
    with open(filepath, "a") as f:
        f.write(expense.to_file_string())
