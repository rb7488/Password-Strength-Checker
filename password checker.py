import re

def check_password_strength(password):
    # Password rules
    length_error = len(password) < 8
    lowercase_error = not re.search(r"[a-z]", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Count number of failed checks
    errors = [length_error, lowercase_error, uppercase_error, digit_error, special_char_error]
    strength = 5 - sum(errors)

    # Determine strength
    if strength == 5:
        return "Strong 💪"
    elif strength >= 3:
        return "Medium ⚡"
    else:
        return "Weak ❌"

# User Input
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")
