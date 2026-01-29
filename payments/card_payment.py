from payments.payment import Payment


class CardPayment(Payment):

    def pay(self, amount, wallet, user_id):
        if wallet.deduct_money(amount, "Card Payment", user_id):
            print(f"₹{amount} paid using Card")
        else:
            print("Card Payment Failed ❌")
