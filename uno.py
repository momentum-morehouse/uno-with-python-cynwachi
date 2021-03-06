import random

#Uno Game Python
"""
Generate the uno deck of 108 cards.
Red green blue yellow
one 0 card, two 1, 2, 3, 4, 5, 6, 7, 8, 9, D2, SK, RE; and four W, WD
Parameters: None 
Return values: deck -> list
"""
#Build Deck function 
def buildDeck():
    deck = [] #empty list 
    #example card: Red 7, Green 8, Blue SK
    colors = ["🔴","🟢","🟡","🔵" ] #This is a local variable so I need to restate it if using it later
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]
    wilds = ["Wild", "Wild Draw Four"]
    for color in colors:
        for value in values:
            cardVal = "{} {}".format(color, value) #The format method
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)
    for i in range(4): #Iterate over the range of 
        deck.append(wilds[0])
        deck.append(wilds[1])

    return deck

"""

Shuffles deck function to create a list of items passed into it
Parameters: deck => list
Return values: deck => list

"""

def shuffleDeck(deck):
    for cardPosition in range(len(deck)): #To interate over indeces of a sequence 
        randPosition = random.randint(0,107)
        deck[cardPosition], deck[randPosition] = deck[randPosition], deck[cardPosition]
    return deck
#Shuffle Deck function  complete here
#create a dealer function that deals x number of cards 
#create a data set that allows for viewing hands 
#==>Deal X cards to player
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
#showHands function to show hand
Print formatted (use format method) list of player's hand
Parameter: player = integer, playerHand = -> list
Return:None
"""
def showHand(player, playerHand):
    print("Player {}' Turn".format(player+1))
    print("Your Hand")
    print('==============')
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
        # testing splitCard = card.split(' ',1) 
        if "Wild" in card:
            return True
        elif color in card or value in card:
            return True
    return False


unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)
unoDeck = shuffleDeck(unoDeck) #shuffle twice
discards = [] #emtpy list 
print(unoDeck) # dont think I need this printed # but it prints the built and shuffled deck named unoDeck

#2.0print("Enter number of players to begin")
players = []
colors = ["🔴","🟢","🟡","🔵" ]
numPlayers = int(input("How many players?"))
while numPlayers<2 or numPlayers>4:
    numPlayers = int(input("Try Again. Use a number between 2-4 How many players?"))
for player in range(numPlayers):
    players.append(drawCards(5))

playerTurn = 0 

playDirection = 1 #comes out in later lists, indexes to control direction as (the sum or divisor of a number)
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
        print("You cant play. Draw a card.")
        players[playerTurn].extend(drawCards(1))
    print("")
    
#check for special cards #=>Apply card Effects

# Apply the state to the Reverse card
    splitCard = discards[0].split(" ", 1)
    currentColor = splitCard[0] #
    if len(splitCard) == 1:
        cardVal = "Any" #the value of the card is True
    else:
        cardVal = splitCard[1]
    if currentColor == "Wild": #assigning wild a color
        for x in range(len(colors)):
            print("{}) {}".format(x+1, colors[x])) #print list of colors 
        newColor = int(input("What color would you like to choose? ")) #choosing a new color based on what we printed
        while newColor < 1 or newColor > 4: #printed list of available color
            newColor = int(input("Wrong, Choose a color")) #Verify entry 
        currentColor = colors[newColor-1] # take the 1 and subtract 1 to makes current color == to string refers to the index of colors
    if cardVal == "Reverse":    #this is the string that was made [newColor-1]
        playDirection = playDirection * -1 #makes playDirection become to 1 if already used them makes it 1 chaging payer turn based on play direction
    elif cardVal == "Skip":
        playerTurn += playDirection #increses/decreases play direction by another 1
    elif cardVal == "Draw Two":
        players[playerTurn.extend(drawCards(2))]
    elif  cardVal == "Draw Four":
        players[playerTurn.extend(drawCards(4))]

  playerTurn += playDirection # if play direction is - then chagin player turn based on play directon makes it go down 
    if playerTurn == numPlayers:
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = numPlayers-1






#Play Card
#=> Play Card 2.o
#=>Have a user choose a card to play
#=>Validate card played

#==>Version 3.0

#==>Skip a turn
#==>Reverse order
#=>Check for uno or win condition
#==>End Game 
#Keep Track of turns
#Keep Track of color and number 


