#msg = "Hello World"
# print(msg)
#spam = (3 + 4 + 7)
# print(spam)

# price = 3.95
# widgets = 10
# print("The price of the widget is: ", price)
# # Dont use + to concatenate use ,(comma)  instead
# print("We have " + str(widgets) + " in stock>")
# print(int(price), float(widgets))


# north = 200
# south = 300
# northwins = north > south
# southwins = south > north
# print("Northwins = ", northwins, "\nSouthwins = ", southwins)

# from re import A


# regions = ["North", "South", "East", "West"]
# sales = [3000, 2000, 4000, 5400]
# employees = ["Alice", "Vera", "Flo", "Mel"]
# locations = []

# for employee in employees:
#     print(employee)

# employees.append("Belle")
# employees.remove("Flo")
# employees.sort()

# for employee in employees:
#     print(employee)

# # Slicing - pulling a piece outa list to display using index numbering
# print("Region: ", regions[0], " Sales: ", sales[0])

# # Same as above -1 shows last index position data
# print("Region: ", regions[-1], " Sales: ", sales[-1])

# employees[3] = "Belle"
# for employee in employees:
#     print(employee)
# employees.sort()

# a = 8
# b = 3

# print(a ** b)
# print(a % b)

# a = 3
# b = a
# print(a)


from ntpath import join
from pickle import EMPTY_LIST


# why_1 = 'She said, "Hello there!"'
# print(why_1)
# print('*' * 40)
# print(why_1.upper())
# print(why_1.isalpha())
# print(why_1.isdigit())
# csv = "David, Bernard, Mahon"
# print('csv.split(",")', csv.split(","))
# print(",".join(["David", " Bernard", " Mahon"]))

# print('*' * 80)
# EMPTY_LIST = list()

# list_str = list("Hello")
# print(list_str)
# print(sorted(list_str))
# print(list_str)
# list_str.reverse()
# print(list_str)
# print(list_str.count("l"))

# print("Length of list -> ", len(list_str))

print('*' * 80)
print('*' * 80)

a_tuple = ('a', 1, 2, (3, 4, 5, 6), 7, 8, 9, 10)
a_string = "immutable"
a_bytes = b"some_sequence"

a_list = [5, 6, 7, 8, (4, 5)]
a_byte_array = bytearray(b"mutable")

print(a_tuple[3])
print(a_tuple[-1])
print(a_list[0:2])

