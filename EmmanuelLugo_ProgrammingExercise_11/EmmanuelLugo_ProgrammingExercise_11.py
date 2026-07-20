'''
Using the Deck object presented in Section 11.5, write a game program that deals a Poker hand of five cards. Then prompt the user to enter a series of numbers (for example: 1, 3, 5) that selects cards to be replaced during a draw phrase. Then print the result of drawing the new cards.

You should have at least two functions, but you can have more.

Submit your .py file in this assignment and in your repository.
'''

import random

# created the Deck class. Kinda just ripped straight out of the textbook as a good foundation.
class Deck():
    def __init__(self, size):
        self.cards = [i for i in range(size)]
        random.shuffle(self.cards)
        self.cards_in_play =[]
        self.cards_discarded = []

    def deal(self):
        if(len(self.cards)) < 1:
            random.shuffle(self.cards_discarded)
            self.cards = self.cards_discarded
            self.cards_discarded = []
        new_card = self.cards.pop()
        self.cards_in_play.append(new_card)
        return new_card

    def new_hand(self):
        self.cards_discarded += self.cards_in_play
        self.cards_in_play.clear()


# the poker function initiates the dealing/discarding/drawing
def poker(deck):

    #hand container to hold the cards we currently have
    hand = []

    # loop created to deal 5 cards and then prints them to show what we got.
    for card in range(5):
        hand.append(deck.deal())
    print(hand)

    print("You'll need to discard 3 cards. Remember, choose the position, not the card itself, so 1st card becomes 1, 2nd becomes 2, and so on.")

    # loop created to ask the user 3 times what 3 cards they want to discard
    for i in range(3):
        discard = input("Choose a card to discard and press enter.")
        if discard != "":
            index = int(discard) - 1
            hand.pop(index)
            hand.insert(index, deck.deal())

    deck.new_hand()
    print("your new hand: ", hand)
#of course the main function to kick it all off.
def main():
    
    my_deck = Deck(52)
    poker(my_deck)


if __name__ == '__main__':
    main()






