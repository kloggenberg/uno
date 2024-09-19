from card import Card

class Deck:
    def __init__(self):
        self.colours = ["Yellow", "Green", "Blue", "Red"]
        self.numbers = list(range(0,10))
        self.special_list = ["reverse","+2","skip"]
        self.wild_list = ["wild +4","wild"]
        self.cards =[]

        
    def make_deck(self):
        self.make_number_cards()
        self.make_wild_cards()
    
    
    def make_number_cards(self):
        for colour in self.colours:
            
            for number in self.numbers:
                if number == 0:
                    card = Card(colour,number)
                    self.cards.append(card)
                else:
                    for _ in range(0,2):
                        card = Card(colour,number)
                        self.cards.append(card)
            
            for x in self.special_list:
                    for _ in range(0,2):
                        card = Card(colour,x)
                        self.cards.append(card)
    
        for _ in range(0,4):
            for value in self.wild_list:
                card = Card(value=value)
                self.cards.append(card)
            
    
        
    def show_cards(self):
        for card in self.cards:
            print(card.get_card())