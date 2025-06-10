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
from collections import deque

player1, player2 = player.CreatePlayer()
isRunning = True
War = False

def Gameplay():
    global isRunning 
    while player1.playerDeck and player2.playerDeck and isRunning:
        if len(player1.playerDeck) < 1:
            print("Player 1 has Lost the Game")
            isRunning = False
            break
        elif len(player2.playerDeck) < 1:
            print("Player 2 has Lost the Game")
            isRunning = False
            break

        print("Player 1 is playing with", len(player1.playerDeck), "Cards")
        print("Player 2 is playing with", len(player2.playerDeck), "Cards")

        player1Card = player1.playerDeck.pop()
        player2Card = player2.playerDeck.pop()
        stack = []
        print("From Normal Rounds", player1Card.value, player2Card.value)

        if player1Card.value < player2Card.value:
            print("Player 2 has Won the Round")
            player2.playerDeck.appendleft(player2Card)
            player2.playerDeck.appendleft(player1Card)
            print("Player 1 now has", len(player1.playerDeck), "Cards")
            print("Player 2 now has", len(player2.playerDeck), "Cards")

        elif player1Card.value > player2Card.value:
            print("Player 1 has Won the Round")
            player1.playerDeck.appendleft(player2Card)
            player1.playerDeck.appendleft(player1Card)
            print("Player 1 now has", len(player1.playerDeck), "Cards")
            print("Player 2 now has", len(player2.playerDeck), "Cards")

        else:
            print("War is Starting")
            War = True
            stack.append(player1Card)
            stack.append(player2Card)
            print("From War", player1Card.value, player2Card.value)
            print(stack)

            while War and player1.playerDeck and player2.playerDeck:
                if len(player1.playerDeck) < 2:
                    print("Player 1 has Lost the Game")
                    isRunning = False
                    break
                elif len(player2.playerDeck) < 2:
                    print("Player 2 has Lost the Game")
                    isRunning = False
                    break

                stack.append(player1.playerDeck.pop())  
                stack.append(player2.playerDeck.pop()) 

                player1Card = player1.playerDeck.pop()  
                player2Card = player2.playerDeck.pop()  
                stack.append(player1Card)
                stack.append(player2Card)

                print("War Battle Cards:", player1Card.value, player2Card.value)

                if player1Card.value < player2Card.value:
                    for cards in stack:
                        player2.playerDeck.appendleft(cards)
                    print("War is Over, Player 2 Takes", len(stack), "cards")
                    stack = []
                    War = False

                elif player1Card.value > player2Card.value:
                    for cards in stack:
                        player1.playerDeck.appendleft(cards)
                    print("War is Over, Player 1 Takes", len(stack), "cards")
                    stack = []
                    War = False

                    if len(player1.playerDeck) < 1:
                        print("Player 1 has Lost the Game")
                        isRunning = False
                        break
                    if len(player2.playerDeck) < 1:
                        print("Player 2 has Lost the Game")
                        isRunning = False
                        break
                else:
                    print("Cards Match Again, Another War Starts")


Gameplay()