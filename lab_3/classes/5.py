class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successful deposit! The new balance is: {self.balance}")
        else:
            print("Enter the correct amount for making a deposit.")

    def withdrawal(self, amount):
        if amount > self.balance:
            print("You don't have enought resources.")
        elif(amount <= 0):
            print("Enter the positive amount of money!")
        else:
            self.balance -= amount
            print(f"Successful withdrawal! The new balance is {self.balance}")

        

bank_account = Account('John', 4000)
bank_account.deposit(200)
bank_account.deposit(400)
bank_account.deposit(500)

bank_account.withdrawal(100)
bank_account.withdrawal(150)
bank_account.withdrawal(250)

