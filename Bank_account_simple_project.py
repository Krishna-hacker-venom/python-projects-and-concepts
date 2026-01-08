class Bank_account:
    def __init__(self, account_number, owner, balance = 0):
        self.balance = balance
        self.account_number = account_number
        self.owner = owner
        self.amount = amount
        
    def deposit(self, amount):
        self.balance += amount
        print(f"you added amount {self.balance} . Total amount in your account is {amount}")
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"insufficent balance!!")
    
    def display(self):
         print(f"Owner : {self.owner}, Account : {self.account_number}")
        
acc = Bank_account("12345","Krishna", 500)
acc.deposit(200)
acc.display()
