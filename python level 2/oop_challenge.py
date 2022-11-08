class bankAccount():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def __repr__(self):
        return f"owner:{self.owner},balance:{self.balance}"

    def withdraw(self,withdraw):
        if self.balance>=withdraw:
          self.balance=self.balance-withdraw 

        else:
            print("no money")
    def deposit(self,dep_amount):
        self.balance=self.balance+dep_amount       
x=bankAccount('hamas',12000)
print(x)        