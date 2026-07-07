import random
import time

print("Welcome to Roshambeaux")
print("You are playing against the computer")
print("Have a 65% win rate or greater to pass")
print("Good Luck!")
print()

def result(user_choice, computer_choice):
    global wins
    global losses

    if (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        print("You Win")
        wins += 1
    elif user_choice == computer_choice:
        print("Tie")
    else:
        print("You Lose")
        losses += 1

current_round = 1
wins = 0
losses = 0

while True:
    try:
        rounds = int(input("How many rounds would you like to play?     :"))
        if rounds > 0:
            break
        else:
            print()
            print("Please enter a number greater than 0")
    except ValueError:
        print()
        print("Please enter a whole number:     ")

print()
if rounds == 1:
    print("There will be 1 round")
else:
    print("Ok! There will be", rounds, "rounds.")
print()

while current_round <= rounds:
    print("Round", current_round, ":")
    
    while True:
        user_choice = input("What would you like to play? : ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            break
        else:
            print()
            print("Please enter: rock, paper, or scissors.")

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print()
    print("Rock...")
    time.sleep(0.37)
    print("Paper...")
    time.sleep(0.37)
    print("Scissors...")
    time.sleep(0.37)
    print("Shoot!")
    print()
    print(user_choice, "vs", computer_choice)

    result(user_choice, computer_choice)
    print()

    current_round += 1

if wins + losses == 0:
    print("Every round was a tie!")
    print("No win rate could be calculated.")
    print()
    time.sleep(2.5)
    print("(You still failed.)")
    print("Better luck next time!")
else:
    win_rate = (wins / (wins + losses)) * 100

    if win_rate < 65:
        print("You...")
        time.sleep(2.5)
        print("Failed.")
        print("(Ties don't count)")
        print()
        print("Better luck next time!")
    else:
        print("You...")
        time.sleep(2.5)
        print("Passed!")

    print()
    print(f"Your win rate is {win_rate:.1f}%")

print()
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print(f"Ties: {rounds - wins - losses}")