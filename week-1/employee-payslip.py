employeeName = input("enter employee name: ")
basicSalary = float(input("enter basic salary: "))
transporAllowance = float(input("enter transport allowance: "))
foodAllowance = float(input("enter food allowance: "))

line = "========================================"
line2 = "------------------------------"
title = "EMPLOYEE PAYSLIP"

grossSalary = basicSalary + transporAllowance + foodAllowance

print(f"""
{line}
              {title}
{line}


Employee: {employeeName}

Basic Salary:  {basicSalary} ETB
Transport Allowance:   {transporAllowance} ETB
Food Allowance: {foodAllowance} ETB
{line2}
Gross Salary: {grossSalary} ETB
{line}
""")