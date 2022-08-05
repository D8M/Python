
# for letter in ['h', 'e', 'l', 'l', 'o']:
#     print(letter)


# for letter in "Iteration":
#     print(letter)

# any_string = "ffgnjkoshjbhjgsb"
# for char in any_string:
#     print(char)

# for digit in '10': # String treated as a list of 2 chars
#     print(digit)

# for digit in 10: # Not iterable int
# print(digit)
#############################################################

# Iterating over elements in Tuple or Dict

# cars = ("Ford Ranger", "Toyota Celica", "Mercedes E Class",
#         "Tesla Model S")  # Tuple of cars
# for car in cars:
#     print("\nIt's a ", car)

# car_speed = (("Ford Ranger", 100), ("Toyota Celica", 140), ("Mercedes E Class", 130), ("Tesla Model S, 180")
#              )
# for i, (car, speed) in enumerate(car_speed):
#     print("\nThe Car at index %d is a %s and its max speed is %s mph" %
#           (i, car, speed))

####################################################################

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    result = num * 10

    print(result, "Is the result of ", num, " times 10 ")

#####################################################################
results = []

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = 0
for val in numbers:
    results.append(val ** 2)
    print("\nSquare of ", val, " is ", square)


print("\nResults: ", results)

#######################################################################

# string = input("\nEnter a word please: ")

# counter = 0
# for i in string:
#     counter = counter + 1
# print(counter)

########################################################################

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    print(num)
else:
    # The program will enter the else block after all for loop iterations completed
    print("\nNo more items in list")

##########################################################################

colours_list = ["Red", "Green", "Blue"]
items_list = ["Pen", "Marker", "Pencil"]

for colour in colours_list:
    for item in items_list:

        print(colour, item)

###########################################################################
