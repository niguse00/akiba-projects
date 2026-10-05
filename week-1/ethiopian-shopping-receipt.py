customerName = input("enter customer name: ")
productName = input("enter product name: ")
price = float(input("enter a price: "))
quantity = int(input("enter a quantity: "))
total = price * quantity
line = "========================================"
line2 = "------------------------------"
title = "RECEIPT"
print(f"""
{line}
         {title}
{line}

Customer: {customerName}

Product     Price    Qty
{line2}
{productName}   {price} ETB   {quantity} 

Total:  {total} ETB

Thank you for shopping!
{line}
""")