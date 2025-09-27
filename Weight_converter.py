#Python Weight Converter
W = float(input("Enter your weight: "))
U = input("Enter your weight units in Kilogram or Pounds (enter K or L only):").capitalize().strip()
if U == "K":
    W = round(W * 2.205, 3)
    U = "Lbs."
    print(f"Your weight in pounds is {W} {U}")
elif U == "L":
    W = round(W / 2.205, 3)
    U = "Kgs"
    print(f"Your weight in Kilos is {W}{U}")
else:
    print(f"{U} is not a valid unit.")