from Classes.Blackjack import *
from Classes import Blackjack

class Chips:
    def __init__(self, total):
        self.total = total


class Hand:
    def __init__(self,handnum, status='h'):
        self.status = status
        self.value = 0
        self.aces = 0
        self.cards = []  # want to pull cards from table deck in order to append in my list of cards
        self.betvalue = 0
        self.numcards=0
        self.handnum = handnum

    #    def set_bet_value(self):

    def add_card(self, tempcard):
        self.cards.append(tempcard)
        self.value += Blackjack.values[tempcard.rank]
        self.numcards +=1
        if tempcard.rank == 'Ace':
            self.aces+=1
        if self.aces>=1 and self.numcards>1 and self.value > 21:
            #self.aces += 1
            self.adjust_for_ace()

    def adjust_for_ace(self):
        while (self.value > 21 and self.aces > 0):
                self.value -= 10
                self.aces -= 1

    def print_cards(self):
        for mycard in self.cards:
            print(mycard)

    def get_card(self,num):
        self.cards.pop(num)


class Player():
    def __init__(self, name='Dealer', tchips=100):
        self.cnthands = 1
        self.hands = [Hand(self.cnthands)]
        # self.name = input("What is your name?\nName: ")
        self.name = name
        self.mychips = Chips(tchips)
        self.hidecard = 1

    def add_hand(self,hand,card):
        hand.add_card(card)
        self.cnthands+=1
        hand.handnum = self.cnthands
        self.hands.append(hand)


    def print_hands(self):
        print(self.name + " cards:")
        if (len(self.hands) > 1):
            for i in range(0, len(self.hands)):
                print("hand {}:".format(i + 1))
                print(self.hands[i])
        else:
            print(self.hands[0].__str__())  # prints also None object

