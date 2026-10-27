
# Multi-Currency Travel Budget Analysis

budget = float(input("Enter travel budget in INR: "))
fee_rate = float(input("Enter conversion fee percentage: "))

exchange_rates = {
    "INR": 1.0,
    "USD": 85.0,
    "EUR": 95.0,
    "GBP": 110.0
}

expenses = {}
total_spending = 0.0

n = int(input("Enter number of expense entries: "))

for i in range(n):
    print(f"\nExpense {i + 1}")

    category = input("Enter category: ").strip().title()
    amount = float(input("Enter expense amount: "))
    currency = input(
        "Enter currency (INR/USD/EUR/GBP): "
    ).strip().upper()

    if currency not in exchange_rates:
        print("Unsupported currency. Entry skipped.")
        continue

    if amount < 0:
        print("Amount cannot be negative. Entry skipped.")
        continue

    # Convert to INR
    converted_amount = amount * exchange_rates[currency]

    # Calculate conversion fee
    conversion_fee = converted_amount * fee_rate / 100

    final_amount = converted_amount + conversion_fee

    expenses[category] = (
        expenses.get(category, 0) + final_amount
    )

    total_spending += final_amount

    print(f"Converted Amount: Rs. {converted_amount:.2f}")
    print(f"Conversion Fee: Rs. {conversion_fee:.2f}")
    print(f"Final Expense: Rs. {final_amount:.2f}")

# Budget analysis
print("\n" + "=" * 50)
print("       TRAVEL BUDGET SUMMARY")
print("=" * 50)

for category, amount in expenses.items():
    print(f"{category:20}: Rs. {amount:.2f}")

print("-" * 50)
print(f"Total Spending       : Rs. {total_spending:.2f}")
print(f"Travel Budget        : Rs. {budget:.2f}")

if total_spending > budget:
    print(f"Budget Exceeded      : Rs. {total_spending - budget:.2f}")
else:
    print(f"Budget Remaining     : Rs. {budget - total_spending:.2f}")

if expenses:
    largest_category = max(expenses, key=expenses.get)
    print(f"Largest Expense      : {largest_category}")
    print(f"Category Amount      : Rs. {expenses[largest_category]:.2f}")
else:
    print("No valid expenses recorded.")

print("=" * 50)
