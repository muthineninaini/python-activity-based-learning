
# Retail Billing with Multiple Discount Rules

products = {
    "electronics": {"price": 1000, "tax": 18},
    "clothing": {"price": 500, "tax": 5},
    "groceries": {"price": 200, "tax": 0},
    "footwear": {"price": 800, "tax": 12}
}

cart = []
subtotal = 0
total_tax = 0

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nProduct {i + 1}")
    name = input("Enter product name: ")
    category = input(
        "Category (electronics/clothing/groceries/footwear): "
    ).lower()
    quantity = int(input("Enter quantity: "))

    if category not in products:
        print("Invalid category. Product skipped.")
        continue

    if quantity <= 0:
        print("Quantity must be positive. Product skipped.")
        continue

    price = products[category]["price"]
    tax_rate = products[category]["tax"]

    amount = price * quantity
    tax = amount * tax_rate / 100

    cart.append({
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price,
        "amount": amount,
        "tax_rate": tax_rate,
        "tax": tax
    })

    subtotal += amount
    total_tax += tax

# Threshold discount rules
if subtotal >= 10000:
    discount_rate = 15
elif subtotal >= 5000:
    discount_rate = 10
elif subtotal >= 2000:
    discount_rate = 5
else:
    discount_rate = 0

discount = subtotal * discount_rate / 100

# Maximum concession limit
max_discount = 1500
discount = min(discount, max_discount)

# Final invoice total
grand_total = subtotal - discount + total_tax

print("\n" + "=" * 75)
print("                         RETAIL INVOICE")
print("=" * 75)

print(f"{'Product':15}{'Qty':>5}{'Price':>10}"
      f"{'Amount':>12}{'Tax':>10}{'Tax Amt':>12}")

print("-" * 75)

for item in cart:
    print(f"{item['name'][:15]:15}"
          f"{item['quantity']:5}"
          f"{item['price']:10.2f}"
          f"{item['amount']:12.2f}"
          f"{item['tax_rate']:9.1f}%"
          f"{item['tax']:12.2f}")

print("-" * 75)
print(f"Subtotal:              Rs. {subtotal:.2f}")
print(f"Discount ({discount_rate}%):       Rs. {discount:.2f}")
print(f"Total Tax:             Rs. {total_tax:.2f}")
print("=" * 75)
print(f"GRAND TOTAL:           Rs. {grand_total:.2f}")
print("=" * 75)
