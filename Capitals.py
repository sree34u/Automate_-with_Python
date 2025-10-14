#dictionary collection of {key:value pairs} ordered changeable but no duplicates
#The program finds capital of countries and let's user add missing countries and capitals(no persistance)
capitals = {"USA":"Washington", "India":"Delhi","China":"Beijing"}

while True:
    country = input("Enter the country name to get it's capital(q to quit): ").strip().title()
    
    if country.lower() == 'q':
        print("Exiting the program. Goodbye!")
        break

    if capitals.get(country):
        print(f"The capital of {country} is {capitals.get(country)}")
    else:
        print(f"The capital of {country} is not known.")
        capital = input(f"Enter the capital of {country}:").strip().title()

        capitals[country] = capital
        print(f"{country} with capital {capital} has been added to the collection.")