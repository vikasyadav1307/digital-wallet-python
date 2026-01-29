class WalletService:

    def add_money(self, wallet, amount, user_id):
        wallet.add_money(amount, user_id)
        print(f"₹{amount} added to wallet")

    def pay_money(self, wallet, amount, description, user_id):
        if wallet.deduct_money(amount, description, user_id):
            print(f"₹{amount} paid successfully")
        else:
            print("Payment Failed ❌")
