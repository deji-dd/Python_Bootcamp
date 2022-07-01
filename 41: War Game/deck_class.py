import random
import card_class


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in card_class.suits:
            for rank in card_class.ranks:
                created_card = card_class.Card(suit, rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
