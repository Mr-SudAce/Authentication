#register.py
import hashlib

def register(username, email, password):
    with open("login.txt", "a") as file:
        file.write(f"Username: {username},\nEmail: {email}\nPasscode: {hashlib.sha256(password.encode()).hexdigest()}\n")
    print("Registration successful!!")
