'''
Write a program asking the user for a list of their monthly expenses. When asking the user for their expenses, ask for the type of expense and the amount. Use the reduce method to analyze the expenses and display the total expense, the highest expense and the lowest expense. Label what the highest and lowest expense is.

*You can use separate functions for your calculations or you can use lambda functions within your main function to do this.

You must also have a technical design document (refer to the Submitting Programming Exercises Module).

Submit both your .py file and .doc/.docx file in this assignment and these files must also be in your repository.


'''
from functools import reduce


def main():
    expenses_list = get_expenses()

    if not expenses_list:
        print("No expenses entered.")
        return

    sorted_expenses = reduce(sort_expenses, expenses_list)

    print(sorted_expenses)



def get_expenses():
    expense_list = []

    expense ="placeholder"
    expense_amount = "placeholder"

    while True:
        expense = input("Please enter the expense: When done, don't add anything- just enter.")
        if expense == "":
            break

        expense_amount = int(input("How much goes toward that expense?: "))

        add_to_list = (expense, expense_amount)
        expense_list.append(add_to_list)
    return expense_list

def sort_expenses(list):


    highest_expense_value = 0
    highest_expense_item = ""
    lowest_expense_value = highest_expense_value
    lowest_expense_item = ""
    expense_total = 0
    for x, y in list:
        expense_total += y

        if(y > highest_expense_value):
            highest_expense_value = y
            highest_expense_item = x

        if(y < lowest_expense_value):
            lowest_expense_value = y
            lowest_expense_item = x
    return f"Total cost of expenses: {expense_total}, Your highest expense is {highest_expense_item} which costs: {highest_expense_value}, and lowest expense is {lowest_expense_item} which costs: {lowest_expense_value}"









main()

