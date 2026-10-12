PIN = 1234
count = 3

while(count >= 1):
    password = int(input("enter password: "))
    if(PIN != password):
        print(f"Incorrect PIN\nAttempts remaining: {count - 1}")
    else:
        break       
    count -= 1
         