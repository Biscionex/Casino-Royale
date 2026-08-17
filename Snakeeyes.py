#Snakeeyes

import random

dice_art = { 
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")                        
}

def print_dice(die1, die2):
    """Displays two dice side-by-side."""
    for line1, line2 in zip(dice_art[die1], dice_art[die2]):
        print(f"{line1}   {line2}")

def main() :
    balance = 10000
    
    print("=" * 35)
    print("\n   WELCOME TO THE SNAKE EYES GAME   \n")
    print("=" * 35)
    print("Rules:")
    print(" - Double 1s (Two Snake Eyes): Win 10x your bet!\n")
    print(" - One 1 (One Snake Eye): Win 5x your bet!\n")
    print(" - Any other Double: Win 2x your bet!\n")
    print(" - Any other roll: Lose your bet.\n")
    print("-" * 35)

    while balance > 0:
        print(f"\nCurrent Balance: ${balance}")
        bet_input = input("Enter your bet amount (or 'q' to quit): ").strip()

        if bet_input.lower() == 'q':
            print("Thanks for playing!")
            break

        if not bet_input.isdigit():
            print("Invalid input! Please enter a numeric amount.")
            continue

        bet = int(bet_input)

        if bet <= 0:
            print("Bet amount must be greater than zero.")
            continue
        if bet > balance:
            print("You don't have enough balance for that bet.")
            continue

        # Roll 2 dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        print("\nRolling the dice...")
        print_dice(die1, die2)

        # Evaluate outcome
        if die1 == 1 and die2 == 1:
            winnings = bet * 10
            balance += winnings
            print(f"🐍👀 DOUBLE SNAKE EYES! You won ${winnings}! (10x Payout)")
        elif die1 == 1 or die2 == 1:
            winnings = bet * 5
            balance += winnings
            print(f"👁️ ONE SNAKE EYE! You won ${winnings}! (5x Payout)")
        elif die1 == die2:
            winnings = bet * 2
            balance += winnings
            print(f"🎉 DOUBLES! You won ${winnings}! (2x Payout)")
        else:
            balance -= bet
            print(f"❌ No match! You lost ${bet}.")

    if balance == 0:
        print("\n💸 You ran out of money! Game over.")

    print(f"Final Balance: ${balance}")


if __name__ == "__main__" :
    main()