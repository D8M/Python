list_of__cars = ["Mercedes Benz E220", "Landrover Defender LWB",
                 "Mercedes Unimog", "Mitsubshi Warrior", "Tesla Model S", "Nissan Juke", "Nissan Bluebird"]

list_numbers = [1, 44, 87, 55, 99, 22, 101.101]

print(max(list_numbers))
print(min(list_numbers))
list_numbers.sort()
print(sum(list_numbers))

# list_numbers *= 2 is the same as list_numbers = list_numbers * 2 Only works on Ints
print(all(list_numbers))
print(any(list_numbers))
