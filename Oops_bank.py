#object oriented programming concepts create a bank account using python
class MyBank_Account:
    def __init__(self):
        self.balance = 0
        print("Welcome to MyBank_Account and you can Withdrawal Machine")
    def Deposit(self):
        amount=float(input("Enter your amount to be Deposited: "))
        self.balance+=amount
        print("Enter your amount to be Deposited: ", amount)
    def Withdrawal(self):
        amount=float(input("Enter your amount to be Withdrawal: "))
        if self.balance>=amount:
            self.balance-=amount
            print("Your Withdrawal: ", amount)
        else:
            print("Check your Balance: ")
    def Display(self):
        print("Net Available Balance", self.balance)
#creating an object of class an amount
A=MyBank_Account()
#Calling function of an class that
A.Deposit()
A.Withdrawal()
A.Display()




