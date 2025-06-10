"""Each player turns up a card at the same time and the player 
with the higher card takes both cards and puts them, face down, 
on the bottom of his stack.
If the cards are the same rank, it is War. 
Each player turns up one card face down and one card face up. 
The player with the higher cards takes both piles (six cards). 
If the turned-up cards are again the same rank, each player places another card face down and turns another card face up. 
The player with the higher card takes all 10 cards, and so on.
The game ends when one player has won all the cards.
"""
import Player as player
#create players with decks, points, and name player2 DEFAULT NAME = CPU
player1, player2 = player.CreatePlayer()

for cards in player2.playerDeck:
    print(player2.name , cards)
for cards in player1.playerDeck:
    print(player1.name , cards)


pile = []


