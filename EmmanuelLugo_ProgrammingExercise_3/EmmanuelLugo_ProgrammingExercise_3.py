'''
Write a program asking the user for a list of their monthly expenses. When asking the user for their expenses, ask for the type of expense and the amount. Use the reduce method to analyze the expenses and display the total expense, the highest expense and the lowest expense. Label what the highest and lowest expense is.

*You can use separate functions for your calculations or you can use lambda functions within your main function to do this.

You must also have a technical design document (refer to the Submitting Programming Exercises Module).

Submit both your .py file and .doc/.docx file in this assignment and these files must also be in your repository.


'''
def main():
    expenses_list = get_expenses()
    sorted_expenses = expenses_list.reduce(sort_expenses)

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

def sort_expenses():
    
    expense_list = []
    expense_amount = "placeholder"



get_expenses()

