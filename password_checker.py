password = input("Enter Password: ")
score = 0

if len(password) >= 8:
    score += 1
if any(c.isupper() for c in password):
    score += 1
if any(c.islower() for c in password):
    score += 1
if any(c.isdigit() for c in password):
    score += 1
if any(not c.isalnum() for c in password):
    score += 1

if password in ["123456", "password", "qwerty"]:
    print("Very Weak Password")
elif score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Medium Password")
else:
    print("Strong Password")