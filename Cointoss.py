# Cointoss

import random
import time

def coin() :
    outcomes = {0: "heads", 1: "tails"}
    result_code = random.randint(0, 1)
    return outcomes[result_code]

def main() :
    balance = 0
    print()
    print("*****************************************")
    print()
    print("~~~ WELCOME TO COINTOSS ~~~")
    print()
    print("*****************************************")
    start = input("Do you wish to start the game [Y/N]: ").strip().lower()
    if start != "y":
        print("\nMaybe next time! Goodbye.\n")
        return
    playing = True 
    while playing :
        guess = (
            input("\nCall it — Heads or Tails? [H/T]: ").strip().lower()
        )
        if guess in ["h", "heads"]:
            player_choice = "heads"
        elif guess in ["t", "tails"]:
            player_choice = "tails"
        else:
            print("Invalid choice! Please choose 'H' for Heads or 'T' for Tails.")
            continue

        print("\nFlipping the coin into the air...")
        time.sleep(1)
        print("Catching the coin...\n")
        time.sleep(1)

        result = coin()


        print(f"The coin landed on: {result.upper()}")

        if player_choice == result:
            balance += 100
            print(f"Correct! You won $100! Current balance: ${balance}\n")
        else:
            print(f"Wrong guess! You lost this round.")
            print(f"Final balance: ${balance}\n")
        while True:
            play_again = (
                input("Do you want to play again [Y/N]: ").strip().lower()
            )
            if play_again == "y":
                break  
            elif play_again == "n":
                print(
                    f"\nYou walked away safely with ${balance}. Thanks for playing!\n"
                )
                playing = False 
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.\n")

if __name__ == "__main__" :
    main()