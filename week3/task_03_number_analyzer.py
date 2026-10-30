number = int(input("Enter number: "))
def is_prime(number):
    my_num = []
    for i in range(1,number+1):
        if number % i == 0:
           my_num.append(i)
    if len(my_num) > 2:
       return "is Not prime"
    elif len(my_num) < 2:
       return "is neither prime nor composite"
    else:
       return "is prime"

def even_or_odd(number):
    if number % 2 == 0:
       return "even"
    else:
       return "odd"
            
def get_divisors(number):
    for i in range(1, number+1):
        if number % i == 0:
           return i

def sum_of_digits(number):
    num_str = str(number)
    nums = 0
    for num in num_str:
        nums += int(num)
    return nums

def reverse_number(number):
    num_str = str(number)
    return(int(num_str[::-1]))

def analyze_number(number): 
    odd_even = even_or_odd(number)
    prime_or = is_prime(number)
    sum_digit = sum_of_digits(number)
    reverse = reverse_number(number)
    print(f"          {number}")
    print("============================")
    print(f"""
    The number is {odd_even}
    The number is {prime_or}
    The sum of the digit is {sum_digit}
    The reverse of the number is {reverse}
""")
analyze_number(number)
    
    
    