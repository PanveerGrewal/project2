# Import necessary modules
import random
import time

# Define global variables
slot_machine_running = True
wallet = 0

# Define the main function
def again():
    global wallet
    global slot_machine_running

    # Check if the player has money to bet
    if wallet > 0:
        # Get the bet amount from the player
        bet = int(input("How much money would you like to bet? "))

        # Check if the bet amount is within the available wallet balance
        if bet <= wallet:
            # Spin the slot machine
            print("Spinning...")
            time.sleep(3)
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            c = random.randint(1, 6)
            print(a, b, c)
            time.sleep(2)

            # Check the results of the spin and update the wallet accordingly
            if a == b == c:
                wallet = (wallet - bet) + bet * 3
                print("You win!")
                print("You win", bet * 3, "dollars!")
                print("Your wallet is now", wallet, "dollars!")
            elif a == b - 1 and b == c - 1 or c == b - 1 and b == a - 1:
                wallet = (wallet - bet) + bet * 2
                print("You win!")
                print("You win", bet * 2, "dollars!")
                print("Your wallet is now", wallet, "dollars!")
            else:
                wallet = wallet - bet
                print("You lose!")
                print("You lose", bet, "dollars!")
                print("Your wallet is now", wallet, "dollars!")
                time.sleep(2)

            # Ask the player if they want to play again
            que = str(input("Would you like to play again?  yes or no  "))
            if que == "yes":
                again()
            else:
                print("Thanks for playing!")
                slot_machine_running = False
        else:
            print("You don't have enough money to bet!")
            time.sleep(2)
            again()
    else:
        print("You have no money!")

# Welcome message and initialization of wallet
print("Welcome to the slot machine!")
wallet = int(input("How much money do you want to add to your wallet? "))

# Run the slot machine game while it's still running
while slot_machine_running:
    again()
