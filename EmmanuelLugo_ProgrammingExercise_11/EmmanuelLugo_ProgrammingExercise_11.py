'''
Using the Deck object presented in Section 11.5, write a game program that deals a Poker hand of five cards. Then prompt the user to enter a series of numbers (for example: 1, 3, 5) that selects cards to be replaced during a draw phrase. Then print the result of drawing the new cards.

You should have at least two functions, but you can have more.

Submit your .py file in this assignment and in your repository.
'''

import random

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
        self.cards_discards += self.cards_in_play
        self.cards_in_play.clear()

def poker(deck):
    hand = []
    for card in range(5):
        hand.append(deck.deal())
    print(hand)

    user_discarded = input("Discard which cards? Choose 3 and enter the position of the cards, not the actual cards)")
    