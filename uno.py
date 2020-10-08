from random import randint
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
COLORS = ["🔴","🟢","🟡","🔵" ]


class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def ___str___(self):
        return f"{self.color} {self.number}"   


class Player:
    def __init__(self, name):
        self.name = name 


class Deck:
    def __init__(self, numbers, colors):
        self.cards = []
        for number in numbers:
            for color in colors:
                card = (color, number)
                self.cards.append(card)
    def shuffle(self, cards):
        randomize_deck = []
        for card in cards:
            rand_number = randint(0, 39)
            if not cards[rand_number]:

                card = cards[rand_number]
                randomize_deck.append(card)
        return randomize_deck



class Game:
    pass