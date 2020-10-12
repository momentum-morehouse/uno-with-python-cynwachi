import random

#Uno Game Python
"""
Generate the uno deck of 108 card.
Red green blue yellow
one 0 card, two 1, 2, 3, 4, 5, 6, 7, 8, 9, D2, SK, RE; and four W, WD
Parameters: NOnoe 
Return values: deck -> list
"""
#Build Deck function 
def buildDeck():
    deck = []
    #example card: Red 7, Green 8, Blue SK
    colors = ["Blue", "Red", "Yellow", "Green"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]
    wilds = ["Wild", "Wild Draw Four"]
    for color in colors:
        for value in values:
            cardVal = "{} {}".format(color, value)
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])

    return deck

"""

Shuffles deck function to create a list of items passed into it
Parameters: deck => list
Return values: deck => list

"""

def shuffleDeck(deck):
    for cardPosition in range(len(deck)):
        randPosition = random.randint(0,107)
        deck[cardPosition], deck[randPosition] = deck[randPosition], deck[cardPosition]
    return deck
#Shuffle Deck function  complete here
#create a dealer function that deals x number of cards 
#create a data set that allows for viewing hands 
"""Draw card function that draws a specified number of cards off the top of the deck 
Parameters: numbCards => interger
Return: cardsDrawn =>
"""
def drawCards(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn
"""
#View hands function to show hand
Print formatted list of player's hand
Parameter: player = integer, playerHand = -> list
Return:None
"""
def showHand(player, playerHand):
    print("Player {}".format(player+1))
    print("Your Hand")
    print('========')
    y = 1
    for card in playerHand:
        print("{}) {}".format(y,card))
        y+=1
        print("")

"""
#Discard function that tells when a player can play = True

Check whether a player is able to play a card, or not 
Parameters: color-> string -> value string  , playerHand = > list
Return:
"""

def canPlay(color, value, playerHand):
    for card in playerHand:
        splitCard = card.split(' ',1) 
    if "Wild" in card:
        return True
    elif color in card or value in card:
        return True
    return False


unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)
unoDeck = shuffleDeck(unoDeck)
print(unoDeck)


players = []
discards = []
numPlayers = int(input("How many players?"))
while numPlayers<2 or numPlayers>4:
    numPlayers = int(input("Try Again. Use a number between 2-4. How many players?"))
for player in range(numPlayers):
    players.append(drawCards(5))

playerTurn = 0 
playDirection = 1
playing = True
discards.append(unoDeck.pop(0))
splitCard = discards[0].split(" ", 1)
currentColor = splitCard[0]
if currentColor != "Wild":
    cardVal = splitCard[1]
else:
    cardVal = "Any"

while playing:
    showHand(playerTurn, players[playerTurn])
    print("Card on top of discard pile: {}".format(discards[-1]))
    if canPlay(currentColor, cardVal, players[playerTurn]):
        cardChosen = int(input("Which card do you want to play? "))
        while not canPlay(currentColor, cardVal,[players[playerTurn][cardChosen-1]]):
            cardChosen = int(input("Not a valid card. Which card do you want to play?"))
        discards.append(players[playerTurn].pop(cardChosen-1))
    else:
        print("You cant play. You need to draw a card.")
        players[playerTurn].extend(drawCards(1))
    playerTurn += playDirection







#Play Card
#=> Play Card 2.o
#=>Have a user choose a card to play
#=>Validate card played
#=>Apply card Effects
#==>Version 3.0
#==>Deal X cards to player
#==>Skip a turn
#==>Reverse order
#=>Check for uno or win condition
#==>End Game 
#Keep Track of turns
#Keep Track of color and number 


