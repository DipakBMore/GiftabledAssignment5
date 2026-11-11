class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Current balance:", self._balance)

    def get_balance(self):
        return self._balance

account= Bank("A", 100)
account.get_balance()
account.deposit(50) 
account.get_balance()  