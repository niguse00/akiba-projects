studentName = input("Enter your name: ")
studentId = input("Enter your id: ")
department = input("Enter your department: ")
year = int(input("Enter year: "))
university = input("Enter university: ")
phone = int(input("Enter phone number: "))
line = "+--------------------------------+"

print(
    f"""
    {line}
    |       AKIBA STUDENT CARD          |
    {line}
    |Name: {studentName}      |
    |ID: {studentId}         |
    |Department: {department}       |
    |Year: {year}         |
    |University: {university} University      |
    |Phone: {phone}               |
    {line}""")