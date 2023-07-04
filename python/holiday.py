# Function to calculate the hotel cost based on number of nights
def hotel_cost(num_nights):
    price_per_night = 100  # Assuming the hotel charges £100 per night
    return price_per_night * num_nights

# Function to calculate the flight cost based on the destination city
def plane_cost(city_flight):
    if city_flight == "New York":
        return 500
    elif city_flight == "London":
        return 1000
    elif city_flight == "Sydney":
        return 1500
    else:
        return 0

# Function to calculate the car rental cost based on number of rental days
def car_rental(rental_days):
    daily_rental_cost = 50  # Assuming the rental car costs £50 per day
    return daily_rental_cost * rental_days

# Function to calculate the total holiday cost based on the above functions
def holiday_cost(city_flight, num_nights, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

# User inputs
city_flight = input("Enter the city you will be flying to (options: New York, London, Sydney): ")
num_nights = int(input("Enter the number of nights you will be staying at the hotel: "))
rental_days = int(input("Enter the number of days that you will be hiring a car for: "))

# Calculation of the total holiday cost
total_holiday_cost = holiday_cost(city_flight, num_nights, rental_days)

# Printing the details of the holiday
print("\nDetails of your holiday:")
print(f"City of flight: {city_flight}")
print(f"Number of nights at the hotel: {num_nights}")
print(f"Number of days for car rental: {rental_days}")
print(f"Total cost of your holiday: £{total_holiday_cost}")
