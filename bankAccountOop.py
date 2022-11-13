class BankAccount():

    def __init__(self, balance = 0.0):
        self.balance = balance

    def displayBalance(self):
        print(f'Your balance is {self.balance}.')

    def withdrawCash(self):
        withdrawalAmount = float(input("The amount of cash you want to withdraw is?"))
        if (withdrawalAmount > self.balance):
            print(f'Your balance {self.balance} is less than the amount you want to withdraw')
        else:
            self.balance = self.balance - withdrawalAmount
            print(f'Withdrawal successful. Remaining balance is {self.balance}.')
    
    def depositCash(self):
       depositAmount = float(input("The amount of cash you want to withdraw is?"))
       self.balance += depositAmount