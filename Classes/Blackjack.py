from Classes.Character import *
from Classes.Deck import *


class Table:
    def __init__(self, nump):
        self.num_of_players=nump
        self.mydeck = TableDeck()
        self.players = []
        self.mydeck.shuffle()
        self.dealer = Player()

    def addplayer(self):
        self.num_of_players+=1
    def set_table(self):
        print("There are {} player/s, in the following enter name/s\nand each will get 100$ chips\n".format(self.num_of_players))
        print("*************************************\nTable is being set for the followng {} player/s: ".format(self.num_of_players))

        for i in range(1,self.num_of_players+1,1):
            self.players.append(Player(input("What is your name?\nName: ")))
