#Russian Roulette 

import random
import time

def round() :
    magazine = random.randint(0,5)
    trigger = random.randint(0,5)
    if magazine == trigger :
        code = "death"
    else :
        code = "alive"
    return magazine, trigger, code

def get_emoji(code) :
    emoji_map = {"death": "☠️", "alive": "❤️"}
    return emoji_map.get(code, "")

def main() :
    balance = 0
    print("\nWELCOME TO THE RUSSIAN ROULETTE\n")
    print("Bet your life : win or lose !\n")

    bet = input("Do you wish to bet your life [Y/N]: ").strip().lower()
    if bet != "y" :
        print("\nMaybe next time, Goodbye\n")
        return
    playing = True
    while playing :
        print("\nSpinning the cylinder...\n")
        time.sleep(1)
        print("Pulling the trigger...\n")
        time.sleep(1.5)

        trigger, magazine, code = round()
        emoji = get_emoji(code)

        if code == "death":
            print(
                f"BANG!\n Trigger pulled on Chamber #{trigger}, which had the bullet! {emoji}"
            )
            print(f"GAME OVER! You died with a final balance of ${balance}. But lost your 'LIFE'\n")
            playing = False
        else:
            balance += 1000000
            print(
                f"CLICK! Trigger pulled on Chamber #{trigger} (Bullet was in #{magazine}) {emoji}"
            )
            print(f"You survived! Current balance: ${balance}\n")

            # Ask to play again if survived
            while True:
                play_again = (
                    input("Do you want to play again [Y/N]: ").strip().lower()
                )
                if play_again == "y":
                    break  # Continues the outer while loop
                elif play_again == "n":
                    print(
                        f"\nYou walked away safely with ${balance}. Thanks for playing!\n"
                    )
                    playing = False  # Exits the outer while loop
                    break
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.\n")
        

if __name__ == "__main__" :
    main()