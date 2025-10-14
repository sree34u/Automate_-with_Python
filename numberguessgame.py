#Number guessing game 
import random

low = 1
high = 100
answer = random.randint(low,high)
guesses = 0
is_running = True

print("Python guessing game!!!")
print(f"Select a number between {low} and {high}.")

while is_running:
    guess = input(f"Guess a number between {low} and {high}:")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess > high or guess < low:
            print("The number is out of range.")
            print(f"Select a number between {low} and {high}.")
        elif guess < answer:
            print("Number is tool low! Try again!")
        elif guess > answer:
            print("Number is tool High! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"The number of guesses you took: {guesses}")
            is_running = False
    
    else:
        print("Invalid guess!")
        print(f"Please select a number between {low} and {high}")

