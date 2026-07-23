'''
Create a BankAcct Class that contains at least the following state information: name, account number, amount and interest rate. In addition to an __init__ method, the class should support methods for adjusting the interest rate, for withdrawing and depositing, and for giving a balance. You should also include a method to calculate the interest based on the number of days. Use the __str__ method to display balances and interest amounts. Create a test function to test the different methods in the BankAcct Class.

The class and test function should be in one .py file.

Submit your .py file in this assignment and in your repository.

You DO NOT NEED a technical design document for this assignment BUT YOU NEED TO SUBMIT A SCREENSHOT OF YOUR OUTPUT.
'''

#creating the Bank Account class
class Bank_acct:

    # using the __init__ to make sure every instance of the bank_acct class supports the same set of variables
    def __init__(self, name, account_number,balance, rate, acct_age_in_days ):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = rate
        self.acct_age_in_days = acct_age_in_days

    #string to return the account details as text.
    def __str__(self):
        return f"{self.name}\n{self.account_number}\n{self.get_balance}\n{self.interest_rate}\n{self.acct_age_in_days}\n{self.calculate_interest()}"

    #function designed to return the current balance of the account for the user.
    def get_balance(self):
        return balance

    # function designed to change the interest rate of the account.
    def change_interest_rate(self,new_rate):
        self.interest_rate = new_rate

    #function designed to subtract money from the balance.
    def withdraw(self, amount):
        self.balance -= amount
    #function designed to add money to the balance.
    def deposit(self, amount):
        self.balance += amount

    # Calculates the interest dollar amount to display it in the summary
    def calculate_interest(self):
        accrued_interest = ((self.balance * self.interest_rate)/365)  * self.acct_age_in_days
        return accrued_interest

# test function designed to test the methods of the class object.
def test():
    acct_test = Bank_acct("Emmanuel Lugo",1001,200.00,0.18,30)
    print(acct_test)

    #using the methods created
    acct_test.change_interest_rate(.05)
    acct_test.withdraw(100)
    acct_test.deposit(2000)

    # printing the results of the outputs.
    print("Here are the new values: ")
    print(acct_test)


test()


