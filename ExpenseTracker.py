import json
import os
from typing import List, Dict

def load_expenses() -> List[Dict]:
    """Load expenses from JSON file"""
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses: List[Dict]) -> None:
    """Save expenses to JSON file"""
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses: List[Dict], amount: float, category: str) -> None:
    """Add new expense"""
    expenses.append({"Amount": amount, "Category": category.lower()})
    save_expenses(expenses)

def print_expenses(expenses: List[Dict]) -> None:
    """Display all expenses"""
    for i, expense in enumerate(expenses):
        print(f"{i}: ${expense['Amount']:.2f} - {expense['Category']}")

def total_expenses(expenses: List[Dict]) -> float:
    """Calculate total expenses"""
    return sum(expense["Amount"] for expense in expenses)

def show_categories(expenses: List[Dict]) -> None:
    """Display unique categories"""
    categories = {expense["Category"] for expense in expenses}
    print("\n".join(categories))

def filter_by_category(expenses: List[Dict], category: str) -> List[Dict]:
    """Filter expenses by category"""
    return [exp for exp in expenses if exp["Category"] == category.lower()]

def delete_expense(expenses: List[Dict], index: int) -> bool:
    """Remove expense by index"""
    if 0 <= index < len(expenses):
        deleted = expenses.pop(index)
        print(f"Deleted: ${deleted['Amount']:.2f} ({deleted['Category']})")
        save_expenses(expenses)
        return True
    print("Invalid index!")
    return False

def clear_screen():
    """Clear console based on OS"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Show Total")
        print("4. Filter by Category")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                try:
                    amount = float(input("Amount: $"))
                    category = input("Category: ").strip()
                    add_expense(expenses, amount, category)
                    print("Expense added successfully!")
                except ValueError:
                    print("Invalid amount! Please enter a number.")

            case "2":
                if not expenses:
                    print("No expenses recorded!")
                else:
                    print_expenses(expenses)

            case "3":
                print(f"Total Expenses: ${total_expenses(expenses):.2f}")

            case "4":
                if not expenses:
                    print("No expenses recorded!")
                else:
                    print("Available categories:")
                    show_categories(expenses)
                    category = input("Enter category to filter: ").strip()
                    filtered = filter_by_category(expenses, category)
                    if filtered:
                        print_expenses(filtered)
                    else:
                        print("No expenses found in this category.")

            case "5":
                if not expenses:
                    print("No expenses to delete!")
                else:
                    print_expenses(expenses)
                    try:
                        index = int(input("Enter expense number to delete: "))
                        delete_expense(expenses, index)
                    except ValueError:
                        print("Please enter a valid number!")

            case "6":
                print("Goodbye!")
                break

            case _:
                print("Invalid option!")

        input("\nPress Enter to continue...")
        clear_screen()

if __name__ == "__main__":
    main()