from Classes.Character import *
from Classes.Deck import *
import shutil


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
        self.banner()
        print("There are {} player/s, in the following enter name/s\nand each will get 100$ chips\n".format(self.num_of_players))
        print("*************************************\nTable is being set for the followng {} player/s: ".format(self.num_of_players))

        for i in range(1,self.num_of_players+1,1):
            self.players.append(Player(input("What is your name?\nName: ")))

    def banner(self,txt = "Welcome to BlackJack",ch='$', length=78):
        spaced_text = " {} ".format(txt)
        mybanner = spaced_text.center(length,ch)
        dec_line = "$"*length

        win_size = shutil.get_terminal_size()

        print(dec_line.center(win_size.columns)+mybanner.center(win_size.columns)+dec_line.center(win_size.columns)+"\n\n")

