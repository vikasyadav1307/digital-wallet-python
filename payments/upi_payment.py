from payments.payment import Payment


class UpiPayment(Payment):

    def pay(self, amount, wallet, user_id):
        if wallet.deduct_money(amount, "UPI Payment", user_id):
            print(f"₹{amount} paid using UPI")
        else:
            print("UPI Payment Failed ❌")
