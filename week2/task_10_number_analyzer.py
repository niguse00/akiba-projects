allNum = [] 
even = []
odd = []
sum = 0
for i in range(10):
    num = int(input("enter number: "))
    allNum.append(num)
    largest = max(allNum)
    smallest = min(allNum)
    sum += num
    if num % 2 == 0:
        even.append(num)
    else: 
        odd.append(num)
avg = sum / len(allNum)
print(f"The largest number is {largest}")
print(f"The smallest number is {smallest}")
print(f"The total is {sum}")
print(f"An avarage is {avg}")
print(f"The even numbers are {len(even)}")
print(f"The odd numbers are {len(odd)}")