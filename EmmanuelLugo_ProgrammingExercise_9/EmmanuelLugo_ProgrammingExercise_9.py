'''
Create a BankAcct Class that contains at least the following state information: name, account number, amount and interest rate. In addition to an __init__ method, the class should support methods for adjusting the interest rate, for withdrawing and depositing, and for giving a balance. You should also include a method to calculate the interest based on the number of days. Use the __str__ method to display balances and interest amounts. Create a test function to test the different methods in the BankAcct Class.

The class and test function should be in one .py file.

Submit your .py file in this assignment and in your repository.

You DO NOT NEED a technical design document for this assignment BUT YOU NEED TO SUBMIT A SCREENSHOT OF YOUR OUTPUT.
'''

class Bank_acct:
    def __init__(self, name, account_number,balance , rate, acct_age_in_days ):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = rate
        self.acct_age_in_days = acct_age_in_days

    def __str__(self):
        return f"{self.name}\n{self.account_number}\n{self.balance}\n{self.interest_rate}\n{self.acct_age_in_days}"

'''
We have to remove all the input code from each method. The class should only receive the data through args for this assignment.
'''
    def change_interest_rate(self):

        self.interest_rate = float(input("Please enter a new interest rate: "))

    def withdraw(self):
        self.balance -= float(input("Please enter a new balance: "))

    def deposit(self):
        self.balance += float(input("Please enter a new balance: "))

    def calculate_interest(self):
        accrued_interest = ((self.balance * self.interest_rate)/365)  * self.acct_age_in_days
        return accrued_interest


def test():
    acct_1 = Bank_acct()
    acct_2 = Bank_acct()
    acct_3 = Bank_acct()
