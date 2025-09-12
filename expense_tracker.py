import json
import os
from datetime import datetime

# -------------------------------
# Global variables
# -------------------------------
Expenses = []                 # List to store all expense records
FILE_NAME = "expenses.json"   # File to save/load expenses

# -------------------------------
# Load expenses from file at program start
# -------------------------------
def load_expenses():
    global Expenses
    if os.path.exists(FILE_NAME):   # Check if file exists
        with open(FILE_NAME, "r") as f:
            try:
                Expenses = json.load(f)   # Load expenses from JSON file
            except json.JSONDecodeError:  # If file is empty or corrupted
                Expenses = []
    else:
        Expenses = []   # If no file, start with empty list

# -------------------------------
# Save expenses to file
# -------------------------------
def save_expenses():
    with open(FILE_NAME, "w") as f:
        json.dump(Expenses, f, indent=4)  # Save data in JSON format with indentation

# -------------------------------
# Add a new expense
# -------------------------------
def add_expenses():
    try:
        amount = float(input("Enter amount: "))   # Expense amount
        category = input("Enter category (Food, Travel, etc.): ").strip()
        note = input("Enter note: ").strip()
        date_input = input("Enter date (YYYY-MM-DD) or leave blank for today: ")

        if not date_input:   # Default = today's date
            date_input = datetime.today().strftime("%Y-%m-%d")

        # Store new expense as dictionary
        Expenses.append({
            "Amount": amount,
            "Category": category,
            "Note": note,
            "Date": date_input
        })

        save_expenses()   # Save immediately
        print("✅ Expense added successfully!\n")

    except ValueError:
        print("❌ Invalid input! Amount must be a number.\n")

# -------------------------------
# View all expenses
# -------------------------------
def view_expenses():
    if not Expenses:
        print("📂 No expenses recorded yet.\n")
        return

    print("\n--- Expenses List ---")
    for i, exp in enumerate(Expenses, start=1):
        print(f"{i}. {exp['Amount']} | {exp['Category']} | {exp['Note']} | {exp['Date']}")
    print()

# -------------------------------
# Delete an expense by index
# -------------------------------
def delete_expenses():
    view_expenses()
    if not Expenses:
        return

    try:
        index = int(input("Enter expense number to delete: "))
        if 1 <= index <= len(Expenses):
            removed = Expenses.pop(index - 1)   # Remove chosen expense
            save_expenses()
            print(f"🗑️ Removed: {removed['Amount']} | {removed['Category']} | {removed['Note']}\n")
        else:
            print("❌ Invalid index.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# -------------------------------
# Show total expenses
# -------------------------------
def show_total():
    if not Expenses:
        print("📂 No expenses recorded yet!")
        return 

    total = sum(exp["Amount"] for exp in Expenses)
    print(f"\n💰 Total Expenses: {total}")
    print()
    
# -------------------------------
# Show category-wise summary
# -------------------------------
def show_category():
    if not Expenses:
        print("📂 No expenses recorded yet!")
        return 

    print("\n📊 Category Summary: ")
    categories = {}

    for exp in Expenses:
        categories.setdefault(exp["Category"], 0)
        categories[exp["Category"]] += exp["Amount"]

    for cat, amt in categories.items():
        print(f"- {cat}: {amt:.2f}")
    print()

# -------------------------------
# Show monthly total expenses
# -------------------------------
def show_monthly_total():
    if not Expenses:
        print("📂 No expenses recorded yet.\n")
        return

    month = input("Enter month (YYYY-MM): ").strip()
    if not month:
        month = datetime.today().strftime("%Y-%m")

    total = 0
    for exp in Expenses:
        if exp["Date"].startswith(month):   # Match year & month
            total += exp['Amount']

    if total == 0:
        print(f"No expenses found for {month}")
    else:
        print(f"💰 Total expenses for {month}: {total}\n")

# -------------------------------
# Edit an expense
# -------------------------------
def edit_expenses():
    view_expenses()
    if not Expenses:
        return 

    try:
        index = int(input("Enter expense number to edit: "))
        if 1 <= index <= len(Expenses):
            exp = Expenses[index - 1]
            print("✏️ Leave blank to keep the old value")

            # Update amount
            amount_input = input(f"Amount ({exp['Amount']}): ").strip()
            if amount_input:
                try:
                    exp['Amount'] = float(amount_input)
                except ValueError:
                    print("❌ Invalid amount! Keeping old value")

            # Update category
            category_input = input(f"Category ({exp['Category']}): ").strip()
            if category_input:
                exp['Category'] = category_input

            # Update note
            note_input = input(f"Note ({exp['Note']}): ").strip()
            if note_input:
                exp['Note'] = note_input

            # Update date
            date_input = input(f"Date ({exp['Date']}): ").strip()
            if date_input:
                exp['Date'] = date_input

            save_expenses()
            print("✅ Expense updated successfully!")
        else:
            print("❌ Invalid index.\n")
    except ValueError:
        print("❌ Please enter a valid number.")

# -------------------------------
# Search expenses
# -------------------------------
def search_expenses():
    if not Expenses:
        print("📂 No expenses recorded yet.\n")
        return

    print("\n--- Search Expenses ---")
    print("You can search by Category, Date, or Amount")
    print("1. By Category")
    print("2. By Date (YYYY-MM-DD)")
    print("3. By Amount")

    choice = input("Enter your choice: ").strip()
    results = []

    if choice == '1':   # Search by category
        cat_input = input("Enter category to search: ").strip().lower()
        for exp in Expenses:
            if cat_input in exp['Category'].lower():
                results.append(exp)

    elif choice == '2':   # Search by date
        date_input = input("Enter date to search (YYYY-MM-DD): ").strip()
        for exp in Expenses:
            if exp['Date'] == date_input:
                results.append(exp)

    elif choice == '3':   # Search by amount
        try:
            amount_input = float(input("Enter amount to search: ").strip())
            for exp in Expenses:
                if exp['Amount'] == amount_input:
                    results.append(exp)
        except ValueError:
            print("❌ Invalid amount! Please enter a number")
            return

    else:
        print("❌ Invalid choice! Choose 1, 2, or 3") 
        return 

    # Show results
    if results:
        print("\n--- Search Results ---")
        for i, exp in enumerate(results, start=1):
            print(f"{i}. Amount: {exp['Amount']} | Category: {exp['Category']} | Note: {exp['Note']} | Date: {exp['Date']}")
        print(f"\n✅ {len(results)} expenses found matching your search.\n")
    else:
        print("❌ No matching expenses found.\n")

# -------------------------------
# Main program loop
# -------------------------------
def main():
    load_expenses()  # Load data at start
    while True:
        print("\n--- Expense Tracker CLI ---")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Delete Expenses")
        print("4. Show Total Expenses")
        print("5. Show Category Summary")
        print("6. Show Monthly Total")
        print("7. Edit Expenses")
        print("8. Search Expenses")
        print("9. Exit")

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
            show_monthly_total()
        elif choice == "7":
            edit_expenses()
        elif choice == "8":
            search_expenses()
        elif choice == "9":
            print("Exiting... Goodbye 👋")
            break
        else:
            print("❌ Invalid choice, try again.\n")

# -------------------------------
# Run program
# -------------------------------
if __name__ == "__main__":
    main()
