balance = 500

transactions = []

def record_transactions(transaction_type, amount):
    transactions.append({
        "type":transaction_type,
        "amount":amount,
        "balance":balance
    })

def deposit():
    global balance
    
    amount = float(input("Enter deposit amount: "))
    if amount <= 0:
       print("Error: Amount must be greater than zero")
    else:
        balance += amount
        record_transactions("Deposit", amount)
        print(f"Successfully deposited {amount:.2f} Birr.")
        print(f"Current balance: {balance:.2f} Birr")

def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: "))
    
    if amount <= 0:
       print("Error: Amount must be greater tahn zero")
    elif amount > balance:
       print("Error: Insufficient balance")
    else: 
        balance -= amount
        record_transactions("Withdrawal",amount)
        print(f"Successfully withdrawed {amount:.2f} Birr.")
        print(f"Current balance: {balance:.2f} Birr")

def check_balance():
    print(f"Your current balance is: {balance:.2f} Birr")


def transaction_summary():
    total_deposited = 0
    total_withdrawn = 0

    print("\n========== TRANSACTION HISTORY ==========")

    if len(transactions) == 0:
        print("No transactions found.")
    else:
        for i, transaction in enumerate(transactions, start=1):
            print(f"\nTransaction {i}")
            print(f"Type: {transaction['type']}")
            print(f"Amount: {transaction['amount']:.2f} Birr")
            print(f"Balance: {transaction['balance']:.2f} Birr")

            if transaction["type"] == "Deposit":
                total_deposited += transaction["amount"]
            else:
                total_withdrawn += transaction["amount"]

    print("\n========== ACCOUNT SUMMARY ==========")
    print(f"Opening balance: 500.00 Birr")
    print(f"Total deposited: {total_deposited:.2f} Birr")
    print(f"Total withdrawn: {total_withdrawn:.2f} Birr")
    print(f"Final balance: {balance:.2f} Birr")

def main():
    while True: 
        print("\n========== BANKING SYSTEM ==========")
        print("1. Deposit money")
        print("2. withdraw money")
        print("3. Check balance")
        print("4. Transaction summary")
        print("5. exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
           deposit()
        elif choice == 2:
           withdraw()
        elif choice == 3:
           check_balance() 
        elif choice == 4:
           transaction_summary()
        elif choice == 5:
            print("Thank you for using our system!")
            break
        else: 
            print("Invalid choice. Please select 1-5.")


main()

