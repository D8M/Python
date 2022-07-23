# Swapper list

# cars_list = ["Toyota Camry", "Honda Accord", "Ford Ranger",
#              "Mercedes Benz", "VW Golf", "Skoda Octavia"]

# print("\nList of cars before the swap: ", cars_list)
# #var below
# cars_list_temp = cars_list[0]
# cars_list[0] = cars_list[2]

# cars_list[2] = cars_list_temp # This is a variable storing Toyota Camry
# print("\nList of cars after swap: ", cars_list)


#######################################################################

cars_list = ["Toyota Camry", "Honda Accord", "Ford Ranger",
             "Mercedes Benz", "VW Golf", "Skoda Octavia"]

print("\nList of cars before the swap: ", cars_list)

car1 = 1
car2 = 2

cars_list[car1], cars_list[car2] = cars_list[car2], cars_list[car1]
print("\nList of cars after swap: ", cars_list)




