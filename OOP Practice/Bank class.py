class Bank:
    def __init__(self, acc_holder, balance=0):
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return f"{amount} Rs. deposited successfully !"
    
    def withdraw(self,amount):
        if amount > self.balance:
            return f"Insufficient funds ! Current balance : {self.balance}"
        elif amount < self.balance:
            self.balance -= amount
            return f"{amount} Rs. withdrawn successfully !!"
        else:
            return "Some error has occured, please try again !"
        
    def display_balance(self):
        return f"Name of acc holder : {self.acc_holder}\nCurrent balance : {self.balance}"
    
acc1 = Bank('Alok',10000)
print(acc1.deposit(5000))
print(acc1.withdraw(6000))
print(acc1.display_balance())