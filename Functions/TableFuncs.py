from Classes.Blackjack import *
from Classes.Character import *
from Classes.Deck import *
from Classes import Deck

from Functions.PlayerFuncs import *

import time
#
# def create_new_deck(gametable):
#     gametable.mydeck.deck = Deck.TableDeck()
#     gametable.mydeck.shuffle()

def deal_all(gametable):
    # if (gametable.mydeck.deck == True):
    #     create_new_deck(gametable)
    for player in gametable.players:
        for hand in player.hands:
            first_crd = gametable.mydeck.deal()
            hand.add_card(first_crd)
    for player in gametable.players:
            for hand in player.hands:
                #fix if player doesnt want to split hands
                flag=0
                nextcard = gametable.mydeck.deal()
                if(nextcard.rank == hand.cards[0].rank):
                    print(hand.cards[0].rank + nextcard.rank)
                    while(flag==0):
                        try:
                            split = input("{} Would you like to split?\nCurrent cards are: \n{}\n{}\nAnswer: (y or n):".format(player.name, hand.cards[0].__str__(), nextcard.__str__()))
                            if(split.lower() == 'y'):
                                print("Splitting...")
                                splitbet = int(hand.betvalue / 2)
                                hand.betvalue = splitbet
                                player.add_hand(Hand(player.cnthands + 1), nextcard)
                                player.hands[player.cnthands-1].betvalue = splitbet
                                nextcard = gametable.mydeck.deal()
                                if(nextcard.rank != hand.cards[0].rank):
                                    hand.add_card(nextcard)
                                    flag=0
                                    break
                            else:
                                flag=1
                                hand.add_card(nextcard)
                        except ValueError:
                                print("Please pick y or n")
                        # except nextcard.rank == hand.cards[0].rank:
                        #     continue
                else:
                    hand.add_card(nextcard)

    # for player in gametable.players:
    #     for cur_hand in player.hands:
    #         if(cur_hand.numcards<2):
    #             print("MISSING CARD,ADDED")
    #             cur_hand.add_card(gametable.mydeck.deal())

    for hand in gametable.dealer.hands:
        for i in range(2):
            hand.add_card(gametable.mydeck.deal())


def ascii_version_of_card(gametable,player,cards):
    # create an empty list of list, each sublist is a line
    displaycards = []
    lines = [[] for i in range(7)]
    for card in cards:
        # add the individual card on a line by line basis
        if(card.rank=="Ten"):
            rank = Deck.values[card.rank]
            space = ''
        elif((Deck.values[card.rank] == 10 or Deck.values[card.rank] == 11) and card.rank != "Ten"):
            rank = card.rank[0]
            space = ' '
        else:
            rank = Deck.values[card.rank]
            space = ' '
        if(cards.index(card)==1 and player.name=="Dealer" and gametable.dealer.hidecard==1):
            lines[0].append('┌───────┐')
            lines[1].append('│*******│')
            lines[2].append('│*******│')
            lines[3].append('│*******│')
            lines[4].append('│*******│')
            lines[5].append('│*******│')
            lines[6].append('└───────┘')
            gametable.dealer.hidecard=0
        else:
            lines[0].append('┌───────┐')
            lines[1].append('│{}{}     │'.format(rank, space))
            lines[2].append('│       │')
            lines[3].append('│   {}   │'.format(Deck.suits_symbols[card.suit]))
            lines[4].append('│       │')
            lines[5].append('│     {}{}│'.format(space,rank))
            lines[6].append('└───────┘')

    for index, line in enumerate(lines):
        displaycards.append(''.join(lines[index]))

    # print('\n'.join(displaycards))
    for l in displaycards:
        print(l)
        delay(0.1)


def loose_bet(gametable,player,hand):
    print("{}: total chips -> {}, lost -> {}\n".format(player.name, player.mychips.total, hand.betvalue))
    if (player.mychips.total <25):
        print("Player {} has to go\n".format(player.name))
        gametable.players.remove(player)
    time.sleep(0.8)
    # for num,player in reversed(list(enumerate(gametable.players))):
    #     if(player == pl_check):
    #         for hand in player.hands:
    #             if(hand == hnd_check):

#def place_insurance(gametable,player,hand):


def delay(x):
    time.sleep(x)

def clear_players_hands(gametable):
    for player in gametable.players:
        if(player.mychips.total>0):
            player.hands[:] = []
            player.cnthands=1
            player.hands = [Hand(player.cnthands)]
        else:
            player.hands[:] = []
            del gametable.players[gametable.players.index(player)]
    gametable.dealer.hands[:] = []
    gametable.dealer.hands = [Hand(1)]

    # for player in gametable.players:
    #     for hand in player.hands:
    #         hand.print_cards()
    #         print("hello")
    gametable.firstprint = 1
    gametable.dealerprint = 1
    gametable.dealer.hidecard = 1

#prints all players hands
def print_all(gametable):
    print("----{}----".format(gametable.dealer.name))
    print("->Hand holds: ")
    for hand in gametable.dealer.hands:
        ascii_version_of_card(gametable, gametable.dealer, hand.cards)
    for player in gametable.players:
        print("----{}----".format(player.name))
        for hand in player.hands:
            if(player.cnthands>1):
                print("->Hand num {} holds:".format(hand.handnum))
            else:
                print("->Your hand holds:")
            ascii_version_of_card(gametable,player,hand.cards)
        print("\n\n")

# def last_print(gametable):
#     for player in gametable.players:
#         print("----{}----".format(player.name))
#         for hand in player.hands:
#             if (player.cnthands > 1):
#                 print("->Hand num {} holds:".format(hand.handnum))
#             else:
#                 print("->Your hand holds:")
#             ascii_version_of_card(gametable, player, hand.cards)
#         print("\n\n")
#     print("----{}----".format(gametable.dealer.name))
#     print("->Hand holds: ")
#     for hand in gametable.dealer.hands:
#         ascii_version_of_card(gametable, gametable.dealer, hand.cards)


#checks for any win in the table
#
#need ot fix check win func in order to split the win between winners or one winner

def ret_dealer_hand(gametable):
    for player in gametable.players:
        if player == 'Dealer':
            return player.hands.pop(0)

def check_win(gametable):
    rev_pl_list = gametable.players[::-1]

    for player in rev_pl_list[::-1]:
        for hand in player.hands:
            print("Checking {} hand num {} ...".format(player.name,hand.handnum))
            if((hand.value > gametable.dealer.hands[0].value or (hand.value<=21 and gametable.dealer.hands[0].value>21)) and hand.status!='b' and hand.natural==0):
                win_bet(gametable,player,hand,2)
            elif((hand.value==gametable.dealer.hands[0].value and hand.status!='b') or (hand.natural==1 and gametable.dealer.hands[0].natural==1)):
                player.mychips.total +=hand.betvalue
                hand.betvalue=0
                print("Player {}: Hand {} ended by draw\n".format(player.name,hand.handnum))
            elif(hand.natural==1 and gametable.dealer.hands[0].natural==0):
                win_bet(gametable,player,hand,2.5)
                print("Oh, that one was a fine BlackJack\n")
            else:
                loose_bet(gametable,player,hand)



def win_bet(gametable,player,hand,win_rate):
    player.mychips.total += hand.betvalue*win_rate
    print("{} overcome the dealer, won {} chips, total updated: {}\n".format(player.name,hand.betvalue*win_rate,player.mychips.total))
