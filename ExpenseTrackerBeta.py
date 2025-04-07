
def add_expense(expenses, amount, category):
    expenses.append({"Amount": amount, "Category": category})


def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["Amount"]}, Category: {expense["Category"]}')


def sum_expenses(expenses):
    return sum(map(lambda expense: expense["Amount"], expenses))


def show_categorys(expenses):
    seen_categorys = set()
    for expense in expenses:
        if expense["Category"] not in seen_categorys:
            print(expense["Category"])
            seen_categorys.add(expense["Category"])


def filter_expenses(expenses, category):
    return list(filter(lambda x: x["Category"] == category, expenses))


def main():
    expenses = []

    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = input("Type your choice: ").strip()

        match choice:
            case "1":
                try:
                    category = input("Type the category: ").strip().lower()
                    amount = int(input("Type the amount: "))
                    add_expense(expenses, amount, category)
                    print(f"Added: R$ {amount} to {category}")
                except ValueError:
                    print("Invalid amount! Please enter a number.")
            case "2":
                if not expenses:
                    print("No expenses yet!")
                else:
                    print_expenses(expenses)
            case "3":
                total = sum_expenses(expenses)
                print(f"Total expenses: R$ {total}")
            case "4":
                if not expenses:
                    print("No expenses yet!")
                else:
                    print_expenses(expenses)
                    category = input("Type the category to filter: ").strip().lower()
                    filtered = filter_expenses(expenses, category)
                    if not filtered:
                        print("No expenses in this category.")
                    else:
                        print_expenses(filtered)
            case "5":
                break
            case _:
                print("Invalid option!")

        input("\nPress Enter to continue...")
        

if __name__ == "__main__":
    main()