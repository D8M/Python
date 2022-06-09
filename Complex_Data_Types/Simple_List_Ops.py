# Simple List Operations
# List index starts at 0, elements start at 1

list_of_available_cars = ["Mercedes Benz E220", "Landrover Defender LWB",
                          "Mercedes Unimog", "Mitsubshi Warrior", "Tesla Model S", "Nissan Juke", "Nissan Bluebird"]

# Add new Element to the end of the above list use .append method on the list, its called & modifies the list itself - 1 element at a time

list_of_available_cars.append("BMW 330D")
# print(list_of_available_cars)

# Inserts a new element at specific index position, in this case position 4 - other elements shifted to the right
list_of_available_cars.insert(4, "Fiat Daily")
# print(list_of_available_cars)

#print("The number of available vehicles is: ", len(list_of_available_cars))
# Below, using .extend method to add multiple elements to the end of the list - takes another List as input argument
list_of_available_cars.extend(
    ["Ford Galaxy", "Ford SMAX", "Volkswagen Caddy 7 Seater"])
print(list_of_available_cars)
print("The number of available vehicles is: ", len(list_of_available_cars))

expensive_cars_list = ["Ferrari 340", "Bugatti Veyron",
                       "Porshe 911 Turbo", "Range Rover Vogue SE"]
# Concatenate lists creates a new list - original unaffected
complete_cars_list1 = list_of_available_cars + expensive_cars_list
print("Complete cars list: ", complete_cars_list1)

# complete_cars_list1.index[8]
print("Car at position is: ", complete_cars_list1.index(
    "Ford SMAX"))  # Has to be an exact match of query

complete_cars_list1.remove("Ferrari 340")  # Removes queried element
print("Complete cars list: ", complete_cars_list1)
