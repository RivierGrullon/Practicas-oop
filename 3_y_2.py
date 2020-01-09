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
        s = int(input('what card do u want to discard?'))
        if s == 1:
            undonedeck.Uncards.append(self.hand.pop(0))
            undonedeck.show_undeck()
            self.show_hand()
        elif s == 2:
            undonedeck.Uncards.append(self.hand.pop(1))
            undonedeck.show_undeck()
            self.show_hand()
        elif s == 3:
            undonedeck.Uncards.append(self.hand.pop(2))
            undonedeck.show_undeck()
            self.show_hand()
        elif s == 4:
            undonedeck.Uncards.append(self.hand.pop(3))
            undonedeck.show_undeck()
            self.show_hand()
        elif s == 5:
            undonedeck.Uncards.append(self.hand.pop(4))
            undonedeck.show_undeck()
            self.show_hand()
        else:
            undonedeck.Uncards.append(self.hand.pop(5))
            undonedeck.show_undeck()
            self.show_hand()
    def drop_cards(self):
        z = input('do u want take a card from deck or undonedeck? ')
        if z == 'deck':
            self.hand.append(deck.show_drop())
            self.show_hand()
        elif z == 'undonedeck':
            self.hand.append(undonedeck.Uncards.pop())
            self.show_hand()


class Undone_deck(object):
    def __init__(self,deck):
        self.Uncards = []
        self.Uncards.append(deck.show_drop())

    def show_undeck(self):
        self.Uncards[-1].show()

deck = Deck()
deck.barajar()
undonedeck = Undone_deck(deck)
player = Player(input('Introduce your name: '))
undonedeck.show_undeck()
# # # deck.show()
# deck.show()

player.take_hand(deck)
player.show_hand()
player.drop_cards()
player.discard()
# jose = Player("Jose Esteban")
# jose.take_hand(deck)
# jose.show_hand()
# card.show()
