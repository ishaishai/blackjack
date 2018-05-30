from Functions.TableFuncs import *
from Classes.Blackjack import *
from Classes.Character import *
from Classes.Deck import *
from Classes import Deck
import time


def take_bet(gametable):
    for player in gametable.players:
        bet=0
        if(player.name!="Dealer"):
            for hand in player.hands:
                set_hand_bet(gametable,player,hand)

#def set_insurance(player,hand):

#first deal for the openning
def set_hand_bet(gametable,player,hand):
    while(True):
        bet=0
        try:
            bet = int(input(("{}, please place bet(you hold {} chips): ").format(player.name,player.mychips.total)))
            if (bet >=1 and bet <= player.mychips.total and bet%25==0):
                hand.betvalue = bet
                player.mychips.total -=bet
                print("Bet value set to: {} you've got left {} Chips".format(hand.betvalue, player.mychips.total))
                break
            else:
                print("You've got only {} chips".format(player.mychips.total))
        except ValueError:
            print("Please pick a number")


def fold_down(player,hand):
    print("{} decided to surrender and lost {} chips\n".format(player.name,hand.betvalue))
    del player.hands[player.hands.index(hand)]

def double_down(gametable,player,hand):
    player.mychips.total -= hand.betvalue
    hand.betvalue *= 2
    print("{} has doubled the bet and draw last card...".format(player.name))
    hit(gametable,player,hand)
    ascii_version_of_card(gametable,player,hand.cards)


def player_decision(gametable):
    for i,player in enumerate(gametable.players,1):
        for hand in player.hands:
            if(hand.value>0 and hand.value<21 and hand.status!='b'):
                print("{} it's your turn:\nhand {}:\n".format(player.name, hand.handnum))
                ascii_version_of_card(gametable,player,hand.cards)
                print("Hand value: {}, Bet value: {}$".format(hand.value,hand.betvalue))
                if (hand.value < 21):
                    while(True):
                        decision = input("Hit or Stand or Fold(Surrender) or Double-down (h or s or f or d): ")
                        if(decision.lower()=='s'):
                            stand(hand)
                            break
                        elif(decision.lower()=='f'):
                            fold_down(player,hand)
                            break
                        elif(hand.betvalue<=player.mychips.total and decision.lower()=='d'):
                            double_down(gametable,player,hand)
                            break
                        elif(decision.lower()=='h'):
                            while(decision.lower()=='h'):
                                hit(gametable,player,hand)
                                ascii_version_of_card(gametable,player,hand.cards)
                                print("Hand value: {}, Bet value: {}$".format(hand.value,hand.betvalue))
                                decision='none'
                                if(hand.status!='b' and hand.value<21):
                                    decision = input("hit or stand? ")
                                else:
                                    break
                        else:
                            print("Only h or s or f or d")


    for hand in gametable.dealer.hands:
        if(hand.value<=17):
            dealer_refill=0
            while (hand.value < 17):
                dealer_refill=1
                print("\nDealer takes another card...")
                hand.add_card(gametable.mydeck.deal())
                print("{} holds:".format(gametable.dealer.name))
                ascii_version_of_card(gametable,gametable.dealer,hand.cards)
                # if(player.name!='Dealer'):
                #     print("Hand value: {}, Bet value: {}$".format(hand.value, hand.betvalue))
                # else:
                print("Hand value: {}\n\n".format(hand.value))
                delay(3)
            if(dealer_refill==0):
                ascii_version_of_card(gametable,gametable.dealer,hand.cards)
        else:
            print("\n{} holds:".format(gametable.dealer.name))
            ascii_version_of_card(gametable, gametable.dealer, hand.cards)

    print("------------No More Deal-------------\n\n")

def hit(gametable,player,hand):
    hand.add_card(gametable.mydeck.deal())
    if(hand.value>21):
        if(hand.aces==0):
             hand.status = 'b'
             #player.mychips.total -=hand.betvalue
             print("{} is busted for the following hand:".format(player.name))
        else:
            hand.adjust_for_ace()

def stand(hand):
    hand.status = 's'

def kick_player(player):
    del player