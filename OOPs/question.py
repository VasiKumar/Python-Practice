class Account:
    def __init__(self,balance,number):
        self.balance=balance
        self.number=number

    def debit(self,amount):
        self.amount=amount
        self.balance+=self.amount
    def credit(self,removed):
        self.removed=removed
        self.balance-=self.removed

    def printing(self):
        print(self.balance," is balance for Account number ",self.number)

s1=Account(50000,354)
s1.debit(3000)
s1.printing()
s1.credit(7000)
s1.printing()