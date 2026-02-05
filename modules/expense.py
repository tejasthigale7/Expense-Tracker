class Expense:
    def __init__(self, amount: float, category: str, date: str):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.amount = float(amount)
        self.category = category.strip().title()
        self.date = date

    def to_file_string(self):
        return f"{self.amount},{self.category},{self.date}\n"

    def __str__(self):
        return f"{self.amount:<12.2f}{self.category:<15}{self.date:<12}"
