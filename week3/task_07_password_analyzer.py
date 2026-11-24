def analyze_password(password):
    special_chars = "!@#$%^&*"
    if len(password) < 8:
       print("Password length must be greater than 8!")
    if not any(letter.isupper() for letter in password):
       print("there must upercase letter")
    if not any (letter.islower() for letter in password):
       print("password must include small letter")
    if not any(letter.isdigit() for letter in password):
       print("password must include numbers")
    if not any(letter in special_chars for letter in password):
       print("password must include special charcter.")
password = input("Enter password: ")
analyze_password(password)
         
