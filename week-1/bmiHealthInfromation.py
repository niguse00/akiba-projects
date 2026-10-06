name = input("enter your name: ")
weight = int(input("enter your weight: "))
height = float(input("enter your height: "))
line = "================================"
title = "BMI REPORT"

bmi = weight / (height * height)

print(f"""
{line}
           {title}
{line}

Name: {name}
weight: {weight} kg
Height: {height} m

BMI: {bmi}
{line}
""") 