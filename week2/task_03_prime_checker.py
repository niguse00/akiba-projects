
num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

# we don't need to check every number the 
# The reason is we use loop and the loop iterate  every number.  