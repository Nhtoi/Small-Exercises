import Cards as Cards
import random
import collections
Cards.createCard()
class Deck():
    deck = collections.deque([])
    def __init__(self):
        pass
    def createDeck():
        for card in Cards.Cards.cards:
            Deck.deck.append(card)
        shuffleDeck()
    def __str__(self): 
        return f"Cards in the Deck: {self.deck}"

def shuffleDeck():
    random.shuffle(Deck.deck)
