from modules.expense import Expense


def load_expenses(filepath):
    expenses = []

    try:
        with open(filepath, "r") as f:
            for line in f:
                if line.strip():
                    amount, category, date = line.strip().split(",")
                    expenses.append(Expense(amount, category, date))
    except FileNotFoundError:
        open(filepath, "w").close()

    return expenses


def save_expense(filepath, expense):
    with open(filepath, "a") as f:
        f.write(expense.to_file_string())
