from payments.payment import Payment


class NetBankingPayment(Payment):

    def pay(self, amount, wallet):
        try:
            if wallet.deduct_money(amount, "Net Banking Payment"):
                print(f"₹{amount} paid using Net Banking")
            else:
                print("Net Banking Payment Failed ❌")

        except Exception as e:
            print("Net Banking Payment Error:", e)
