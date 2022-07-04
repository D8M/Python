list_of__cars = ["Mercedes Benz E220", "Landrover Defender LWB",
                 "Mercedes Unimog", "Mitsubshi Warrior", "Tesla Model S", "Nissan Juke", "Nissan Bluebird"]

print("Shows list of cars List with start & end indexes and Step size: ",
      list_of__cars[:6:2])  # start index : end index : step size

print("\nWith -1 step this shows list of cars starting at last index - shows list in reverse ",
      list_of__cars[::-1])  # start index : end index : step size in minus, shows list in reverse

# print("\nShows list of cars List starting at index 6 and ending at last and inserts two new elements  ",
# list_of__cars[:6:-1] = ["Ford Focus", "Ford Ranger"])

print("Nissan Juke" in list_of__cars)  # In command
list_of__cars.pop(-2)
print("\n", list_of__cars)
print("\nNissan Juke" in list_of__cars)  # In command
