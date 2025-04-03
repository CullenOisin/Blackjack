import random
import time

cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "J": 10, "Q": 10, "K": 10, "A": 11}



def calculate_hand(hand):
    total = sum(cards[card] for card in hand)
    # if Ace is 1 or 11
    if "A" in hand and total > 21:
        total -= 10
    return total


def deal_card():
    return random.choice(list(cards.keys()))


def play():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    print("Hands are Dealt\n")

    #show hands
    print(f"Your hand: {player_hand} | Total: {calculate_hand(player_hand)}")
    print(f"Dealer's hand: {dealer_hand[0]}, '?'")

    #player input
    while calculate_hand(player_hand) < 21:
        choice = input("Do you want to Hit or Stand? (H or S)").lower()
        if choice == 'h':
            player_hand.append(deal_card())
            print(f"Your hand: {player_hand} | Total: {calculate_hand(player_hand)}")
        elif choice == 's':
            break
        else:
            print("Please enter H to Hit or S to Stand")


    if calculate_hand(player_hand) > 21:
        print(f"\nYour hand: {player_hand} | Total: {calculate_hand(player_hand)}")
        print("You Bust, You Lose :(")
        return


    print(f"\nDealer's hand: {dealer_hand} | Total: {calculate_hand(dealer_hand)}")
    while calculate_hand(dealer_hand) < 17:
        print("Dealer takes!")
        time.sleep(1)
        dealer_hand.append(deal_card())
        time.sleep(1)
        print(f"Dealer's hand: {dealer_hand} | total: {calculate_hand(dealer_hand)}")

    #winner
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)

    if dealer_total > 21:
        time.sleep(1)
        print(f"\nDealer Busts, You win! :)")
    elif player_total > dealer_total:
        time.sleep(1)
        print(f"\nYou win! Your total of: {player_total} beat the Dealer's : {dealer_total}")
    elif player_total < dealer_total:
        time.sleep(1)
        print(f"\nYou lose! Dealer's total of {dealer_total} beat your total of: {player_total}")
    else:
        time.sleep(1)
        print(f"\nIt's a Draw, Money back! Your total: {player_total} | Dealer's total: {dealer_total}")

# Run the game
choice2 = 'h'
while choice2 != 'q':
    choice2 = input("Do you want to Play or Quit? (P or Q): ").lower()

    if choice2 == 'p':
        print("Bets Closed!")
        time.sleep(1)
        play()
    elif choice2 == 'q':
        print("Thanks for playing")
    else:
        print("Enter P to play or Q to quit.")
