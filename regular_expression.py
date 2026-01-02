# User Input Validator using Regular Expressions project
import re

def validate_email(email):
    pattern = r'^[a-zA-A0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    return re.fullmatch(pattern, email)

def validate_mobile(mobile):
    pattern = r'^[6-9]\d{9}$'
    return re.fullmatch(pattern, mobile)

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@#$]).{8,}$'
    return re.fullmatch(pattern,password)

while True:
    print("\n--- Input Validation Menu ---")
    print("1. Validate email")
    print("2. Validate Mobile Number")
    print("3. Validate Password")
    print("4. Exit")

    choice = input("Enter the choice: ")

    if choice == '1':
        email = input("Enter the email: ")
        if validate_email(email):
            print("Valid Email...")
        else:
            print("Invalid email...")

    elif choice == '2':
        mobile = input("Enter the mobile number: ")
        if validate_mobile(mobile):
            print("Valid mobile number")
        else:
            print("Invalid mobile number...")

    elif choice == '3':
        password = input("Enter the passoword:")
        if validate_password(password):
            print("Valid password...")
        else:
            print("Invalid password..")

    elif choice == '4':
        print("Program ended...")
        break

    else:
        print("Invalid choice...")