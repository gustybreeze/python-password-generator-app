import random
import string

def generate_password(length):
    if length < 4:
        return "Password must be at least 4 characters."
    
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
]
    
    all_chars = upper + lower + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password) 

try:
    length = int(input("Enter desired password length in numbers: "))
    print("Generated Password: ", generate_password(length)) 

except ValueError:
    print("Please enter a valid number.") 