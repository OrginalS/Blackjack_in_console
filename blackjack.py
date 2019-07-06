from random import *
import time


class Player:

    def __init__(self, money):

        self.money = money


class Deck:

    def __init__(self, cards):

        self.cards = cards


def hit(turn):
    if turn == 1:
        try:
            hit = int(input("1-Hit 2-Stay: "))
        except ValueError:
            return wrong_input("hit")
        if hit == 1:
            return now.pop()
        elif hit == 2:
            return "X"
        else:
            return wrong_input("hit")
    elif turn == 2:
        return now.pop()


def score(cards):
    score = 0
    ace = 0
    for i in range(len(cards)):
        if cards[i] == "J" or cards[i] == "Q" or cards[i] == "K":
            score += 10
        elif cards[i] == "A":
            ace += 1
        else:
            score += cards[i]
    if score + ace > 21:
        return score + ace
    else:
        if score + 11*ace <= 21:
            return score + 11*ace
        elif score + 11 * (ace-1)+1 <= 21:
            return score + 11 * (ace-1)+1
        elif score + 11 * (ace-2)+2 <= 21:
            return score + 11 * (ace-2)+2
        elif score + 11 * (ace-3) + 3 <= 21:
            return score + 11 * (ace-3) + 3
        else:
            return score + ace


def wrong_input(err):
    print("\nWrong input\n")
    if err == "bet":
        return bet(player1)
    if err == "hit":
        return hit(1)


def bet(player):
    print("\nYour credits: " + str(player.money) + "\n")
    try:
        return int(input("How much do you want to bet: "))
    except ValueError:
        return wrong_input("bet")


def status(player_cards, dealer_cards, player_score, dealer_score):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Dealers cards : " + " ".join(map(str, dealer_cards)) + " = " + str(dealer_score))
    print("Your cards : " + " ".join(map(str, player_cards)) + " = " + str(player_score))
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


def play():
    shuffle(now)
    while True:
        while True:
            bet_amount = bet(player1)
            if bet_amount >= 0:
                break
            else:
                wrong_input("bet")
        if bet_amount > player1.money:
            print("Insufficient funds, bet different amount")
            bet(player1)
        else:
            break

    player_cards = [now.pop(), now.pop()]
    dealer_cards = [now.pop(), now.pop()]
    while player_cards[-1] != "X" and score(player_cards) <= 21:
        player_score = score(player_cards)
        status(player_cards, [dealer_cards[0], "X"], player_score, "?")
        player_cards.append(hit(1))

    if player_cards[-1] == "X":
        player_cards.pop()
        dealer_score = score(dealer_cards)
        status(player_cards, dealer_cards, player_score, dealer_score)
        while player_score > dealer_score and dealer_score <= 21:
            print("Dealer draws a card")
            time.sleep(2)
            dealer_cards.append((hit(2)))
            dealer_score = score(dealer_cards)
            status(player_cards, dealer_cards, player_score, dealer_score)
        if dealer_score > 21:
            print("Dealer is over 21.")
            print("Player wins")
            player1.money += bet_amount
        else:
            print("Dealer wins")
            player1.money -= bet_amount
    else:
        player_score = score(player_cards)
        dealer_score = score(dealer_cards)
        status(player_cards, dealer_cards, player_score, dealer_score)
        print("You'r over 21.")
        print("Dealer wins.")
        player1.money -= bet_amount


player1 = Player(500)
cont = 1
while cont == 1:
    deck = Deck([2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"])
    now = deck.cards
    play()
    while True:
        try:
            cont = int(input("\n1-Play 2-Exit : "))
        except ValueError:
            cont = 0
        if cont == 1 or cont == 2:
            break
        else:
            print("\nWrong input")
