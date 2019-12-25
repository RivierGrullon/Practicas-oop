from random import shuffle


class Card(object):
    #start the value of the cards
    def __init__(self,face,val):
        self.face = face
        self.val = val
    
 
 
    def show(self):
        #Change the value of the special cards
        if self.val == 1:
            val = "A"
        elif self.val == 11:
            val = "J"
        elif self.val == 12:
            val = "Q"
        elif self.val == 13:
            val = "K"
        #Show the cards
        else:
            val = self.val

        print("{} de {}".format(val,self.face))


#constructor of deck
class Deck(object):
    def __init__(self):
        self.cards = []
        self.build_deck()
    def build_deck(self):
        
        for w in ["♠","♥","♦","☘"]:
            for v in range(1,14):
                self.cards.append(Card(w,v))
                 
             
    #Shuffle the deck 
    def barajar (self):
        shuffle(self.cards)   
        return self.cards

    def show(self):
        for c in self.cards:
            c.show()
    #Take a card from the deck
    def show_drop(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name
    #take cars per player

    def take_hand(self,deck,cards_per_playes = 5):
        for _ in range(cards_per_playes):
            self.hand.append(deck.show_drop())
        return self
    #Shows the player's hand

    def show_hand(self):
        print("{}'s hand".format(self.name))
        for cards in self.hand:
            cards.show()

    def discard(self):
        return self.hand.pop()   


class Undone_deck(object):
    def __init__(self,deck):
        self.Uncards = []
        self.Uncards.append(deck.show_drop())
   
    def show_undeck(self):
        for cards in self.Uncards:
            cards.show()

deck = Deck()
deck.barajar()
undonedeck = Undone_deck(deck)
undonedeck.show_undeck()
# # # deck.show()
# deck.show()
# rivier = Player("Rivier")
# rivier.take_hand(deck) 
# rivier.show_hand()
# jose = Player("Jose Esteban")
# jose.take_hand(deck)
# jose.show_hand()
# card.show()