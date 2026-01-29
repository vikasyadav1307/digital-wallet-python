from models.transaction import Transaction
from database import save_transaction


class Wallet:

    def __init__(self):
        self.__balance = 0
        self.transactions = []   # For fast UI display

    # ---------------- ADD MONEY ----------------
    def add_money(self, amount, user_id=1):
        try:
            if amount <= 0:
                raise ValueError("Amount must be positive")

            # Update balance
            self.__balance += amount

            # Create transaction object
            txn = Transaction("CREDIT", amount, "Money Added", "SUCCESS")
            self.transactions.append(txn)

            # Save to database
            save_transaction(user_id, "CREDIT", amount, "Money Added", "SUCCESS")

        except Exception as e:
            print("Add Money Error:", e)

    # ---------------- DEDUCT MONEY ----------------
    def deduct_money(self, amount, description, user_id=1):
        try:
            if amount <= self.__balance:

                # Update balance
                self.__balance -= amount

                # Create SUCCESS transaction
                txn = Transaction("DEBIT", amount, description, "SUCCESS")
                self.transactions.append(txn)

                # Save SUCCESS to DB
                save_transaction(user_id, "DEBIT", amount, description, "SUCCESS")

                return True

            else:
                # Create FAILED transaction
                txn = Transaction("DEBIT", amount, description, "FAILED")
                self.transactions.append(txn)

                # Save FAILED to DB
                save_transaction(user_id, "DEBIT", amount, description, "FAILED")

                print("Insufficient Balance ❌")
                return False

        except Exception as e:
            print("Deduct Money Error:", e)
            return False

    # ---------------- GET BALANCE ----------------
    def get_balance(self):
        return self.__balance

    # ---------------- SHOW TRANSACTIONS ----------------
    def show_transactions(self):
        print("\n--- Transaction History ---")
        for txn in self.transactions:
            txn.show()
