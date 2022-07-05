list_of__cars = ["Mercedes Benz E220", "Landrover Defender LWB",
                 "Mercedes Unimog", "Mitsubshi Warrior", "Tesla Model S", "Nissan Juke", "Nissan Bluebird"]

print(len(list_of__cars))  # Length of list
# Access individual index position - Remember, element 1 is at Index 0
print((list_of__cars[4]))
# counts back elements from last element of the list
print((list_of__cars[-2]))

# Slicing allows for accessing a range of elements in a list , if you store the result of your slicing in a var this creates a deep copy - ie a new list with the range specified. Changes to the original list do not affect the deep copy
# [Start index : End Index] End index is exclusive - in this case first 4 elements or 0 to 3 index
print(list_of__cars[0: 4])

print("Apply with greater amount of index than exists - shows entire list: ",
      list_of__cars[0: 10])
print("\nStart with index greater than what exists - shows empty list",
      list_of__cars[8:])
print("\nStart with only end index  - Python infers 0 start index",
      list_of__cars[:4])
print("\nStart at index 0 & got to -4  - Py starts counting back from endof list to the 4th last element and then shows the elements from 0 to where it counted back to from e.o.l but the last element specified is exclusive",
      list_of__cars[0:-4])
print("\nStart at index -4 from last, and go back to -2 from last, - Starts at -4 and shows elements from 4th last to 3rd last as -2 or second last is exclusive: ",
      list_of__cars[-4: -2])
