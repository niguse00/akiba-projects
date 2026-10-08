num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

if((num1 > num2) & (num1 > num3)):
    print(f"{num1} is largest number")
elif((num1 < num2) & (num2 > num3)):
    print(f"{num2} is largest number")
elif((num1 < num3) & (num2 < num3)):
    print(f"{num3} is largest number")
else:
    print("all numbers are equal")