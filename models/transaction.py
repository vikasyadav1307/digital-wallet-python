class Transaction:

    def __init__(self, txn_type, amount, description, status="SUCCESS"):
        self.txn_type = txn_type
        self.amount = amount
        self.description = description
        self.status = status

    def show(self):
        print(f"{self.txn_type} | ₹{self.amount} | {self.description} | {self.status}")
