# login.py
import os
import hashlib
def login(username, email, password):
    if not os.path.exists("login.txt"):
        print("No users registered yet")
        return False
    
    with open("login.txt", "r") as file:
        users = file.readlines()
        for user in users:
            saved_username, saved_email, saved_password = user.strip().split(",")
            if username and email == saved_username and saved_email and hashlib.sha256(password.encode()).hexdigest() == saved_password:
                print(f"Login successful!!\nWelcome {username}")
                return True
        print("Failed to login")
        return False














