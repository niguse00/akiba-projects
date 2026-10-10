secreteNum = 4890

for i in range(5):
    userGuessNum = int(input("guessing number: "))
    if(secreteNum == userGuessNum):
        print(f"Congratulations!\n You guessed the number in  Attempt {i + 1} attempts")
        break;
    else:
        print(f"wrong please try again \n Attempt {i + 1}")
else:
    print("failed to guess correctly")