# Encapsulation : The concept of wrapping data and methods that work on that data within one unit, e.g., a class in Python. 
# It restricts direct access to some of an object's components, which can prevent the accidental modification of data.

# Example :
# Create Account class with 2 attributes - balance and account_number.
# create methods for debit, credit and get_balance. 

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = initial_balance        # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance or invalid withdrawal amount")

    def get_balance(self):
        return self.__balance
    
# Creating an instance of BankAccount
my_account = BankAccount("123456789", 1000)
my_account.deposit(500)
my_account.withdraw(200)
print("Current Balance:", my_account.get_balance())
