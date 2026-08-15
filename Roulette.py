#Roulette 

import random
import time

red_num = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 30, 32, 34, 36}
black_num = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 29, 31, 33, 35}

def roulette() :
    num = random.randint(0, 36)
    if num == 0 :
        color = "green"
    elif num in red_num :
        color = "red"
    else :
        color = "black"

    return num, color

def get_emoji(color):
    emoji_map = {"red": "🔴", "black": "⚫", "green": "🟢"}
    return emoji_map.get(color, "")

def main() :
    balance = 1000
    print("***************************************")
    print("\n~~~~~~~~Welcome to the Roulette~~~~~~~~\n")
    print(f"You get a joining bonus of {balance}")
    print("\n***************************************\n")
    while True :
        if balance <= 0 :
            print("You are out of funds! Game over")
            break
        print(f"Current balance : ${balance} ")
        try :
            bet = float(input("Enter your bet : $ "))
        except ValueError :
            print("Invalid bet\n")
            continue

        if bet > balance :
            print("Insufficient funds\n")
            continue
        elif bet <= 0 :
            print("Unreal bet 🤡\n")
            continue

        print("\nChoose a colour to bet on :\n")
        print("[R] Red🔴 (1:1 payout)\n")
        print("[B] Black⚫ (1:1 payout)\n")
        print("[G] Green🟢 (14:1 payout)\n")

        choice = input("Choose [R] Red , [B] Black, [G] Green : ").strip().lower()
        color_code = {'r': 'red', 'b': 'black', 'g': 'green'}
        if choice not in color_code :
            print("Invalid choice\n")
            continue
        choice_color = color_code[choice]
        balance -= bet
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        print("*******The Wheel spins...******")
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        time.sleep(1.5)

        num, land_color = roulette()
        print(f"The wheel landed on {num} ({land_color.upper()})!")
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()

        if choice_color == land_color:
            if choice_color == "green":
                multiplier = 14
            else:
                multiplier = 1  # Red or Black 1:1 profit

            payout = bet + (bet * multiplier)
            balance += payout
            print(f"🎉 YOU WIN! You earned ${bet * multiplier:.2f} profit!")
        else:
            print(f"❌ YOU LOSE! You lost your bet of ${bet:.2f}.")

        print(f"New Balance: ${balance:.2f}\n")

        play_again = input("Do you want to spin again? (y/n): ").strip().lower()
        if play_again != 'y':
            break

    print(f"\nThanks for playing! You left with ${balance:.2f}.")

if __name__ == "__main__" :
    main()