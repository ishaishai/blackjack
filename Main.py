from Classes.Blackjack import *
from Classes import Deck
from Functions.PlayerFuncs import *
from Functions.TableFuncs import *
import os
import time

def main():
    os.system('cls')
    pnum = int(input("how many players this time? ;)\nAmount: "))
    gametable = Table(pnum)
    gametable.set_table()
    while(True):
        take_bet(gametable)
        deal_all(gametable)
        print_all(gametable)
        player_decision(gametable)
        check_win(gametable)
        clear_players_hands(gametable)
        if(len(gametable.players)==0):
            print("Dealer takes it all...go practice")
            break
        gametable.banner("Next Round of BlackJack")
    # for player in gametable.players:
    #     for hand in player.hands:
    #
    #         card1 = gametable.mydeck.deal()
    #         hand.add_card(card1)
    #
    #         # hand.add_card(card2)
    #         cardpeek = gametable.mydeck.peek()
    #         print(cardpeek.rank)
    #         print(card1.rank)
    #         if(card1.rank == cardpeek.rank):
    #             if(input("{} would you like to split your hand?\nAnswer: (y or n)".format(player.name)) == 'y'):
    #                 player.add_hand(Hand(player.cnthands+1), gametable.mydeck.deal())
    #                 hand.add_card(gametable.mydeck.deal())
    #         else:
    #             hand.add_card(gametable.mydeck.deal())
    #

                   # #card is the same,pull another one, after not the same do a while that pull another and another one
                   #  player.split_hand(gametable.mydeck)

main()
