startNum = int(input("enter number: "))
endNum = int(input("enter number: "))
for i in range(startNum, endNum):
    if((i % 3 == 0) & (i % 5 == 0)):
        print("FizzBuzz")
    elif(i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    else:
        print(i)