import tkinter as tk

from models.wallet import Wallet
from services.wallet_service import WalletService
from payments.upi_payment import UpiPayment
from payments.card_payment import CardPayment
from database import load_transactions


def open_wallet_dashboard(user_id):

    wallet = Wallet()
    service = WalletService()

    root = tk.Tk()
    root.title("Digital Wallet")
    root.geometry("360x640")
    root.configure(bg="#121212")

    # ---------------- LOGOUT ----------------
    def logout():
        root.destroy()
        from gui.login_window import start_login_window
        start_login_window()

    # ---------------- HEADER ----------------
    header = tk.Frame(root, bg="#1F1F1F", height=50)
    header.pack(fill="x")

    tk.Button(header, text="Logout", bg="#FF5252",
              fg="white", border=0,
              command=logout).pack(side="right", padx=10, pady=10)

    # ---------------- BALANCE ----------------
    tk.Label(root, text="Balance", fg="white",
             bg="#121212", font=("Arial", 14)).pack(pady=10)

    balance_label = tk.Label(root, text="₹ 0",
                             fg="#00E676",
                             bg="#121212",
                             font=("Arial", 28, "bold"))
    balance_label.pack()

    # ---------------- AMOUNT ENTRY ----------------
    tk.Label(root, text="Enter Amount", fg="white",
             bg="#121212").pack(pady=10)

    amount_entry = tk.Entry(root, font=("Arial", 16), justify="center")
    amount_entry.pack()

    # ---------------- FUNCTIONS ----------------
    def add_money():
        try:
            amount = float(amount_entry.get())
            service.add_money(wallet, amount, user_id)
            load_data()
        except:
            pass

    def pay_upi():
        try:
            amount = float(amount_entry.get())
            UpiPayment().pay(amount, wallet, user_id)
            load_data()
        except:
            pass

    def pay_card():
        try:
            amount = float(amount_entry.get())
            CardPayment().pay(amount, wallet, user_id)
            load_data()
        except:
            pass

    # ---------------- BUTTONS ----------------
    btn_frame = tk.Frame(root, bg="#121212")
    btn_frame.pack(pady=15)

    tk.Button(btn_frame, text="Add Money", bg="#00C853",
              fg="white", width=12, height=2,
              command=add_money).grid(row=0, column=0, padx=5)

    tk.Button(btn_frame, text="Pay UPI", bg="#2979FF",
              fg="white", width=12, height=2,
              command=pay_upi).grid(row=0, column=1, padx=5)

    tk.Button(btn_frame, text="Pay Card", bg="#FF9100",
              fg="white", width=25, height=2,
              command=pay_card).grid(row=1, column=0, columnspan=2, pady=5)

    # ---------------- HISTORY ----------------
    tk.Label(root, text="Transactions",
             fg="white", bg="#121212",
             font=("Arial", 14)).pack()

    history_box = tk.Listbox(root, bg="#1E1E1E",
                             fg="white", height=15)
    history_box.pack(fill="both", expand=True, padx=10, pady=10)

    # ---------------- LOAD DATA ----------------
    def update_balance():
        balance_label.config(text=f"₹ {wallet.get_balance()}")

    def update_history():
        history_box.delete(0, tk.END)

        for txn in wallet.transactions:
            text = f"{txn.txn_type} ₹{txn.amount} {txn.status}"
            history_box.insert(tk.END, text)

            idx = history_box.size() - 1
            if txn.status == "SUCCESS":
                history_box.itemconfig(idx, fg="#00E676")
            else:
                history_box.itemconfig(idx, fg="#FF5252")

        history_box.see(tk.END)

    def load_data():

        data = load_transactions(user_id)

        wallet.transactions.clear()
        wallet._Wallet__balance = 0

        for txn in data:
            txn_type, amount, desc, status, timestamp = txn

            if txn_type == "CREDIT" and status == "SUCCESS":
                wallet._Wallet__balance += amount
            elif txn_type == "DEBIT" and status == "SUCCESS":
                wallet._Wallet__balance -= amount

            wallet.transactions.append(
                type("obj", (), {
                    "txn_type": txn_type,
                    "amount": amount,
                    "description": desc,
                    "status": status,
                    "timestamp": timestamp
                })
            )

        update_balance()
        update_history()

    load_data()

    root.mainloop()
