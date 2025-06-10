import Deck as deck

class Player():
    deck = deck.Deck.createDeck()
    def __init__(self, name, points, playerDeck):
        self.name = name
        self.playerDeck = playerDeck
        self.points = points

    def __str__(self):
        return f"Player: {self.name}, Deck: {self.playerDeck} Points: {self.points}"
    
def CreatePlayer():
        name = input("Choose your Name: ")
        points = 0
        mid = len(deck.Deck.deck) // 2
        playerDeck = deck.Deck.deck[:mid]
        player1 = Player(name, points, playerDeck)
        player2 = Player("CPU", 0, deck.Deck.deck[mid:])
        return player1, player2
def printPlayerInfo():
    if Player.player:
        for player in Player.player:
             print(player)
    else:
         print("No Player")

# CreatePlayer()
# printPlayerInfo()

