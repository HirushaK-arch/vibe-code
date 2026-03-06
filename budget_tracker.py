def main():
    try:
        # Ask for total monthly budget
        total_budget = float(input("Enter your total monthly budget: "))

        total_expenses = 0.0
        print("Enter your expenses (type 'done' to finish):")
        
        while True:
            user_input = input("Enter expense: ").lower()
            if user_input == 'done':
                break
            try:
                expense = float(user_input)
                total_expenses += expense
            except ValueError:
                print("Invalid input. Please enter a numeric value or 'done'.")

        # Subtract expenses from total budget
        remaining_balance = total_budget - total_expenses

        # Display results
        print("-" * 30)
        print(f"Total Budget      : {total_budget:.2f}")
        print(f"Total Expenses    : {total_expenses:.2f}")
        print(f"Remaining Balance : {remaining_balance:.2f}")
        print("-" * 30)

        # Warning for low funds
        if remaining_balance < 500:
            print("Warning: Low Funds")

    except ValueError:
        print("Invalid input. Please enter numeric values for budget and expenses.")

if __name__ == "__main__":
    main()
