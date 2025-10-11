#python quiz game
questions = ("What do cows drink?",
    "Why did the computer go to the doctor?",
    "Which fruit is always sad?",
    "What do you call a bear with no teeth?")
options = ( ("a) Milk", "b) Water", "c) Juice", "d) Soda"),
    ("a) It caught a virus", "b) It had a headache", "c) It was tired", "d) It needed a reboot"),
    ("a) Apple", "b) Blueberry", "c) Grapes", "d) Lemon"),
    ("a) Polar bear", "b) Gummy bear", "c) Teddy bear", "d) Brown bear"))
answers = ("b", "a", "b", "b")
guesses = []
score = 0 
q_number = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[q_number]:
        print(option)

    guess = input("Enter the correct option (a,b,c,d): ").lower()
    guesses.append(guess)
    if guess == answers[q_number]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[q_number]} is the correct answer.")
    q_number += 1

print("---------------------------")
print("         RESULTS           ")    
print("---------------------------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/len(questions)*100)
print(f"Your score is {score}%.")