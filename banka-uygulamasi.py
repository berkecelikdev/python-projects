from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.__balance = balance 

    @abstractmethod
    def display_info(self):
        #Must be implemented by all subclasses.
        pass

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New Balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}. Remaining Balance: ${self.__balance}")
            return True
        print("Insufficient funds or invalid amount!")
        return False


class CurrentAccount(Account):
    def display_info(self):
        return f"Current Account - Owner: {self.owner}, Balance: ${self.get_balance()}"

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def display_info(self):
        return f"Savings Account - Owner: {self.owner}, Interest: {self.interest_rate}%, Balance: ${self.get_balance()}"
    

def print_account_details(account):
    print(account.display_info())

acc1 = CurrentAccount("John Doe", 1500.0)
acc2 = SavingsAccount("Jane Smith", 3000.0, 4.5)

acc1.deposit(500)
acc2.withdraw(200)

print("-" * 40)
print_account_details(acc1)
print_account_details(acc2)

