# concession stand programme

menu = {"pizza":4.71, "popcorn":13.2, "burger":4.78, "chips":2.98, "fries":7.32, "nachos":3.43}

cart = []
Total = 0

print("----------MENU----------")
for key,value in menu.items():
    print(f"{key:10}:₹{value:.2f}")
print("------------------------")

while True:
    food = input("select an item from menu(q to quit):").lower().strip()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print(cart)

print("----------YOUR ORDER--------")
for food in cart: 
    Total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ₹{Total:.2f}")

print("----------------------------")