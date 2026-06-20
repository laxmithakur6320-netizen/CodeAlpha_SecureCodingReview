
def login(username, password):
    # KAMIZ: Hardcoded credentials (security risk)
    if username == "admin" and password == "12345":
        return "Login Successful!"
    else:
        return "Login Failed!"

user = input("Enter Username: ")
pw = input("Enter Password: ")
print(login(user, pw))