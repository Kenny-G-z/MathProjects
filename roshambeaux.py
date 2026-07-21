import random

def result(user_choice, computer_choice):
    if (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        return "You Win"
    elif user_choice == computer_choice:
        return("Tie")
    else:
        return("You Lose")

def play(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    outcome = result(user_choice, computer_choice)
    
    return {"user": user_choice, "computer": computer_choice,"result": outcome}