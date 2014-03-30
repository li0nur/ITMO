# coding: utf-8

from random import shuffle, choice


class Card(object):
    """представляет игральную карту.
        атрибуты: suit (масть) и rank (ранг карты)"""

    suits = ["Пк", "Трф", "Чрв", "Ббн"]
    ranks = {6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "В", 12: "Д", 13: "К", 14: "Т"}
    #ranks = ["6", "7", "8", "9", "10", "В", "Д", "К", "Т"]
    trump = None

    def __cmp__(self, other):
#        c1 = self.trump, self.rank
#        c2 = other.trump, other.rank
        c1 = self.trump, self.rank, self.suit
        c2 = other.trump, other.rank, self.suit
        return cmp(c1, c2)

    def __init__(self, suit=0, rank=12, trump=None):
        self.suit = suit
        self.rank = rank
        self.trump = trump

    def __str__(self):
        return "%s-%s" % (Card.ranks[self.rank], Card.suits[self.suit])


class Deck(object):
    """представляет колоду карт."""

    @property
    def trump(self):
        return self.trump

    @trump.setter
    def trump(self, trump):
        for card in self.cards:
            if card.suit == trump.suit:
                card.trump = card.suit

    def shuffle(self):
        shuffle(self.cards)

    def chooseTrump(self):
        trump = choice(self.cards)
        self.cards.pop(self.cards.index(trump))
        self.cards.insert(0, trump)
        return trump

    def moveCard(self, num=-1):
        return self.cards.pop(num)

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in range(4) for rank in range(6, 15)]
        #self.cards = [Card(suit, rank) for suit in range(4) for rank in range(9)]
        self.__trump = ''

    def __str__(self):
        res = [str(card) for card in self.cards]
        return " | ".join(res)


class Person(object):

    @staticmethod
    def deanonimise(name):
        print "Hello,", name
        return name

    @classmethod
    def sortCard(cls, hand):
        hand.sort()


class Hand(Deck):
    """представляет набор игральных карт в руке."""

    def addCard(self, card):
        self.cards.append(card)

    def __init__(self):
        self.cards = []