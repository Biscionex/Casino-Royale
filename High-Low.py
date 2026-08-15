# High-Low

import random
import time

def main():
    low = 1
    high = 100
    balance = 1000.0

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n******WELCOME TO HIGH-LOW******\n")
    print(f"You get a joining bonus of ${balance:.2f}")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    while True:
        if balance <= 0:
            print("You are out of money! Game over.")
            break

        bet = float(input(f"Enter your bet (Current balance: ${balance:.2f}): $ "))
        
        if bet > balance:
            print("Insufficient funds!\n")
            continue
        elif bet <= 0:
            print("Invalid Bet!\n")
            continue

        # Deduct bet upfront
        balance -= bet
        
        # Pick new random numbers for each round
        ques = random.randint(low, high)
        ans = random.randint(low, high)

        print(f"Remaining balance: ${balance:.2f}\n")
        print("*****************************\n")
        print("The computer is choosing a number between 1 - 100...\n")
        time.sleep(1)
        print(f"The shown number is: {ques}")
        print("Is the target number higher or lower?")
        guess = input("Type (H) for Higher, (L) for Lower, (J) for Exact Match (JACKPOT): ").strip().lower()
        print()

        # Win conditions
        if (guess == "h" and ans > ques) or (guess == "l" and ans < ques):
            payout = bet * 2  # Returns original bet + 1x profit
            balance += payout
            print("~~~YOU WIN!!!~~~")
            print(f"The number was {ans}")
            print(f"You won ${bet:.2f}!")
            print(f"Your new balance is ${balance:.2f}")

        elif guess == "j" and ans == ques:
            payout = bet * 10  # Standard jackpot multiplier (10x payout)
            balance += payout
            print("~~~JACKPOT WINNER!!!~~~")
            print(f"The number was indeed {ans}!")
            print(f"You won ${bet * 9:.2f} profit!")
            print(f"Your new balance is ${balance:.2f}")

        # Tie / Equal number standard guess condition
        elif ans == ques and guess in ["h", "l"]:
            balance += bet  # Push/Tie: Return bet
            print("~~~PUSH / TIE~~~")
            print(f"The number was {ans} (equal to initial number).")
            print(f"Your bet of ${bet:.2f} has been refunded.")
            print(f"Your balance remains ${balance:.2f}")

        # Loss condition
        else:
            print("~~~YOU LOSE !!!~~~")
            print(f"The number was {ans}")
            print(f"You lost your bet of ${bet:.2f}.")
            print(f"Your new balance is ${balance:.2f}")

        print("\n*******************************")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        play = input("Do you want to play again (y / n): ").strip().lower()
        if play != "y":
            break

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Thank you for playing! Final Balance: ${balance:.2f}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if __name__ == "__main__":
    main()