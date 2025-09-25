#A Simple Python Calculator

N1 = float(input("Enter first number:"))
O = input("Enter an operator(+ - * /):")
N2 = float(input("Enter second number:"))

if O == "+":
    R = N1 + N2
    print(round(R, 3))
elif O == "-":
    R = N1 - N2
    print(round(R, 3))
elif O == "*":
    R = N1 * N2
    print(round(R, 3))
elif O == "/":
    R = N1 / N2
    print(round(R, 3))