U = input("Is this in Celsius or Fahreheit(C/F):").capitalize().strip()
T = float(input("Enter the temperature: "))
if U == "C":
    T = round((9*T)/5+32,1)
    print(f"The temperature in Fahrenheit is:{T} °F.")
elif U == "F":
    T = round((T-32)*5/9,1)
    print(f"The temperature in Celsius is:{T} °C.")
else:
    print(f"{U} is an invalid unit of measurement.")