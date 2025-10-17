#!/usr/bin/env python3
import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input(f"Enter either {options[0]}, {options[1]} or {options[2]}: ").lower().strip()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
        last_result = "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
        last_result = "win"
    else:
        print("You lose!")
        last_result = "lose"

    while True:
        quit_prompt = input("Play again? (y/n): ").lower().strip()
        if quit_prompt == "y":
            break  # continue the game
        elif quit_prompt == "n":
            if last_result == "lose":
                # Sarcastic message for losing player
                quit_prompt = input("Of course you want to quit now that you have lost. Boo hoo! Really, do you want to quit? (y/n): ").lower().strip()
                if quit_prompt == "y":
                    running = False
                    break
                # If they say 'n', continue the game
            else:
                running = False
                break
        else:
            print("Please enter 'y' or 'n'.")

print("Thanks for playing!")
