#This is a compound interest calculator using while loop.
principle = 0
rate = 0
years = 0

while principle <= 0:
    principle = float(input("Enter the principle amount:"))
    if principle <= 0:
        print("Principle cannot be less than or equal to zero.")
    
while rate <= 0:
    rate = float(input("Enter the interest rate:"))
    if rate <= 0:
        print("Interest rate cannot be less than or equal to zero.")

while years <= 0:
    years = int(input("Enter the number of years:"))
    if years <= 0:
        print("Number of years cannot be less than or equal to zero.")

total = principle * pow((1+rate/100), years)
print(f"Balance after {years} years is:₹{total:.2f}")