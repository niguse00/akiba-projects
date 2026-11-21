products = {}

def product(name, price, stock_quantity):
    clean_name = name.strip()
    product_key = clean_name.lower() 
    products[product_key] = {
       "name":name,
       "price":price,
       "stock_quantity":stock_quantity
    }
    
    
def add_new_product():
    name = input("Enter product name: ")
    price = int(input("Enter product price: "))
    stock_quantity = int(input("Enter stock quantity: "))
    if name == "" and price <= 0 and stock_quantity <= 0:
       print("invalid input")
    else:
       product(name,price,stock_quantity)
    print("Product is added successfully!")

def search_product(name):
    product_key = name.strip().lower()
    product = products.get(product_key)
    if product:
       print(f"{product['name']} | Price: ${product['price']:.2f} | Stock: {product['stock_quantity']}")
    else:
       print("product is not found.")
        
def update_product_price(name, new_price):
    product_key = name.strip().lower()
    product = products.get(product_key)
    if product:
       product['price'] = new_price
       print(f"Updated price for '{products[product_key]['name']}' to ${new_price:.2f}.")
def increase_stock(name, quantity):
    product_key = name.strip().lower()
    product = products.get(product_key)
    if not product:
       print("product is not found")
       
    if product:
       product['stock_quantity'] += quantity
       new_stock = product['stock_quantity']
       print(f"Added {quantity} units to '{products[product_key]['name']}'. New stock: {new_stock}.")
    
def sell_product(name,quantity):
    product_key = name.strip().lower()
    product = products.get(product_key)
    if quantity <= 0:
       print("Error: sale quantity must be greater than zereo")
    if not product:
       print(f"Error: Product '{name}' not found.")
    
    current_stock = product['stock_quantity']
    if quantity > current_stock:
       print(f"Error: Insufficient stock for '{products[product_key]}'. Available")
    current_stock -=int(quantity)
    total_sale = quantity * products[product_key]["price"]
    print(f"Sold {quantity} x '{product_key}' for ${total_sale:.2f}. Remaining stock: {products[product_key]['stock_quantity'] - quantity}.")

def calculate_total_value(products):
    total = sum(
        item["price"] * item["stock_quantity"]
        for item in products.values()
    )
    return total


def generate_low_stock_report(products, threshold=5):
    low_stock_items = []
    for name, details in products.items():
        if details["stock_quantity"] < threshold:
            low_stock_items.append({
                "name": name,
                "price": details["price"],
                "stock": details["stock_quantity"]
            })
    return low_stock_items

def main():
    while(True):
        print("\n========== inverntary ==========")
        print("1. Add New Product")
        print("2. Search Product")
        print("3. Update Product")
        print("4. Increase Stock")
        print("5. Sell Product")
        print("6. Calculate total value")
        print("7. Generate low stock report")
        print("8. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
           add_new_product()
        elif choice == 2: 
           search = input("Type here what you want.. ")
           search_product(search)
        elif choice == 3:
            search = input("Enter name: ")
            new_price = int(input("Enter new price: "))
            update_product_price(search, new_price)
        elif choice == 4:
            search = input("Enter name: ")
            if search:
               quantity = int(input("enter stock quantity to be added: "))
               increase_stock(search, quantity)
        elif choice == 5:
            search = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            sell_product(search,quantity)
        elif choice == 6:
             total = calculate_total_value(products)
             print(f"Total value: {total}")
        elif choice == 7:
           low_stock_items = generate_low_stock_report(products) 
           print(low_stock_items)
        elif choice == 8:
            print("Thank you for using us")
            break


main()


