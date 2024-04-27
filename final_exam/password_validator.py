import re


def validate_password(password):
    if len(password) >= 8:
        return f"Password must be at least 8 characters long!"
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    return True


password = input()
if validate_password(password):
    print("Valid password")
else:
    print("Invalid password")





