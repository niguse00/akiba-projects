studentName = input("enter student name: ")
pythonScore = float(input("enter python score: "))
englishScore = float(input("enter english score:"))
mathScore = float(input("enter maths score: "))

line = "========================================"
line2 = "------------------------------"
title = "STUDENT RESULT"
avarageScore = (pythonScore + englishScore + mathScore) / 3

print(f"""
{line}
              {title}
{line}

Student: {studentName}

Python:  {pythonScore}
English: {englishScore}
Mathematics: {mathScore}

{line2}

Average:  {avarageScore}
{line}

""")


