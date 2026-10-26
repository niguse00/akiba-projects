
items = [
    {"name": "Notebook", "price": 100, "quantity": 3},
    {"name": "Pen", "price": 100, "quantity": 10},
    {"name": "Pencil", "price": 20, "quantity": 10}
]

line = "=============================="
line2 = "----------------------------------------"


def calculate_subtotal(items):
    total = 0

    for item in items:
        if item["price"] < 0 or item["quantity"] < 0:
            raise ValueError("Price and quantity cannot be negative.")

        total += item["price"] * item["quantity"]

    return total


def calculate_discount(subtotal):
    if subtotal < 1000:
        return 0
    elif subtotal < 3000:
        return subtotal * 0.05
    else:
        return subtotal * 0.10


def calculate_tax(amount, tax_rate):
    if not 0 <= tax_rate <= 100:
        raise ValueError("Invalid tax rate.")

    return amount * (tax_rate / 100)


def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    discounted_amount = subtotal - discount
    tax = calculate_tax(discounted_amount, tax_rate)
    final_amount = discounted_amount + tax

    print(line)
    print("            RECEIPT")
    print(line)

    print(f"{'Product':<15}{'Price':>8}{'Qty':>6}{'Total':>10}")
    print(line2)

    for item in items:
        product_total = item["price"] * item["quantity"]

        print(
            f"{item['name']:<15}"
            f"{item['price']:>8.2f}"
            f"{item['quantity']:>6}"
            f"{product_total:>10.2f}"
        )

    print(line2)
    print(f"Subtotal:       {subtotal:.2f} Birr")
    print(f"Discount:       {discount:.2f} Birr")
    print(f"Tax ({tax_rate}%):      {tax:.2f} Birr")
    print(f"Final amount:   {final_amount:.2f} Birr")
    print(line)


generate_receipt(items, 15)
