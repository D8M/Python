# Introducing Lists
# A List is an ordered collection of elements specified in square brackets
# List start at index position 0

from pickle import EMPTY_LIST


# EMPTY_LIST = []
# print(EMPTY_LIST)

# list_str = ["Volkswagen Beetle", "Ford Ranger",
#             "Toyota Celica", "Mercedes Benz"]
# print(list_str)

# list_floats = [5.3, 6.7, 9.0, 2, 2]
# print(list_floats)

# # Lists can contain duplicates, & order is important, elements are accessed in the order that they appear
# # List containing Differing data types is ok
# mixed_list = ['Datsun 300', 1, 3.99, True, ]

# print("Chosen Car is a...", list_str[1])
# # Last indices are at -1, second last at -2 and so on...
# # Total length -1 is the Last index (element info)
# print("Chosen Car is a...", list_str[-1])

# print(len(list_str))  # len prints out the number of elements ina list
# # Inserts a new element inot position 0 of the list - overwrites whats there
# list_str[0] = "Landrover Defender"
# print(list_str)

# WORKING WITH NESTED LISTS

car_matrix = [  # List of nested lists
    ["Volkswagen Beetle", "Ford Ranger"],
    ["Toyota Celica", "Mercedes Benz"]
]
print(len(car_matrix))

# print(list_str)
