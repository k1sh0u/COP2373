'''
Write a program asking the user for a list of their monthly expenses. When asking the user for their expenses, ask for the type of expense and the amount. Use the reduce method to analyze the expenses and display the total expense, the highest expense and the lowest expense. Label what the highest and lowest expense is.

*You can use separate functions for your calculations or you can use lambda functions within your main function to do this.

You must also have a technical design document (refer to the Submitting Programming Exercises Module).

Submit both your .py file and .doc/.docx file in this assignment and these files must also be in your repository.


'''


def get_expense():
    expense_list = []
    while True:
        expense = input("Please enter the expense: /nWhen done, don't add- just enter.")
        expense_list.append(expense)

        return expense_list


get_expense()

