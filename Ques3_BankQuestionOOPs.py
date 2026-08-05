class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        self._balance =  self._balance + amount
        print("total amount:", self._balance)

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance = self._balance - amount
            print(" total amount:", self._balance)
        else:
            print("Insufficient balance!")

    def get_summary(self):
        print("total_amount :", self._balance)
        print("owner name:", self.owner)

class SavingAccount(BankAccount):
    def __init__(self, owner, balance,interest_rate, time):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.time = time

    def apply_interest(self):
        interest = (self._balance * self.interest_rate * self.time ) / 100
        self._balance = self._balance + interest
        print("interest:", interest)
        print("Total amount after applying rate of ", self.interest_rate, "% and for ", self.time, "years, amount:", self._balance)


s1 = SavingAccount("Dholu", 7500, 5, 2)
s1.get_summary()
s1.deposit(2500)
s1.apply_interest()
