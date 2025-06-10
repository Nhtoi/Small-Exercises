class Cards():
    mappings = {13:"King",
                12:"Queen",
                11:"Jack"} 
    cards = []
    def __init__(self, house, value):
        self.value = value
        self.house = house
        Cards.cards.append(self)

    def __str__(self):
        name = self.mappings.get(self.value, str(self.value))
        return f"House: {self.house} Value: {name}"

    def __repr__(self):
        return self.__str__()
    
def createCard():
        houses = ["Spades", "Hearts", "Clubs","Diamond"]
        values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        for house in houses:
            for value in values:
                card = Cards(house, value)
               
