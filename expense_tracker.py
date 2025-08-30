Expenses = []

def add_expenses():
    try:
        amount = float(input("Enter amount: ")) 
        category = input("Enter category (Food, Travel, etc.): ")
        note = input("Enter note: ")
        Expenses.append({"Amount": amount,"Category": category,"Note": note})
        print("✅ Expenses added successfully!\n")
    except ValueError:
        print("❌ Invalid input! Amount must be a number.\n")
    
def view_expenses():
    if not Expenses:
        print("📂 No expenses recorded yet.\n")
        return
    print("\n--- Expenses List---")
    for i , exp in enumerate(Expenses, start=1):
        print(f"{i}. {exp['Amount']} | {exp['Category']} | {exp['Note']}")
    print()

def delete_expenses():
    view_expenses()
    if not Expenses:
        return
    try:
        index = int(input("Enter expense number to delete: "))
        if 1 <= index <= len(Expenses):
            removed = Expenses.pop(index - 1)
            print(f"🗑️ Removed: {removed['Amount']} | {removed['Category']} | {removed['Note']}\n")
        else:
            print("❌ Invalid index.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def main():
    while True:
        print("---Expense Tracker CLI---")
        print('1. Add Expenses')
        print("2. View Expenses")
        print("3. Delete Expenses")
        print("4. Exit")
        
        choice = input('Enter your choice: ')
        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expenses()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.\n")
            
if __name__ == "__main__":
    main()        