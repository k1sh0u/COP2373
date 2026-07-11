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

    def change_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def calculate_interest(self):
        accrued_interest = ((self.balance * self.interest_rate)/365)  * self.acct_age_in_days
        return accrued_interest

