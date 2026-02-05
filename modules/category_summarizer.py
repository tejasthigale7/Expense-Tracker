def summarize_expenses(expenses):
    totals = {}

    for exp in expenses:
        totals.setdefault(exp.category, 0)
        totals[exp.category] += exp.amount

    return totals
