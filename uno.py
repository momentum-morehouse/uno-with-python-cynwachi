from random import randint
#pretty_suits = {
#    'Spade': '\u2664',
#    'Club': '\u2667',
#    'Heart': '\u2661',
#    'Diamond': '\u2662'
#    }
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


class makeDeck:
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

#Dealer deals 7 cards to each player


