import math
"""
This program defines hotel cost function and takes in two arguments: nights and room_type.
It then stores the room prices in a dictionary room_prices. The get method of the dictionary 
is used to get the price for the given room type, uses the if loop to return None if the room 
type is not found. It then returns the calculation of nights and price_per_night. It then 
prompts user tot enter 2 inputs. It then calculates the toal price and print it if it was 
successfully calculated
"""
def hotel_cost(nights, room_type):
    room_prices = {"Standard Room": 125, "Luxury Room": 150, "super Lux Room": 250}
    price_per_night = room_prices.get(room_type)
    if price_per_night is None:
        print("Invalid room type.")
        return
    return nights * price_per_night

nights = int(input("Please enter number of nights: "))
room_type = input("Please enter room type (Standard Room, Luxury Room or super Lux Room): ")

total_price = hotel_cost(nights, room_type)
if total_price:
    print("Total price:", total_price)

"""
Store the prices of flights to each city in a dictionary. Retrieve the price for the given city
Return the cost of the flight or None if the city is not found. Get the city from the user
Calculate the cost of the flight. Print the cost of the flight if it was successfully calculated
""" 
def plane_cost(city):
    flight_prices = {"Milan": 300, "Amsterdam": 150, "Paris": 250}
    cost_of_flight = flight_prices.get(city)
    return cost_of_flight or print("Invalid city.")

city = input("Please enter the name of the city you are travelling to (Milan, Amsterdam or Paris): ")

cost_of_flight = plane_cost(city)
if cost_of_flight:
    print("Cost of flight:", cost_of_flight)


"""
The code defines two functions: calculate_rental_cost and print_rental_cost. The first function calculates
the total cost of a car rental based on the number of hours and the type of car. If the car type is invalid
it returns None. The second function prints the total cost of the rental if it was successfully calculated
or a message that the car type is invalid if not. The code takes input from user for the number of hours and 
the type of car, and calls the print_rental_cost function to print the total cost.
"""
def car_rental(hours, car_type):
    car_prices = {"Economy": 15, "Standard": 30, "Luxury": 100}
    price_per_hour = car_prices.get(car_type)
    if not price_per_hour:
        return None
    return hours * price_per_hour

def print_rental_cost(hours, car_type):
    cost = car_rental(hours, car_type)
    if cost is None:
        print("Invalid car type.")
    else:
        print(f"Total cost: {cost}")

hours = int(input("Please enter the number of hours: "))
car_type = input("Please enter the type of car (Economy, Standard, Luxury): ")
print_rental_cost(hours, car_type)


"""
This code defines three functions for calculating the costs of a hotel stay, plane ticket, and car rental for a
holiday. The hotel_cost function takes the number of nights and room type and returns the total cost of the hotel 
stay. The plane_cost function takes the city and returns the cost of a plane ticket, lookin up the flight prices. 
The car_rental function takes the number of rental hours and car type and returns the cost of the car rental, 
looking up the car rental prices. The holiday_cost function adds up the costs of the hotel stay, plane ticket, 
and car rental and returns the total cost of the holiday. If any of the inputs for the three arguments are 
invalid, the functions print an error message and return None.
"""
def holiday_cost(nights, city, hours):
    hotel_price = hotel_cost(nights, room_type)
    flight_price = plane_cost(city)
    rental_price = car_rental(hours, car_type)

    if not all([hotel_price, flight_price, rental_price]):
        print("Invalid inputs.")
        return

    return hotel_price + flight_price + rental_price

total_holiday_cost = holiday_cost(nights, city, hours)
if total_holiday_cost:
    print("Total holiday cost:", total_holiday_cost)