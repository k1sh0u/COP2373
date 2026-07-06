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
"""
Two main variables to track how many buyers and how many available tickets at start
and after each purchase.
"""



"""
ticket_sign function designed to take both variables and determine 
if any tickets are available for purchase, and depending on availability
will call the buy_a_ticket function.
will not allow buyer to purchase once ticket_suppy is 0 and then will 
print accumulated number of buyers.
"""
def ticket_sign(ticket_supply, buyers):
    buyers = 0
    ticket_supply = 20

    if ticket_supply >= 1:
        print(f"Welcome! We have {ticket_supply} tickets left.")
        buy_a_ticket(ticket_supply,buyers)
    else:
        print("we are sold out.")
        print(f"Total buyers: {buyers}")

"""
buy_a_ticket function designed to take two variables and validate the input value type and
and then allow the buyer to purchase inline with the purchasing guidelines.
accumulates buyers after each purchase. 
"""
def buy_a_ticket(ticket_supply, buyers):
    while True:

        try:
            tickets_to_buy = int(input("How many tickets would you like?: "))
        except ValueError:
            print("Input must be a number.")
            continue
        if tickets_to_buy > 4:
            print("4 tickets Max per customer.")
        elif tickets_to_buy < 1:
            print("You cannot buy less than 1 ticket.")
        elif tickets_to_buy > ticket_supply:
            print(f"there are only {ticket_supply} tickets left.")
        else:
            print(f"You have purchased {tickets_to_buy} tickets.")
            return ticket_supply



"function called immediately initiates the process."
ticket_sign(ticket_supply,buyers)




