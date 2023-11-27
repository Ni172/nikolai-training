import random
from dataclasses import dataclass


@dataclass
class Card:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.rank}: {self.suit}'


class Deck:
    SUIT_LIST = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'Q', 'K', 'A']
    SUITS = ['HEART', 'CLUB', 'DIAMOND', 'SPADE']

    def __init__(self):
        self.deck: list[Card] = []
        for cart in self.SUIT_LIST:
            for suit in self.SUITS:
                self.deck.append(Card(cart, suit))

    def __str__(self):
        return str(self.deck)
    def __repr__(self):
        return str(self.deck)

    def __random_card(self):
        try:
            return random.choice(self.deck)
        except IndexError:
            return 'Empty'

    def take_card(self):
        card = self.__random_card()
        # print(card)
        if card != 'Empty':
            self.deck.remove(Card(card.rank, card.suit))
        else:
            print('The deck is empty')

# print(Card('4', 'CLUB'))
a = Deck()
a.take_card()
