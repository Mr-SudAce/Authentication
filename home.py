from tkinter import *
from tkinter import ttk
import login
import register

def home():
    root = Tk()
    root.title("Login & Register")
    root.geometry("400x400")  # Set window size

    # Apply modern styling
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12), padding=6)
    style.configure("TEntry", font=("Arial", 12))

    # Add a title label
    lbl_title = ttk.Label(root, text="Welcome", font=("Arial", 16, "bold"), foreground="blue")
    lbl_title.pack(pady=10)

    # Email
    lbl_email = ttk.Label(root, text="Email:")
    lbl_email.pack(pady=5)

    entry_email = ttk.Entry(root, width=30)
    entry_email.pack(pady=5)

    # Username
    lbl_username = ttk.Label(root, text="Username:")
    lbl_username.pack(pady=5)

    entry_username = ttk.Entry(root, width=30)
    entry_username.pack(pady=5)

    # Password
    lbl_password = ttk.Label(root, text="Password:")
    lbl_password.pack(pady=5)

    entry_password = ttk.Entry(root, width=30, show="*")
    entry_password.pack(pady=5)



    # Result label
    lbl_result = Label(root, text="", fg="red", font=("Arial", 10))
    lbl_result.pack(pady=5)

    # Login function
    def on_login():
        username = entry_username.get()
        password = entry_password.get()
        email = entry_email.get()
        if login.login(username, password, email):
            lbl_result.config(text="Login successful!", fg="green")
        else:
            lbl_result.config(text="Login failed. Try again.", fg="red")

    # Register function
    def on_register():
        username = entry_username.get()
        password = entry_password.get()
        email = entry_email.get()
        if username == "" or password == "" or email == "" :
            lbl_result.config(text="Fields cannot be empty", fg="red")
            return

        if len(password) < 8:
            lbl_result.config(text="Password must be at least 8 characters long", fg="red")
            return

        if username == password:
            lbl_result.config(text="Username and password cannot be the same", fg="red")
            return

        if email.count("@") != 1 or "." not in email.split("@")[-1]:
            lbl_result.config(text="Invalid email address format", fg="red")
            return

        register.register(username, password, email)
        lbl_result.config(text="Registration successful!", fg="green")

    # Buttons with improved design
    btn_login = ttk.Button(root, text="Login", command=on_login)
    btn_login.pack(pady=10)

    btn_register = ttk.Button(root, text="Register", command=on_register)
    btn_register.pack(pady=5)

    # Run the app
    root.mainloop()

if __name__ == "__main__":
    home()
