"""
Write an application to pre-sell a limited number of cinema tickets. Each buyer can buy up to 4 tickets.
No more than 20 tickets can be sold total.
Prompt the user for the desired number of tickets and then display the number of remaining tickets after their purchase.
Repeat until all tickets have been sold. Then display the total number of buyers.

Please use the following in your code:

two functions - your choice how you want to design this
input
output
accumulator
if statement
loop
You must also have a technical design document (refer to the Submitting Programming Exercises Module).

Submit both your .py file and .doc/.docx file in this assignment and these files must also be in your repository.
"""

ticket_supply = 20

def ticket_tracker(tickets_ordered):
    if tickets_ordered >= ticket_supply:
        return True
    else:
        return False



def buy_a_ticket():
    print(f"Hello, there are currently {ticket_supply} tickets available.")

    tickets_to_buy = int(input:("How many tickets would you like?"))
    if not ticket_tracker(tickets_to_buy):
        return "sold out."
    elif tickets_to_buy > 4:
        return "4 tickets Max per customer."
    else:
        return f"You have purchased {tickets_to_buy} tickets."
        ticket_supply -= tickets_to_buy


buy_a_ticket()




        if
