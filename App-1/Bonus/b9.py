password = input("Enter your password: ")
result = {}
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isalpha():
        digit = True
result["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["uppercase"] = uppercase

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")
