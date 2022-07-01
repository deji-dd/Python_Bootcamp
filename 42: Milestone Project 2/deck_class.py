import card_class
import global_variables
import random
class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in global_variables.suits:
            for rank in global_variables.ranks:
                self.deck.append(card_class.Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for x in self.deck:
            deck_comp += f"\n {card_class.Card.__str__(x)}"
        return f"The deck has:{deck_comp}"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card
