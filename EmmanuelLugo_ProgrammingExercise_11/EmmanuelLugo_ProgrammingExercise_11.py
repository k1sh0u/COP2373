'''
Using the Deck object presented in Section 11.5, write a game program that deals a Poker hand of five cards. Then prompt the user to enter a series of numbers (for example: 1, 3, 5) that selects cards to be replaced during a draw phrase. Then print the result of drawing the new cards.

You should have at least two functions, but you can have more.

Submit your .py file in this assignment and in your repository.
'''

import random

class Deck():
    def __init__(self, n_decks = 1):
        self.n_decks = n_decks
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        rank =[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]