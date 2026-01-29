import tkinter as tk
from services.auth_service import AuthService

auth = AuthService()


def start_login_window():

    root = tk.Tk()
    root.title("Digital Wallet Login")
    root.geometry("350x350")

    tk.Label(root, text="Digital Wallet", font=("Arial", 18)).pack(pady=20)

    tk.Label(root, text="Name").pack()
    name_entry = tk.Entry(root, width=30)
    name_entry.pack(pady=5)

    tk.Label(root, text="Email").pack()
    email_entry = tk.Entry(root, width=30)
    email_entry.pack(pady=5)

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*", width=30)
    password_entry.pack(pady=5)

    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    # -------- LOGIN --------
    def login():
        email = email_entry.get().strip()
        password = password_entry.get().strip()

        if not email or not password:
            result_label.config(text="Enter Email + Password", fg="red")
            return

        user = auth.login(email, password)

        if user:
            root.destroy()
            from gui.wallet_window import open_wallet_dashboard
            open_wallet_dashboard(user[0])
        else:
            result_label.config(text="Invalid Login", fg="red")

    # -------- REGISTER --------
    def register():
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        password = password_entry.get().strip()

        if not name or not email or not password:
            result_label.config(text="All fields required", fg="red")
            return

        result = auth.register(name, email, password)

        if result == "SUCCESS":
            result_label.config(text="Registered Successfully", fg="green")
        elif result == "EMAIL_EXISTS":
            result_label.config(text="Email Already Exists", fg="red")

    tk.Button(root, text="Login", width=20, command=login).pack(pady=5)
    tk.Button(root, text="Register", width=20, command=register).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    start_login_window()
