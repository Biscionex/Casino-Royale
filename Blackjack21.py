#Blackjack

import random

suite = ['❤️', '♣️', '♦️', '♠️']
card = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values ={
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}
def create_deck():
    deck = [{'rank': rank, 'suit': suit} for suit in suite for rank in card]
    random.shuffle(deck)
    return deck

def hand_value(hand) :
    value = sum(values[card['rank']] for card in hand)
    aces = sum(1 for card in hand if card['rank'] == 'A')
    
    # Convert Ace from 11 to 1 if score goes over 21
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
        
    return value    

def display_hand(name, hand, hide_first_card=False):
    if hide_first_card:
        print(f"{name}'s Hand: [Hidden Card], {hand[1]['rank']} of {hand[1]['suit']}")
    else:
        cards_str = ", ".join([f"{card['rank']} of {card['suit']}" for card in hand])
        print(f"{name}'s Hand: {cards_str} (Total: {hand_value(hand)})")

def bet(balance) :
    while True :
        try:
            bet = float(input("Enter bet amount : $ "))
            if bet > balance:
                print("Insufficient funds! Please enter a valid amount.")
                print()
            elif bet <= 50:
                print("Invalid bet amount. Must be greater than 50.")
                print()
            else:
                return bet
        except ValueError:
            print("Please enter a valid number.")
            print()

def play_hand(hand, deck, bet, balance, hand_title="Player"):

    can_double = balance >= bet
    first_move = True

    while True:
        options = "(H) Hit or (S) Stand"
        if first_move and can_double:
            options += " or (D) Double Down"

        print()

        choice = input(f"{hand_title} - Do you want to {options}? ").strip().lower()
        print()

        if choice == 'h':
            hand.append(deck.pop())
            display_hand(hand_title, hand)
            if hand_value(hand) > 21:
                print(f"{hand_title} Busted!")
                return hand, bet, False  # Hand lost via bust
            first_move = False

        elif choice == 's':
            print(f"{hand_title} stands.")
            print()
            return hand, bet, True  # Hand actively played and standing

        elif choice == 'd' and first_move and can_double:
            bet *= 2
            print(f"Doubled down! Bet increased to ${bet:.2f}")
            print()
            hand.append(deck.pop())
            display_hand(hand_title, hand)
            if hand_value(hand) > 21:
                print(f"{hand_title} Busted on Double Down!")
                return hand, bet, False
            return hand, bet, True

        else:
            print("Invalid selection! Please enter a valid option.")



def main() :
    balance = 1000
    print()
    print("❤️ ♦️ ❤️ ♦️ ❤️ ♦️ ❤️ ♦️ ❤️ ♦️ ❤️ ♦️ ❤️ ♦️ ❤️ ♦️ ❤️ ♦️")
    print()
    print("~~~~~~~21~~~BLACKJACK~~~21~~~~~~~~~")
    print()
    print("♠️ ♣️ ♠️ ♣️ ♠️ ♣️ ♠️ ♣️ ♠️ ♣️ ♠️ ♣️ ♠️ ♣️ ♠️ ♣️ ♠️ ♣️")
    print()
    while balance > 0:
        print(f"Current Balance: ${balance:.2f}")
        print()
        initial_bet = bet(balance)
        
        deck = create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        print()

        print("❤️ ♠️ ♦️ ♣️ --- Dealing Cards --- ♣️ ♦️ ♠️ ❤️")
        display_hand("Dealer", dealer_hand, hide_first_card=True)
        print()
        display_hand("Player", player_hand)
        print()

        # Check for immediate Blackjack
        if hand_value(player_hand) == 21:
            print("Blackjack! You win!")
            print()
            print("❤️ ♠️ ♦️ ♣️")
            print()
            balance += initial_bet * 1.5
            continue

        # Check for Split Availability
        can_split = (
            player_hand[0]['rank'] == player_hand[1]['rank'] 
            and balance >= (initial_bet * 2)
        )

        player_hands_to_play = []

        if can_split:
            split_choice = input("You have a pair! Would you like to (Sp)lit? (y/n): ").strip().lower()
            if split_choice == 'y':
                # Separate hand into two independent hands
                hand1 = [player_hand[0], deck.pop()]
                hand2 = [player_hand[1], deck.pop()]
                player_hands_to_play = [
                    {"hand": hand1, "title": "Hand 1"},
                    {"hand": hand2, "title": "Hand 2"}
                ]

        # Standard non-split setup
        if not player_hands_to_play:
            player_hands_to_play = [{"hand": player_hand, "title": "Player"}]

        completed_hands = []

        # Play each player hand
        for hand_info in player_hands_to_play:
            print(f"\n--- Playing {hand_info['title']} ---")
            display_hand(hand_info['title'], hand_info['hand'])
            
            # Pass balance minus initial bet so we don't allow doubling on money already committed
            current_hand, final_bet, survived = play_hand(
                hand_info['hand'], deck, initial_bet, balance - initial_bet, hand_info['title']
            )
            completed_hands.append({
                "hand": current_hand,
                "bet": final_bet,
                "survived": survived,
                "title": hand_info['title']
            })

        # Dealer Turn (Runs if at least one player hand didn't bust)
        any_survived = any(h['survived'] for h in completed_hands)

        if any_survived:
            print("\n--- Dealer's Turn ---")
            print()
            display_hand("Dealer", dealer_hand)
            
            while hand_value(dealer_hand) < 17:
                print("Dealer hits...")
                dealer_hand.append(deck.pop())
                display_hand("Dealer", dealer_hand)

            dealer_score = hand_value(dealer_hand)
            print(f"\nDealer final score: {dealer_score if dealer_score <= 21 else 'Bust'}")
            print()

            # Resolve payouts for each hand played
            for h in completed_hands:
                p_score = hand_value(h['hand'])
                b_amount = h['bet']

                if not h['survived']:
                    print(f"\n{h['title']} lost (${b_amount:.2f}) due to bust.")
                    balance -= b_amount
                elif dealer_score > 21 or p_score > dealer_score:
                    print(f"\n{h['title']} WINS ${b_amount:.2f}! ({p_score} vs {dealer_score if dealer_score <= 21 else 'Bust'})")
                    balance += b_amount
                elif p_score < dealer_score:
                    print(f"\n{h['title']} lost (${b_amount:.2f}). ({p_score} vs {dealer_score})")
                    balance -= b_amount
                else:
                    print(f"\n{h['title']} PUSH (Tie)! ({p_score} vs {dealer_score})")

        else:
            # All hands busted; deduct bets
            for h in completed_hands:
                balance -= h['bet']

        print("\n--------------❤️ ♠️ ♦️ ♣️---------------\n")

        play = input("Do you want to spin again (y / n) : ").lower()
        if play != "y" :
            break


    print("Thanks for playing !! ")
    print(f"Final balance : ${balance}")
    print("♣️ ♦️ ♠️ ❤️")


if __name__ == "__main__" :
    main()
