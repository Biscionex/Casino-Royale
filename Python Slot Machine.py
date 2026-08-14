#Python Slot Machine

import random

def spin_row() :
    symbols = ['🍒', '🍉', '🍊', '7️⃣', '💎', '🍀', '👑', '⭐', '🔔', '🪙']

    return [random.choice(symbols) for symbol in range(3)]

def print_row(row) :
    print(" || ".join(row))

def payout(row, bet) :
    if row[0] == row[1] == row[2] :
        if row[0] == '🍒' :
            return bet * 1
        elif row[0] == '🍉' :
            return bet * 1.10
        elif row[0] == '🍊' :
            return bet * 1.25
        elif row[0] == '💎' :
            return bet * 2
        elif row[0] == '🍀' :
            return bet * 4
        elif row[0] == '👑' :
            return bet * 7
        elif row[0] == '⭐' :
            return bet * 3
        elif row[0] == '🔔' :
            return bet * 3.50
        elif row[0] == '🪙' :
            return bet * 4.5
        elif row[0] == '7️⃣' :
            return bet * 10
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2] :
        if row[0] == '🍒' :
            return bet * 0.05
        elif row[0] == '🍉' :
            return bet * 0.10
        elif row[0] == '🍊' :
            return bet * 0.15
        elif row[0] == '💎' :
            return bet * 0.50
        elif row[0] == '🍀' :
            return bet * 0.60
        elif row[0] == '👑' :
            return bet * 2
        elif row[0] == '⭐' :
            return bet * 0.75
        elif row[0] == '🔔' :
            return bet * 1.5
        elif row[0] == '🪙' :
            return bet * 2.5
        elif row[0] == '7️⃣' :
            return bet * 4 
        if row[1] == '🍒' :
            return bet * 0.05
        elif row[1] == '🍉' :
            return bet * 0.10
        elif row[1] == '🍊' :
            return bet * 0.15
        elif row[1] == '💎' :
            return bet * 0.50
        elif row[1] == '🍀' :
            return bet * 0.60
        elif row[1] == '👑' :
            return bet * 2
        elif row[1] == '⭐' :
            return bet * 0.75
        elif row[1] == '🔔' :
            return bet * 1.5
        elif row[1] == '🪙' :
            return bet * 2.5
        elif row[1] == '7️⃣' :
            return bet * 4   
    else :
        return 0

def main() :
    balance = 1000
    print()
    print("*****************************************")
    print()
    print("777~~~ WELCOME TO THE SLOT MACHINE ~~~777")
    print()
    print("Symbols : 🍒 🍉 🍊 7️⃣ 💎 🍀 👑 ⭐ 🔔 🪙")
    print()
    print("*****************************************")

    while balance > 0 :
        print(f"Current balance : ${balance}")
        print()
        bet = float(input("Place your bet amount : "))
        print()
        if bet > balance :
            print("Insufficient funds")
            print()
        elif bet <= 0 :
            print("Please place a real bet")
            print()
        else :
            balance -= bet
            print(f"Remaining balance : ${balance}")
            print()

        row = spin_row()
        print(" SPINNING... \n")
        print("---------------")
        print_row(row)
        print("---------------")

        pay = payout(row, bet)

        if pay > 0 :
            print()
            print("~~~ YOU WON ~~~")
            print()
            print(f"Your payout is : ${pay}")
        else :
            ("BETTER LUCK NEXT TIME")
            
        balance += pay

        play = input("Do you want to spin again (y / n) : ").lower()
        if play != "y" :
            break

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("GAME OVER")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print(f"Your final balance is ${balance}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("🥳🥳🥳")


if __name__ == "__main__" :
    main()

