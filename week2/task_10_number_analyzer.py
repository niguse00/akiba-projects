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



if __name__ == '__main__':
    scores = []
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        scores.append([name, score]) 
    scores.sort(key = lambda score : score[1])
    idx = 0
    lowest = scores[0][1]
    second_lowest = 0
    for i in range(n):
        if scores[i][1] != lowest:
            second_lowest = scores[i][1]
            idx = i
            break
    
    ans = []
    # [10, 10, 10, 11, 11, 11, 11] 
    # idx = 3
    # second_lowest = 11
    while idx < n and  scores[idx][1] == second_lowest:
        ans.append(scores[idx][0])
        idx += 1
    ans.sort()
    for name in ans:
        print(name)
if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        command = list(input().split())
        if command[0]  == "insert":
            arr.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(arr)
        elif command[0] == "remove" :
            arr.remove(int(command[1]))
        elif command[0] == "append":
            arr.append(int(command[1]))
        elif command[0] == "sort" :
            arr.sort()
        elif command[0] == "pop":
            arr.pop()
        else:
            arr.reverse()