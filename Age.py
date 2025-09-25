# Exercise: Use if-elif-else statements to respond according to age

age = int(input("Enter your age:"))
if age > 100:
    print("You are too old.")
elif age < 0:
    print("You are not even born yet!")
elif age > 18:
    print("You are legally an adult.")
else: 
    print("You need to be an adult.")