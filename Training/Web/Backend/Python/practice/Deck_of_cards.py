import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self. value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'


# class Deck:
#     suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
#     values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']
#     cards_in_hand = []
#
#     def __init__(self, qty):
#         self.cards = Deck.gen_cards(qty)
#         self.__packs = qty
#
#     def __repr__(self):
#         return f'Deck of {self.__packs} cards'
#
#     def count(self):
#         if self.__packs == len(self.cards):
#             return 'The deck is full'
#
#         return len(self.cards)
#
#     def shuffle(self):
#         if self.count() < self.__packs:
#             raise ValueError('Only full deck can be shuffle')
#         random.shuffle(self.cards)
#
#
#     def _deal(self, qty = None):
#         count = self.count()

#         if qty:
#             if count >= qty:
#                 new_deal_cards = self.cards[-qty:]
#                 for card in new_deal_cards:
#                     self.cards.remove(card)
#                 Deck.cards_in_hand.extend(new_deal_cards)
#             elif count:
#                 Deck.cards_in_hand.extend(self.cards[-qty:])
#                 self.cards.clear()
#             else:
#                 raise ValueError('All cards have being dealt')
#         if Deck.cards_in_hand:
#             return Deck.cards_in_hand
#         else:
#             raise ValueError('No cards in hand to deal')
#
#     def deal_hand(self, quatity=None):
#         return self._deal(quatity)
#
#     def deal_card(self):
#         new_choice = random.choice(self._deal())
#         self._deal().remove(new_choice)
#         return new_choice
#
#     @classmethod
#     def gen_cards(cls, packs):
#         card_per_suit = int(packs / len(cls.suits))
#
#         num, faces = cls.values[:card_per_suit-3], cls.values[-3:]
#
#         new_values = [*num,*faces]
#
#         # card_list = []
#         #
#         # for suit in cls.suits:
#         #     for value in new_values:
#         #         card_list.append(Card(suit, value))
#
#         #  ===> OR
#
#         card_list = [Card(suit, value) for suit in cls.suits for value in new_values]
#         return card_list
#
#
# new_deck = Deck(28)
#
# new_deck.shuffle()
#
# print(new_deck)
#
# print(new_deck.deal_hand(3))
#
# print(new_deck.deal_card())
# print(new_deck.deal_card())
# # print(new_deck.deal_card())
# print(new_deck.deal_hand(5))
# print(new_deck.deal_card())
#
#
# print(new_deck)
#
#
#

# # ---------------------------> Correction

class Deck:
    def __init__(self, qty):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']

        card_per_suit = int(qty / len(suits))
        num, faces = values[:card_per_suit-3], values[-3:]
        new_values = [*num, *faces]

        self.cards = [Card(suit, value) for suit in suits for value in new_values]
        self._deck_qty = qty

    def __repr__(self):
        print(self.cards)
        return f'Deck of {self._deck_qty} cards'

    def count(self):
        return len(self.cards)

    def _deal(self, qty=None):
        count = self.count()
        if count is 0:
            raise ValueError('All cards have being dealt')

        # For deal cards
        if qty:
            actual_cards = min(count, qty)
            new_deal_cards = self.cards[-actual_cards:]
            self.cards = self.cards[:-actual_cards]
            Deck.cards_in_hand.extend(new_deal_cards)

        # For deal cards
        if Deck.cards_in_hand:
            return Deck.cards_in_hand
        else:
            raise ValueError('No cards in hand to deal')


print(Deck(52))

















