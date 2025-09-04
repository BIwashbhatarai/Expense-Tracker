import json
import os

Expenses = []
FILE_NAME = "expenses.json"

# Load expenses from file at program start
def load_expenses():
    global Expenses
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            try:
                Expenses = json.load(f)
            except json.JSONDecodeError:
                Expenses = []
    else:
        Expenses = []

# Save expenses to file
def save_expenses():
    with open(FILE_NAME, "w") as f:
        json.dump(Expenses, f, indent=4)

# Add a new expense
def add_expenses():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food, Travel, etc.): ").strip()
        note = input("Enter note: ").strip()
        Expenses.append({"Amount": amount, "Category": category, "Note": note})
        save_expenses()  # Save immediately
        print("✅ Expenses added successfully!\n")
    except ValueError:
        print("❌ Invalid input! Amount must be a number.\n")

# View all expenses
def view_expenses():
    if not Expenses:
        print("📂 No expenses recorded yet.\n")
        return
    print("\n--- Expenses List ---")
    for i, exp in enumerate(Expenses, start=1):
        print(f"{i}. {exp['Amount']} | {exp['Category']} | {exp['Note']}")
    print()

# Delete an expense by index
def delete_expenses():
    view_expenses()
    if not Expenses:
        return
    try:
        index = int(input("Enter expense number to delete: "))
        if 1 <= index <= len(Expenses):
            removed = Expenses.pop(index - 1)
            save_expenses()  # Save immediately
            print(f"🗑️ Removed: {removed['Amount']} | {removed['Category']} | {removed['Note']}\n")
        else:
            print("❌ Invalid index.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def show_total():
    if not Expenses:
        print("📂 No expenses recorded yet!")
        return 
    total = sum(exp["Amount"] for exp in Expenses)
    print(f"\n💰 Total Expenses: {total}")
    
    print()
    
def show_category():
    if not Expenses:
        print("📂 No expenses recorded yet!")
        return 
    print("\n Category Summary: ")
    categories = {}
    for exp in Expenses:
        categories.setdefault(exp["Category"], 0)
        categories[exp["Category"]] += exp["Amount"]
    for cat, amt in categories.items():
        print(f"- {cat}: {amt}")
    print()
        
# Main program loop
def main():
    load_expenses()  # Load data at start
    while True:
        print("--- Expense Tracker CLI ---")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Delete Expenses")
        print("4: Show Total Expenses")
        print("5: Show Category Summary")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expenses()
        elif choice == "4":
            show_total()
        elif choice == "5":
            show_category()
        elif choice == "6":
            print("Exiting...GoodBye👋")
            break
        else:
            print("❌ Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
