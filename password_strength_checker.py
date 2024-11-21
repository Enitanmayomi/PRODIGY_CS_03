import re

def password_strength(password):
    strength = 0

    # Check password length
    if len(password) >= 8:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for digits
    if re.search(r"\d", password):
        strength += 1

    # Check for special characters
    if re.search(r"[^\w\s]", password):
        strength += 1

    if strength == 0:
        return "Very Weak"
    elif strength == 1:
        return "Weak"
    elif strength == 2:
        return "Medium"
    elif strength == 3:
        return "Strong"
    else:
        return "Very Strong"

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = password_strength(password)
    print("Password strength:", strength)