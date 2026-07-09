'''
Create a BankAcct Class that contains at least the following state information: name, account number, amount and interest rate. In addition to an __init__ method, the class should support methods for adjusting the interest rate, for withdrawing and depositing, and for giving a balance. You should also include a method to calculate the interest based on the number of days. Use the __str__ method to display balances and interest amounts. Create a test function to test the different methods in the BankAcct Class.

The class and test function should be in one .py file.

Submit your .py file in this assignment and in your repository.

You DO NOT NEED a technical design document for this assignment BUT YOU NEED TO SUBMIT A SCREENSHOT OF YOUR OUTPUT.
'''

class Bank_acct:
    def __init__(self, name, account_number, interest_rate ):
        self.name = name
        self.account_number = account_number
        self.interest_rate = interest_rate

    