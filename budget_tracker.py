# Initialize the list to store expenses
expenses = []

# Initialize variables for income and budget
income = 0

# Predefined categories
categories = ['Rent', 'Groceries', 'Entertainment', 'Utilities', 'Transportation', 'Other']


# Function to add an expense
def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: $"))

    # Category selection
    print("Select a category:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    category_choice = int(input(f"Choose a category (1-{len(categories)}): "))
    category = categories[category_choice - 1] if 1 <= category_choice <= len(categories) else input(
        "Enter custom category: ")

    expense = {
        'description': description,
        'amount': amount,
        'category': category
    }
    expenses.append(expense)
    print(f"Added expense: {description} - ${amount} under category {expense['category']}")
    budget_alert()


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\nExpenses recorded:")
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['description']} - ${expense['amount']} (Category: {expense['category']})")


def total_spending():
    return sum(expense['amount'] for expense in expenses)


def remaining_budget():
    return income - total_spending()


def budget_alert():
    total_spent = total_spending()
    if total_spent >= 0.9 * income:
        print("Alert: You are nearing your budget limit!")
    if total_spent > income:
        print("Alert: You have exceeded your budget!")


def view_category_summary():
    if not expenses:
        print("No expenses recorded yet.")
        return

    category_totals = {}
    for expense in expenses:
        if expense['category'] not in category_totals:
            category_totals[expense['category']] = 0
        category_totals[expense['category']] += expense['amount']

    print("\nSpending by category:")
    for category, total in category_totals.items():
        print(f"{category}: ${total}")


def edit_expense():
    view_expenses()
    if expenses:
        index = int(input("Enter the number of the expense to edit (1 to {}): ".format(len(expenses)))) - 1
        if 0 <= index < len(expenses):
            print(f"Editing expense: {expenses[index]}")
            new_description = input("Enter new description (leave blank to keep current): ")
            new_amount = input("Enter new amount (leave blank to keep current): ")
            new_category = input("Enter new category (leave blank to keep current): ")

            if new_description:
                expenses[index]['description'] = new_description
            if new_amount:
                expenses[index]['amount'] = float(new_amount)
            if new_category:
                expenses[index]['category'] = new_category

            print(f"Expense updated: {expenses[index]}")
        else:
            print("Invalid expense number.")


def delete_expense():
    view_expenses()
    if expenses:
        index = int(input("Enter the number of the expense to delete (1 to {}): ".format(len(expenses)))) - 1
        if 0 <= index < len(expenses):
            print(f"Deleted expense: {expenses[index]}")
            expenses.pop(index)
        else:
            print("Invalid expense number.")


def main_menu():
    global income

    print("Welcome to the Personal Budget Tracker!")
    if income == 0:
        income = float(input("Enter your monthly income: $"))

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spending")
        print("4. View Remaining Budget")
        print("5. View Spending by Category")
        print("6. Edit Expense")
        print("7. Delete Expense")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")  # Fixed the input syntax

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print(f"Total spending: ${total_spending()}")
        elif choice == "4":
            print(f"Remaining budget: ${remaining_budget()}")
        elif choice == "5":
            view_category_summary()
        elif choice == "6":
            edit_expense()
        elif choice == "7":
            delete_expense()
        elif choice == "8":
            print("Exiting the program.")
            break  # Properly exit the loop here
        else:
            print("Invalid option. Please try again.")  # Fixed indentation for else block

if __name__ == "__main__":
    main_menu()