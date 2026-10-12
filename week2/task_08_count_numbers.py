N = int(input("enter number: "))
sum = 0
even = []
odd = []
for i in range(N + 1):
    if(i % 2 == 0):
        even.append(i)
    elif(i % 2 == 1):
        odd.append(i)
    sum+=i
print(f"{len(even)} even numbers")
print(f"{len(odd)} odd numbers")
print(sum)