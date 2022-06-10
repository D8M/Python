# a = a + 1
# a += 1
# Same

list_of__cars = ["Mercedes Benz E220", "Landrover Defender LWB",
                 "Mercedes Unimog", "Mitsubshi Warrior", "Tesla Model S", "Nissan Juke", "Nissan Bluebird"]

list_of_traded_in_cars = ["Jeep Cherokee", "2010 Range Rover", "Ford Cortina"]
list_of_cars_for_recycling = ["Toyota Starlet", "Hyundai Trajet"]
list_of_cars_for_spares = ["Ford Mondeo Ghia", "Volvo XC90"]

# Appends spares list to end of the recycling list
temp_list = list_of_cars_for_recycling + \
    list_of_cars_for_spares  # Shallow copy
# print(temp_list)

complete_stock_list = list_of__cars + temp_list

# complete_stock_list.reverse()
complete_stock_list.sort()
#print("Complete stock list: ", complete_stock_list)
complete_stock_list.pop()  # Removes last index element
#print("Complete stock list: ", complete_stock_list)

#print(complete_stock_list.count("Toyota Starlet"))
complete_stock_list.append("Ford Cougar")
# print(complete_stock_list)
complete_stock_list.append("Ford Cougar")
# print(complete_stock_list)

unique_list = set(complete_stock_list)
print(unique_list)
# complete_stock_list.clear() # Clears the list fully - del kills the list for good - no longer in memeory
# complete_stock_list.copy() Performs a deep copy - entirely new list created - chnages to original does not affect the copy
